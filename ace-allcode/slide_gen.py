from PyQt4 import QtGui
from random import randint, uniform, triangular, sample, choice
from math import sqrt, pi
from sprites import SpriteType

class SlideGen(QtGui.QWidget):
    def __init__(self, parent, cellMin, cellMax):
        super(SlideGen, self).__init__(parent)
        self.cell_min_count = cellMin
        self.cell_max_count = cellMax

    
    def genSlide(self, slide_scene, num_cells = 0):
        slide_width = slide_scene.width()        
        slide_height = slide_scene.height()
        
        if(num_cells < self.cell_max_count and num_cells >= self.cell_min_count):
            this_count = num_cells
        else:
            rangenum = randint(3,10)
            low = 2**rangenum
            high = (2**(rangenum+1)) - 1
            this_count = int(triangular(low, high))
        
        #reset scene
        slide_scene.resetSlide()

        pos_or_neg = [1,-1]
        try_again = []

        if (this_count < 20):
            max_blobs = this_count
        else:
            max_blobs = 20

        num_blobs = int(triangular(1, max_blobs))
        shape_ends = sample(range(1, this_count-1), num_blobs-1)
        
        for i in range (this_count):
            #update cell depth, type, rotation
            depth = 2 + (randint(-16, 16) * 0.125) #range -1 to 4
            sprite_type = choice(SpriteType.APHANOTHECE_RENDER1)
            deg_rotation = uniform(0.0,359.9)

            #chooses the center point of the blob
            if ((i == 0) or (i in shape_ends)):
                if (i != 0):
                    shape_ends.remove(i)
                if (len(shape_ends) > 0):
                    next = min(shape_ends)
                    size = next - i
                else:
                    size = this_count - i
                
                x_offset = uniform(slide_scene.SLIDE_PADDING, slide_width - slide_scene.SLIDE_PADDING) 
                y_offset = uniform(slide_scene.SLIDE_PADDING, slide_height - slide_scene.SLIDE_PADDING)

                opt_r = sqrt(200 * size / pi)
                max_r = slide_scene.height()/2
                R = triangular(opt_r, max_r, (opt_r + max_r) / 3)

                #set position                
                slide_scene.placeCell(x_offset, y_offset, depth, deg_rotation, sprite_type)

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
                if ((new_x > slide_scene.SLIDE_PADDING) and 
                    (new_x < slide_width - slide_scene.SLIDE_PADDING) and 
                    (new_y > slide_scene.SLIDE_PADDING) and 
                    (new_y < slide_height - slide_scene.SLIDE_PADDING)):

                    #set position                    
                    slide_scene.placeCell(new_x, new_y, depth, deg_rotation, sprite_type)
                else:
                    try_again.append(i)
            
        for val in try_again:
            x_offset = uniform(slide_scene.SLIDE_PADDING, slide_width - slide_scene.SLIDE_PADDING) 
            y_offset = uniform(slide_scene.SLIDE_PADDING, slide_height - slide_scene.SLIDE_PADDING)

            #update cell depth, type, rotation
            depth = 2 + (randint(-16, 16) * 0.125) #range -1 to 4
            sprite_type = choice(SpriteType.APHANOTHECE_RENDER1)
            deg_rotation = uniform(0.0,359.9)
            
            slide_scene.placeCell(x_offset, y_offset, depth, deg_rotation, sprite_type)
        
        slide_scene.updateSlide()