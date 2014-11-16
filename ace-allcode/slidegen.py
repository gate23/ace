
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
    
    #used for focus control
    factor = 0.2
    
    def __init__(self, parent):
        super(SlideGen, self).__init__(parent)
        self.trainer_ref = parent
    
    def genSlide(self, parent, num_cells):
        #num_cells = 2000
        
        if(num_cells < self.CELL_MAX_COUNT and num_cells >= self.CELL_MIN_COUNT):
            this_count = num_cells
        else:
            rangenum = randint(3,10)
            low = 2**rangenum
            high = (2**(rangenum+1)) - 1
            this_count = int(triangular(low, high))

        #get cell list        
        cell_list = self.scene.items()

        pos_or_neg = [1,-1]
        try_again = []

        if (this_count < 20):
            max_blobs = this_count
        else:
            max_blobs = 20

        num_blobs = int(triangular(1, max_blobs))
        shape_ends = sample(range(1, this_count-1), num_blobs-1)
        
        for i in range (this_count):
            #update cell depth and type
            #depth = 2 + (random.randint(-16, 16)*0.1875) #range -2 to 5
            depth = 2 + (random.randint(-16, 16)*0.125) #range -1 to 4
            
            
            #choose sprite type
            sprite_type = random.choice(SpriteType.APHANOTHECE_RENDER1)
            
            #choose random rotation
            deg_rotation = uniform(0.0,359.9)

            texture, rotation, blur = self.get_texture(
                sprite_type, depth, deg_rotation)
            
            #set vals
            cell_list[i].setZValue(depth)
            cell_list[i].setPixmap(texture)
            cell_list[i].setRotation(rotation)
            cell_list[i].setVisible(True)
            cell_list[i].sprite_rotation = deg_rotation
            cell_list[i].sprite_code = sprite_type
            
            #chooses the center point of the blob
            if ((i == 0) or (i in shape_ends)):
                if (i != 0):
                    shape_ends.remove(i)
                if (len(shape_ends) > 0):
                    next = min(shape_ends)
                    size = next - i
                else:
                    size = this_count - i
                
                x_offset = uniform(self.SLIDE_PADDING, SlideGen.VIEW_WIDTH - self.SLIDE_PADDING) 
                y_offset = uniform(self.SLIDE_PADDING, SlideGen.VIEW_HEIGHT - self.SLIDE_PADDING)

                opt_r = sqrt(200 * size / pi)
                max_r = SlideGen.VIEW_HEIGHT/2
                R = triangular(opt_r, max_r, (opt_r + max_r) / 3)

                #set position                
                #cell_list[i].setPos( x_offset, y_offset)
                self.updatePos(cell_list[i], x_offset, y_offset)

            #plot point around the center
            else:
                r = uniform(0, R)
                x = uniform(-r, r)
                select = sample(pos_or_neg, 1)
                y = sqrt(r**2 - x**2)
                y = y * select[0]
                new_x = x_offset + x
                new_y = y_offset + y
                
                #check if cell is to be placed on screen
                if ((new_x > self.SLIDE_PADDING) and (new_x < SlideGen.VIEW_WIDTH - self.SLIDE_PADDING) and (new_y > self.SLIDE_PADDING) and (new_y < SlideGen.VIEW_HEIGHT - self.SLIDE_PADDING)):
                    #set position                    
                    #cell_list[i].setPos(new_x,new_y)
                    self.updatePos(cell_list[i], new_x, new_y)
                else:
                    try_again.append(i)
            
        for val in try_again:
            x_offset = uniform(self.SLIDE_PADDING, SlideGen.VIEW_WIDTH - self.SLIDE_PADDING) 
            y_offset = uniform(self.SLIDE_PADDING, SlideGen.VIEW_HEIGHT - self.SLIDE_PADDING)

            #set position            
            #cell_list[val].setPos(x_offset, y_offset)
            self.updatePos(cell_list[val], x_offset, y_offset)
        
        #hide the rest
        for i in range (this_count, self.CELL_MAX_COUNT):
            cell_list[i].setVisible(False)
            cell_list[i].setGraphicsEffect(None)
            
        self.cell_count = this_count
        self.updateSlide()

    def updatePos(self, cell, x, y):
        cell.setPos(x - (self.CELL_SCALE_SIZE / 2), y - (self.CELL_SCALE_SIZE / 2))
        
        
    def count(self):
        return self.cell_count
        
    def focusDown(self):
        self.changeFocus(-1)

    def focusUp(self):
        self.changeFocus(1)

    def wheelEvent(self, event):
        self.changeFocus(event.delta()/120.0)
        #print (event.delta()/120)
        #print self.current_focus
        
    def mousePressEvent(self, event):
        self.save_slide()

    #this is called when the slider is moved - value between 0 and 100
    def sliderFocus(self,value):
        # +3 for off by 1, /3 for 100/33 blur levels, *.2, -1 for -1-6 from 0-7
        self.current_focus = (((value+3)/3) * self.factor) - 1
        self.updateSlide()

    #this is called when scrolling or clicking the button - delta 1 or -1
    def changeFocus(self,delta):
        check = self.current_focus + (delta*self.factor)
        if(check > -1 and check < 6):
            self.current_focus = check
            # +1 so we use 0-7 range instead of -1-6, *15 to scale to 100
            self.trainer_ref.focus_slider.setSliderPosition((self.current_focus+1)*15)
            self.updateSlide()
