"""
slide.py

Superclass for slide display widgets
"""

from PyQt4 import QtGui, QtCore

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
        self.bg_texture = QtGui.QPixmap('background.jpg')
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)

        
        #Load and scale the texture for the algae cells
        scaledSize = QtCore.QSize(self.scale_size, self.scale_size)

        self.texture = QtGui.QPixmap('cell-test.png')
        self.texture = self.texture.scaled( scaledSize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.SmoothTransformation )
        
        self.texture2 = QtGui.QPixmap('cell-test2.png')
        self.texture2 = self.texture2.scaled( scaledSize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.SmoothTransformation )
       
       
