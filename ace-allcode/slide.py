"""
slide.py

Superclass for slide display widgets
"""

from PyQt4 import QtGui, QtCore
from sprites import SpriteFactory, SpriteType, SpriteDepth
#import sprites
import math

class Slide(QtGui.QWidget):
    VIEW_WIDTH,VIEW_HEIGHT = 540,540
    
    scale_size = 24
    
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
        self.bg_texture = QtGui.QPixmap("./img/backgrounds/b2.png")
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)

        #Load Sprites
        self.sprites = SpriteFactory("./img/sprites/")
        self.texture_lib = {}

        cellTypes = {SpriteType.APHANOTHECE_OUTLINE,
                     SpriteType.APHANOTHECE_RENDER1}
        scaledSize = QtCore.QSize(self.scale_size, self.scale_size)        
        
        #Load Textures
        for cellType in cellTypes:
            for depth in range (1, 4):        
                for degree in range(0, 360, 15):
                    filename, rotation = self.sprites.get_sprite(cellType, str(depth), degree)
                    #print "filename="+filename+" rotation="+str(rotation)                
                    key = "t"+str(cellType)+"d"+str(depth)+"r"+str(degree);
                    
                    if int(rotation) == 0:
                        #print "added "+filename
                        texture = QtGui.QPixmap(filename)
                        texture = texture.scaled(scaledSize, 
                                                QtCore.Qt.KeepAspectRatio, 
                                                QtCore.Qt.SmoothTransformation )
                        self.texture_lib[key] = texture
            
        
        #print str(self.texture_lib)
        #Load and scale the texture for the algae cells
#        filename1, rotation = self.sprites.get_sprite(
#            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.FAR, 0.0)
#        filename2, rotation = self.sprites.get_sprite(
#            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.CENTER, 0.0)
#        filename3, rotation = self.sprites.get_sprite(
#            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.NEAR, 0.0)
#        
#        self.texture1 = QtGui.QPixmap(filename1)
#        self.texture1 = self.texture1.scaled( scaledSize, 
#                                            QtCore.Qt.KeepAspectRatio, 
#                                            QtCore.Qt.SmoothTransformation )
#
#        self.texture2 = QtGui.QPixmap(filename2)
#        self.texture2 = self.texture2.scaled( scaledSize, 
#                                            QtCore.Qt.KeepAspectRatio, 
#                                            QtCore.Qt.SmoothTransformation )
#
#        self.texture3 = QtGui.QPixmap(filename3)
#        self.texture3 = self.texture3.scaled( scaledSize, 
#                                            QtCore.Qt.KeepAspectRatio, 
#                                            QtCore.Qt.SmoothTransformation )
                                            
    def get_texture(self, cellType, depth, rotation):
        rotation_rounded = ((int)(math.floor(rotation)/15)*15)        
        key = "t"+str(cellType)+"d"+str(depth)+"r"+str(rotation_rounded)
        texture = None
        diff = 360
                
        for key, value in self.texture_lib.iteritems():
            
            t = int(key.split("d")[0][1:])
            if t != cellType:
                continue
            d = int((key.split("d")[1]).split("r")[0])
            if d != depth:
                continue
            degree =  int(key.split("r")[1])
            
            if degree == 0 and rotation > 180:
                degree = 360
            test = (rotation - degree)
            if math.fabs(test) <= math.fabs(diff):
                diff = test
                texture = value
        
        return texture, diff
        
            