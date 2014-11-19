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


class SlideScene(QtGui.QGraphicsScene):
    #sprite
    SPRITE_PATH = "./img/sprites/"
    CELL_SCALE_SIZE = 20
    
    #slide
    SLIDE_PADDING = CELL_SCALE_SIZE / 3
    SLIDE_FOCUS_STEP = 0.2
    
    CELL_DEPTH_ALPHA = 0.2
    CELL_DEPTH_BLUR_FACTOR = 3.3
    
    #shared texture lib... need LoadTextureLib()
    texture_lib = None
    
    def __init__(self, sceneRect, parent = None, ):
        super(SlideScene, self).__init__(sceneRect, parent)
        
        #setup current focus
        self.current_focus = 2.4
        self.cell_count = 0
        
        #parent ref
        self.parent = parent

        #Load and set view background
        bgPath = os.path.normpath("./img/backgrounds/b0.png")
        bg_texture = QtGui.QPixmap(os.path.join(os.path.curdir, bgPath))
        background = QtGui.QBrush(bg_texture)
        
        self.setBackgroundBrush(background)
        
        #load textures
        self.load_textures(self.SPRITE_PATH)
        
#        #test
#        self.placeCell(200, 300, 2, 0, 0)
#        self.placeCell(215, 300, 2, 180, 0)
#        self.resetSlide()
#        
#        self.placeCell(270, 270, 1, 90, 1)
#        self.placeCell(0, 270, 2, 0, 0)
#        self.placeCell(0, 0, 2, 0, 0)
#        self.placeCell(540, 0, 2, 0, 0)        
#        self.placeCell(540, 270, 2, 0, 0)
#        self.placeCell(540, 540, 2, 0, 0)
#        self.placeCell(0, 540, 2, 0, 0)
#        
#        self.placeCell(220, 300, 1.8, 180, 1)
#        self.placeCell(260, 300, 2.6, 60, 1)
#        self.placeCell(290, 300, 3.8, 90, 1)
#        self.updateSlide()

    def updateSlide(self):
        for cell in self.items():
            if cell.isVisible():
                depth = cell.zValue()
                blur, sprite_depth = self.get_blur(depth, self.current_focus)
                
                #remove effect
                cell.setGraphicsEffect(None)
                
                if blur > 12:
                    blur = 12.0

                if blur > 1.5:                        
                    effect = QtGui.QGraphicsBlurEffect()
                    effect.setBlurRadius(blur)
                    cell.setGraphicsEffect(effect)
                
                cell.update()
    
    def load_textures(self, sprite_path):
        #Load Sprites
        spritePath = os.path.normpath(sprite_path)
        self.sprites = SpriteFactory(os.path.join(os.path.curdir, spritePath))
        self.texture_lib = {}

        scaledSize = QtCore.QSize(self.CELL_SCALE_SIZE, self.CELL_SCALE_SIZE)
        
        #Load Textures
        for cellType in range(SpriteType.COUNT):
            for depth in range (1, 4): # 1, 2, 3
                for degree in range(0, 360, 15):
                    filename, rotation = self.sprites.get_sprite(cellType, str(depth), degree)
                    key = "t"+str(cellType)+"d"+str(depth)+"r"+str(degree);
                    
                    if int(rotation) == 0:
                        texture = QtGui.QPixmap(filename)
                        texture = texture.scaled(scaledSize, 
                                                QtCore.Qt.KeepAspectRatio, 
                                                QtCore.Qt.SmoothTransformation )
                        self.texture_lib[key] = texture
    
    def placeCell(self, xPos, yPos, zPos, rotation, spriteType):
        """Places a single cell into the graphics scene"""
        #make cell
        cell = QtGui.QGraphicsPixmapItem()
        cell.setTransformationMode(QtCore.Qt.SmoothTransformation)        
        
        texture, deg_offset, blur = self.get_texture(spriteType, zPos, rotation)
        
        #set texture
        cell.setPixmap(texture)

        #rotate
        trans = QtGui.QTransform()
        trans.translate(self.CELL_SCALE_SIZE / 2, self.CELL_SCALE_SIZE / 2)
        trans.rotate(deg_offset)
        trans.translate(-self.CELL_SCALE_SIZE / 2, -self.CELL_SCALE_SIZE / 2)
        cell.setTransform(trans)
        
        #set visible        
        cell.setVisible(True)        
        
        #set pos
        cell.setPos(xPos - (self.CELL_SCALE_SIZE / 2), yPos - (self.CELL_SCALE_SIZE / 2))
        cell.setZValue(zPos)

        #store extra info
        cell.sprite_rotation = rotation
        cell.sprite_code = spriteType
        
        self.addItem(cell)
        self.cell_count += 1
        
    def resetSlide(self):
        self.clear()
        self.cell_count = 0
                                            
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
        outputimg = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        painter = QtGui.QPainter(outputimg)
        targetrect = QtCore.QRectF(0, 0, self.width(), self.height())
        sourcerect = QtCore.QRectF(0, 0, self.width(), self.height())

        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        self.render(painter, targetrect, sourcerect, QtCore.Qt.KeepAspectRatio)
        painter.end()

        #scale image
        scaledSize = QtCore.QSize(width, height)
        outputimg = outputimg.scaled(scaledSize, 
                    QtCore.Qt.KeepAspectRatio, 
                    QtCore.Qt.SmoothTransformation )

        outputimg.save(filename, "PNG")
        return filename
            
    def save_slide(self):
        """Loops through all items and save data serialized pickle"""
        cell_list = []
        
        for cell in self.items():
            if(cell.isVisible()):
                #print "cell: x=%d y=%d,z=%f type=%d rotation=%d" % (cell.x(), cell.y(), cell.zValue(), cell.sprite_code, cell.sprite_rotation)
                cell_list.append([cell.x(), cell.y(), cell.zValue(), cell.sprite_code, cell.sprite_rotation])

        output = open('last_slide.ace','wb')
        pickle.dump(cell_list, output)
        output.close()
        print "slide saved" 
        
    def count(self):
        return self.cell_count
        
    def wheelEvent(self, event):
        self.changeFocus(event.delta()/120.0)
#        print (event.delta()/120)
#        print self.current_focus
        
    def mousePressEvent(self, event):
        self.save_slide()        

    def setFocus(self, focus):
        print "A" + str(focus)
        self.current_focus = focus
        self.updateSlide()
        
    def changeFocus(self, delta):
        """Changes focus setting and calls update can be called when scrolling or clicking the buttons """
        check = self.current_focus + (delta * self.SLIDE_FOCUS_STEP)
        if(check > -1.2 and check < 5.8):
            self.current_focus = check
            # +1 so we use 0-7 range instead of -1-6, *15 to scale to 100
            self.parent.focus_slider.setSliderPosition(math.ceil((check+1.0)*15))