"""
slide.py

Superclass for slide display widgets
"""

from PyQt4 import QtGui, QtCore, Qt
from sprites import SpriteFactory, SpriteType, SpriteDepth
import os.path
#import sprites
import math
import pickle


class Slide(QtGui.QWidget):
    VIEW_WIDTH,VIEW_HEIGHT = 540,540
    SPRITE_PATH = "./img/sprites/"

    CELL_MIN_COUNT = 2
    CELL_MAX_COUNT = 2048
    
    CELL_SCALE_SIZE = 20
    SLIDE_PADDING = CELL_SCALE_SIZE / 3
    CELL_DEPTH_ALPHA = 0.2
    CELL_DEPTH_BLUR_FACTOR = 3.3
    
    #shared texture lib... need LoadTextureLib()
    texture_lib = None
    
    def __init__(self,parent):
        super(Slide, self).__init__(parent)
        
        #setup current focus
        self.current_focus = 2.4

        #widget size        
        self.setMinimumSize(self.VIEW_WIDTH, self.VIEW_HEIGHT)
        
        #create scene and view
        self.scene = QtGui.QGraphicsScene(  QtCore.QRectF(
                                                0,0,
                                                self.VIEW_WIDTH,
                                                self.VIEW_HEIGHT),
                                                self)

        self.view = QtGui.QGraphicsView(self.scene)
        self.view.setParent(self)
        self.view.setMinimumSize(QtCore.QSize(self.VIEW_WIDTH, self.VIEW_HEIGHT))
        self.view.setSizePolicy(    QtGui.QSizePolicy.MinimumExpanding,
                                    QtGui.QSizePolicy.MinimumExpanding)        

        #build layout        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        
        self.setLayout(layout)

        #Load and set view background
        bgPath = os.path.normpath("./img/backgrounds/b0.png")
        self.bg_texture = QtGui.QPixmap(os.path.join(os.path.curdir, bgPath))
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)
        
        #init empty cells         
        self.initCells()
        
        #load textures
        self.load_textures(self.SPRITE_PATH)
        
    def initCells(self):
        # init the layers
        for i in range(self.CELL_MAX_COUNT):
            #create a new cell            
            cell = QtGui.QGraphicsPixmapItem()
            cell.setVisible(False)
            cell.setTransformationMode(QtCore.Qt.SmoothTransformation)
            self.scene.addItem(cell)

    def updateSlide(self):
        cell_list = self.scene.items()
        
        for i in range (self.CELL_MAX_COUNT):
            cell = cell_list[i]

            if cell.isVisible():
                depth = cell.zValue()
                blur, sprite_depth = self.get_blur(depth, self.current_focus)
                
                #remove effect
                cell_list[i].setGraphicsEffect(None)
                
                if blur > 12:
                    blur = 12.0

                if blur > 1.5:                        
                    effect = QtGui.QGraphicsBlurEffect()
                    effect.setBlurRadius(blur)
                    cell_list[i].setGraphicsEffect(effect)
                
                cell_list[i].update()    
    
    
    
    def load_textures(self, sprite_path):
        #print "loading textures "+ str(self.texture_lib) + " " + str(sprite_path)
        
        #Load Sprites
        spritePath = os.path.normpath(sprite_path)
        self.sprites = SpriteFactory(os.path.join(os.path.curdir, spritePath))
        self.texture_lib = {}

        scaledSize = QtCore.QSize(self.CELL_SCALE_SIZE, self.CELL_SCALE_SIZE)
        
        #Load Textures
        for cellType in range(SpriteType.COUNT):
            for depth in range (1, 4):        
                for degree in range(0, 360, 15):
                    filename, rotation = self.sprites.get_sprite(cellType, str(depth), degree)
                    key = "t"+str(cellType)+"d"+str(depth)+"r"+str(degree);
                    
                    if int(rotation) == 0:
                        texture = QtGui.QPixmap(filename)
                        texture = texture.scaled(scaledSize, 
                                                QtCore.Qt.KeepAspectRatio, 
                                                QtCore.Qt.SmoothTransformation )
                        self.texture_lib[key] = texture

                                            
    def get_texture(self, cellType, depth, rotation, middle_focus=2.0):
        blur, sprite_depth = self.get_blur(depth, middle_focus)
        
        rotation_rounded = ((int)(math.floor(rotation)/15)*15)        
        key = "t"+str(cellType)+"d"+str(sprite_depth)+"r"+str(rotation_rounded)
        texture = None
        diff = 360
                
        for key, value in self.texture_lib.iteritems():
            
            t = int(key.split("d")[0][1:])
            if t != cellType:
                continue
            d = int((key.split("d")[1]).split("r")[0])
            if d != sprite_depth:
                continue
            degree =  int(key.split("r")[1])
            
            if degree == 0 and rotation > 180:
                degree = 360
            test = (rotation - degree)
            if math.fabs(test) <= math.fabs(diff):
                diff = test
                texture = value
        
        return texture, diff, blur
        
    def get_blur(self, depth, current_focus):
        amount = (current_focus - depth)
        sprite_depth = 2 #sets middle

        if abs(amount) > self.CELL_DEPTH_ALPHA:        
            if amount < 0:
                sprite_depth = 3
            else:
                sprite_depth = 1

        return abs(current_focus - depth) * self.CELL_DEPTH_BLUR_FACTOR, sprite_depth
        
    def save_image(self, filename, width, height):
        #outputimg = QtGui.QPixmap(width, height)
        #image_size = QtGui.Q
        outputimg = QtGui.QImage(self.VIEW_WIDTH, self.VIEW_HEIGHT, QtGui.QImage.Format_RGB32)
        painter = QtGui.QPainter(outputimg)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        targetrect = QtCore.QRectF(0, 0, self.VIEW_WIDTH, self.VIEW_HEIGHT)
        sourcerect = QtCore.QRectF(0, 0, self.VIEW_WIDTH, self.VIEW_HEIGHT)
        self.scene.render(painter, targetrect, sourcerect, QtCore.Qt.KeepAspectRatio)
        painter.end()
        scaledSize = QtCore.QSize(width, height)
        outputimg = outputimg.scaled(scaledSize, 
                    QtCore.Qt.KeepAspectRatio, 
                    QtCore.Qt.SmoothTransformation )
        outputimg.save(filename, "PNG")
        return filename
            
    def save_slide(self):
        #loop through all items and save data serialized json or pickle
        cell_list = []
        
        for cell in self.scene.items():
            if(cell.isVisible()):
                #print "cell: x=%d y=%d,z=%f type=%d rotation=%d" % (cell.x(), cell.y(), cell.zValue(), cell.sprite_code, cell.sprite_rotation)
                cell_list.append([cell.x(), cell.y(), cell.zValue(), cell.sprite_code, cell.sprite_rotation])

        output = open('last_slide.ace','wb')
        pickle.dump(cell_list, output)
        output.close()
        print "slide saved" 
