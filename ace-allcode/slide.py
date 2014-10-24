"""
slide.py

Superclass for slide display widgets
"""

from PyQt4 import QtGui, QtCore
from sprites import SpriteFactory, SpriteType, SpriteDepth
import os.path
#import sprites
import math

class Slide(QtGui.QWidget):
    VIEW_WIDTH,VIEW_HEIGHT = 540,540
    
    scale_size = 30
    depth_alpha = 0.2
    depth_blur_amount = 3.3
    
    
    def __init__(self,parent):
        super(Slide, self).__init__(parent)
        
        self.scene = QtGui.QGraphicsScene(  QtCore.QRectF(
                                                0,0,
                                                Slide.VIEW_WIDTH,
                                                Slide.VIEW_HEIGHT),
                                                self)

        self.view = QtGui.QGraphicsView(self.scene)
        self.view.setParent(self)
        self.view.setMinimumSize(QtCore.QSize(Slide.VIEW_WIDTH, Slide.VIEW_HEIGHT))
        self.view.setSizePolicy(    QtGui.QSizePolicy.MinimumExpanding,
                                    QtGui.QSizePolicy.MinimumExpanding)        

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        #Load and set view background
        bgPath = os.path.normpath("./img/backgrounds/b0.png")
        self.bg_texture = QtGui.QPixmap(os.path.join(os.path.curdir, bgPath))
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)

        #Load Sprites
        spritePath = os.path.normpath("./img/sprites/")
        self.sprites = SpriteFactory(os.path.join(os.path.curdir, spritePath))
        self.texture_lib = {}

        cellTypes = {SpriteType.APHANOTHECE_OUTLINE,
                     SpriteType.APHANOTHECE_RENDER1}
        scaledSize = QtCore.QSize(self.scale_size, self.scale_size)        
        
        #Load Textures
        for cellType in cellTypes:
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

                                            
    def get_texture(self, cellType, depth, rotation, current_focus=2.0):
        blur, sprite_depth = self.get_blur(depth, current_focus)
        
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

        if abs(amount) > self.depth_alpha:        
            if amount < 0:
                sprite_depth = 3
            else:
                sprite_depth = 1

        return abs(current_focus - depth) * self.depth_blur_amount, sprite_depth