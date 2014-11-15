
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
    MIN_COUNT = 2
    MAX_COUNT = 2048
    current_focus = 2.4
    factor = 0.2
    #sprite_list = [SpriteType.APHANOTHECE_OUTLINE, SpriteType.APHANOTHECE_OUTLINE2, SpriteType.APHANOTHECE_OUTLINE3]
    
    def __init__(self, parent):
        super(SlideGen, self).__init__(parent)
        self.initCells()
        self.trainer_ref = parent
        self.num_cells = 8
        

    
    def genSlide(self, parent, num_cells):
        self.num_cells = num_cells
        if(self.num_cells < 2048 and self.num_cells > 0):
            this_count = self.num_cells
        else:
            rangenum = randint(3,10)
            low = 2**rangenum
            high = (2**(rangenum+1)) - 1
            this_count = int(triangular(low, high))
        cell_list = self.scene.items()
        shuffle(cell_list)
        pos_or_neg = [1,-1]
        try_again = []

        if (this_count < 20):
            max_blobs = this_count
        else:
            max_blobs = 20
        num_blobs = int(triangular(1, max_blobs))
        shape_ends = sample(range(1, this_count-1), num_blobs-1)
        
        for i in range (0, this_count):
            #chooses the center point of the blob
            if ((i == 0) or (i in shape_ends)):
                if (i != 0):
                    shape_ends.remove(i)
                if (len(shape_ends) > 0):
                    next = min(shape_ends)
                    size = next - i
                else:
                    size = this_count - i
                x_offset = uniform(5.0, SlideGen.VIEW_WIDTH - 5) 
                y_offset = uniform(5.0, SlideGen.VIEW_HEIGHT - 5)
                opt_r = sqrt(200 * size / pi)
                max_r = SlideGen.VIEW_HEIGHT/2
                R = triangular(opt_r, max_r, (opt_r + max_r) / 3)
                cell_list[i].setPos( x_offset, y_offset)

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
                if ((new_x > 5) and (new_x < SlideGen.VIEW_WIDTH - 5) and (new_y > 5) and (new_y < SlideGen.VIEW_HEIGHT - 5)):
                    cell_list[i].setPos(new_x,new_y)
                else:
                    try_again.append(i)

            if i not in try_again:
                deg_rotation = uniform(0.0,359.9)
                depth = cell_list[i].zValue()
                #set sprite type
                sprite_type = random.choice(SpriteType.APHANOTHECE_RENDER1)
                
                texture, rotation, blur = self.get_texture(
                    sprite_type, depth, deg_rotation)

                cell_list[i].setPixmap(texture)
                cell_list[i].setRotation(rotation)
                cell_list[i].setVisible(True)
                cell_list[i].sprite_rotation = deg_rotation
                cell_list[i].sprite_code = sprite_type
            
        for val in try_again:
            x_offset = uniform(5.0, SlideGen.VIEW_WIDTH - 5) 
            y_offset = uniform(5.0, SlideGen.VIEW_HEIGHT - 5)
            cell_list[val].setPos(x_offset, y_offset)
            deg_rotation = uniform(0.0,359.9)
            depth = cell_list[val].zValue()
            #set sprite type
            sprite_type = random.choice(SpriteType.APHANOTHECE_RENDER1)
            
            texture, rotation, blur = self.get_texture(
                sprite_type, depth, deg_rotation)

            cell_list[val].setPixmap(texture)
            cell_list[val].setRotation(rotation)
            cell_list[val].setVisible(True)
            cell_list[val].sprite_rotation = deg_rotation
            cell_list[val].sprite_code = sprite_type
        
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
