
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTransform
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush
from random import randint, uniform, triangular, sample, shuffle
from math import sqrt, floor
from slide import Slide
from sprites import SpriteType
import random
import math
import PyQt4

class SlideGen(Slide):
    MIN_COUNT = 250
    MAX_COUNT = 750
    current_focus = 2.2
    
    def __init__(self, parent):
        super(SlideGen, self).__init__(parent)
        self.initCells()
        
    def initCells(self):
        # init the layers
        for i in range(0, SlideGen.MAX_COUNT-1):
            cell = QtGui.QGraphicsPixmapItem()
            rdepth = random.uniform(0.0, 4.0)

            cell.setZValue(rdepth) #set random depth
            cell.setVisible(False)
            cell.setTransformationMode(QtCore.Qt.SmoothTransformation)

            self.scene.addItem(cell)
    
    def genSlide(self):
        self.current_focus = 2.2
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
            depth = cell_list[i].zValue()
            
            texture, rotation, blur = self.get_texture(
                int(SpriteType.APHANOTHECE_OUTLINE), depth, deg_rotation, self.current_focus)
            
            effect = PyQt4.QtGui.QGraphicsBlurEffect()
            effect.setBlurRadius(blur)
            
            cell_list[i].setPixmap(texture)
            cell_list[i].setRotation(rotation)
            cell_list[i].setGraphicsEffect(effect)
            cell_list[i].setVisible(True)
        
        #hide the rest
        for i in range (this_count, SlideGen.MAX_COUNT-1):
            cell_list[i].setVisible(False)
            
        self.cell_count = this_count
        
    def updateSlide(self):
        cell_list = self.scene.items()
        
        for i in range (0, SlideGen.MAX_COUNT-1):
            cell = cell_list[i]

            if cell.isVisible():
                depth = cell.zValue()
                blur, sprite_depth = self.get_blur(depth, self.current_focus)
                
                effect = PyQt4.QtGui.QGraphicsBlurEffect()
                effect.setBlurRadius(blur)
                cell_list[i].setGraphicsEffect(effect)
                cell_list[i].update()
        
    def count(self):
        return self.cell_count
        
    def wheelEvent(self, event):
        self.current_focus = self.current_focus + (event.delta()/120)
        self.updateSlide()