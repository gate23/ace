#Something within this module is causing the application to close abnormally.
#Crashes instead of exiting cleanly

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTransform
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush

from random import randint, uniform, triangular, sample
from math import sqrt


class SlideGen(QtGui.QWidget):
    MIN_COUNT = 500
    MAX_COUNT = 2500

    VIEW_WIDTH,VIEW_HEIGHT = 540, 540

    scale_size = 15
    
    def __init__(self, parent):
        super(SlideGen, self).__init__(parent)
        
        self.scene = QtGui.QGraphicsScene(  QtCore.QRectF(
                                                0,0,
                                                SlideGen.VIEW_WIDTH,
                                                SlideGen.VIEW_HEIGHT),
                                            self)
        
        self.view = QtGui.QGraphicsView(self.scene)
        self.view.setParent(self)
        self.view.setMinimumSize(QtCore.QSize(SlideGen.VIEW_WIDTH, SlideGen.VIEW_HEIGHT))
        self.view.setSizePolicy(    QtGui.QSizePolicy.MinimumExpanding,
                                    QtGui.QSizePolicy.MinimumExpanding)
        
        
        self.view.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.SmoothPixmapTransform)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        
        #Load and set view background
        self.bg_texture = QtGui.QPixmap('background.jpg')
        background = QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)
        
        #Load and scale the texture for the algae cells
        self.texture = QtGui.QPixmap('aphanothece1.png')
        self.texture = self.texture.scaled( QtCore.QSize(SlideGen.scale_size, SlideGen.scale_size) )
        
        self.blurred_texture = self.blurPixmap(self.texture)
        
        self.cell_count = 0

        self.initCells()
        
        
    def initCells(self):
        
        for i in range(0, SlideGen.MAX_COUNT-1):
            cell = QtGui.QGraphicsPixmapItem(self.texture)
            #Place the cell in non visible location
            cell.setPos(-500,-500)

            self.scene.addItem(cell)
    
    def genSlide(self):
        this_count = randint(SlideGen.MIN_COUNT, SlideGen.MAX_COUNT)
        cell_list = self.scene.items()
        num_blobs = int(triangular(1, 20, 10))
        shape_ends = sample(range(0, this_count-1), num_blobs-1)
        
        for i in range (0, this_count-1):

            #chooses the center point of the blob
            if ((i == 0) or (i in shape_ends)):
                x_offset = uniform(0.0, SlideGen.VIEW_WIDTH) 
                y_offset = uniform(0.0, SlideGen.VIEW_HEIGHT)
                R = triangular(1, SlideGen.VIEW_HEIGHT/2, 5)
                cell_list[i].setPos( x_offset, y_offset)
            #plot point around the center
            else:
                r = uniform(0, R)
                x = uniform(-r, r)
                y = sqrt(r**2 - x**2)
                cell_list[i].setPos(x_offset + x,y_offset + y)

            deg_rotation = uniform(0.0,359.9)
            cell_list[i].setRotation( deg_rotation)
        
        #hide the rest
        for i in range (this_count, SlideGen.MAX_COUNT-1):
            cell_list[i].setPos(-500,-500)
        
            
        self.cell_count = this_count
    
        
    def blurPixmap(self, in_pixmap):
        output = QtGui.QPixmap( in_pixmap.size() )
        output.fill( QtCore.Qt.transparent)
        
        painter = QPainter( output)
        
        #need to apply a blur effect to painter here
        
        return output
        
    def count(self):
        return self.cell_count
        