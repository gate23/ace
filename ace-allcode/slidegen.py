
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTransform
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush
from random import randint, uniform, triangular, sample, shuffle
from math import sqrt, floor, pi, fabs
from slide import Slide
from sprites import SpriteType
import random
import math
import PyQt4

class SlideGen(Slide):
    MIN_COUNT = 1
    MAX_COUNT = 750
    current_focus = 2.5
    
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
        #self.current_focus = 1.9
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
                opt_r = sqrt(200 * size / pi)
                max_r = SlideGen.VIEW_HEIGHT/2
                R = triangular(opt_r, max_r, (opt_r + max_r) / 3)
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
                int(SpriteType.APHANOTHECE_OUTLINE), depth, deg_rotation)

            cell_list[i].setPixmap(texture)
            cell_list[i].setRotation(rotation)
            cell_list[i].setVisible(True)
        
        #hide the rest
        for i in range (this_count, SlideGen.MAX_COUNT-1):
            cell_list[i].setVisible(False)
            cell_list[i].setGraphicsEffect(None)
            
        self.cell_count = this_count
        self.updateSlide()
        
    def updateSlide(self):
        cell_list = self.scene.items()
        
        for i in range (0, SlideGen.MAX_COUNT-1):
            cell = cell_list[i]

            if cell.isVisible():
                depth = cell.zValue()
                blur, sprite_depth = self.get_blur(depth, self.current_focus)
                
                cell_list[i].setGraphicsEffect(None)
                
                if blur > 12:
                    blur = 12.0

                if blur > 1.5:                        
                    effect = PyQt4.QtGui.QGraphicsBlurEffect()
                    effect.setBlurRadius(blur)
                    cell_list[i].setGraphicsEffect(effect)
                
                cell_list[i].update()
        
    def count(self):
        return self.cell_count
        
    def wheelEvent(self, event):
        factor = 0.2
        check = self.current_focus + (event.delta()/120.0*factor)
        if(check > -1 and check < 6):
            self.current_focus = check
            self.updateSlide()
        #print (event.delta()/120)
        #print self.current_focus
