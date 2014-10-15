
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTransform
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush
from random import randint, uniform, triangular, sample, shuffle
from math import sqrt
from slide import Slide

class SlideGen(Slide):
    MIN_COUNT = 250
    MAX_COUNT = 750

    def __init__(self, parent):
        super(SlideGen, self).__init__(parent)
        self.initCells()
        
    def initCells(self):
        for i in range(0, SlideGen.MAX_COUNT-1):
            cell = QtGui.QGraphicsPixmapItem()
            if (i < self.MAX_COUNT / 3):            
                #cell = QtGui.QGraphicsPixmapItem(self.texture1)
                cell.setZValue(1.0)
            elif (i >= self.MAX_COUNT / 3 and i < self.MAX_COUNT * 3 / 4):
                #cell = QtGui.QGraphicsPixmapItem(self.texture2)
                cell.setZValue(2.0)
            else:
                #cell = QtGui.QGraphicsPixmapItem(self.texture3)
                cell.setZValue(3.0)

            #Place the cell in non visible location
            cell.setPos(-500,-500)
            cell.setTransformationMode(QtCore.Qt.SmoothTransformation)
            self.scene.addItem(cell)
    
    def genSlide(self):
        this_count = randint(SlideGen.MIN_COUNT, SlideGen.MAX_COUNT)
        cell_list = self.scene.items()
        shuffle(cell_list)
        num_blobs = int(triangular(1, 20, 10))
        shape_ends = sample(range(1, this_count-1), num_blobs-1)
        
        for i in range (0, this_count-1):

            #chooses the center point of the blob
            if ((i == 0) or (i in shape_ends)):
                if (i != 0):
                    shape_ends.remove(i)
                if (len(shape_ends) > 0):
                    next = min(shape_ends)
                    size = next - i
                else:
                    size = this_count - i
                x_offset = uniform(0.0, SlideGen.VIEW_WIDTH) 
                y_offset = uniform(0.0, SlideGen.VIEW_HEIGHT)
                R = triangular(size / 10, SlideGen.VIEW_HEIGHT/2, 5)
                cell_list[i].setPos( x_offset, y_offset)

            #plot point around the center
            else:
                r = uniform(0, R)
                x = uniform(-r, r)
                y = sqrt(r**2 - x**2)
                cell_list[i].setPos(x_offset + x,y_offset + y)

            deg_rotation = uniform(0.0,359.9)
            zvalue = cell_list[i].zValue()
            #print "zvalue=", zvalue
            #add the fuction to slide            
            texture, rotation = self.get_texture(1, int(zvalue), deg_rotation)
            #print "texture="+str(texture)+" rotation="+str(rotation)
            cell_list[i].setPixmap(texture)
            cell_list[i].setRotation(rotation)
        
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