"""
slide.py

Superclass for slide display widgets
"""

from PyQt4 import QtGui, QtCore
from sprites import SpriteFactory, SpriteType, SpriteDepth

class Slide(QtGui.QWidget):
    VIEW_WIDTH,VIEW_HEIGHT = 540,540
    
    scale_size = 24
    texture_lib = None

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
        self.bg_texture = QtGui.QPixmap("./img/backgrounds/b0.png")
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)

        #Load Sprites
        self.sprites = SpriteFactory("./img/sprites/")
        
        #Load and scale the texture for the algae cells
        scaledSize = QtCore.QSize(self.scale_size, self.scale_size)
        filename1, rotation = self.sprites.get_sprite(
            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.FAR, 0.0)
        filename2, rotation = self.sprites.get_sprite(
            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.CENTER, 0.0)
        filename3, rotation = self.sprites.get_sprite(
            SpriteType.APHANOTHECE_OUTLINE, SpriteDepth.NEAR, 0.0)
        
        self.texture1 = QtGui.QPixmap(filename1)
        self.texture1 = self.texture1.scaled( scaledSize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.SmoothTransformation )

        self.texture2 = QtGui.QPixmap(filename2)
        self.texture2 = self.texture2.scaled( scaledSize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.SmoothTransformation )

        self.texture3 = QtGui.QPixmap(filename3)
        self.texture3 = self.texture3.scaled( scaledSize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.SmoothTransformation )