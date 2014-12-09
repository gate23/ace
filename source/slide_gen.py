"""
slide_gen.py

The Slide Generate populates QtGraphicScene with cell elements

"""

from PyQt4 import QtGui
from random import randint, uniform, triangular, sample, choice
from math import sqrt, pi
from sprites import SpriteType
import pickle
import zipfile
import os
from os import path
import time

class SlideGen(QtGui.QWidget):
    def __init__(self, parent, cellMin, cellMax):
        super(SlideGen, self).__init__(parent)
        self.cell_min_count = cellMin
        self.cell_max_count = cellMax
        
    def loadSlide(self, slide_scene):
        """open pickle file, builds slide"""

        file_fullpath = QtGui.QFileDialog.getOpenFileName(self,
                                                          "Load Slide",
                                                          str(path.join(path.curdir, 'slide', 'last.slz')), #default dir / filename
                                                          filter = "Slide (*.slz)")

        dir_name, file_name = path.split(str(file_fullpath))
        dir_name = path.normpath(dir_name)
        
        if(not file_name):
            return
        
        zf = zipfile.ZipFile(path.join(dir_name, file_name), 'r')
        slides = zf.namelist()
        
        for f in slides:
            try:
                data = zf.read(f)
            except:
                print "Error loading file"
            else:
                myslide = pickle.loads(data)
#        
#        #reset scene
        slide_scene.resetSlide()        
        for cell in myslide:
            #create cell
            slide_scene.placeCell(cell[0], cell[1], cell[2], cell[3], cell[4])
            
        slide_scene.updateSlide()
    
    def saveSlide(self, slide_scene, file_name = None):
        """Loops through all items and save data serialized pickle"""
        cell_list = []
        if (file_name is None):
            file_fullpath = QtGui.QFileDialog.getSaveFileName(self,
                                                     "Save File",
                                                     str(path.join(path.curdir, 'slide', 'last.slz')), #default dir / filename
                                                     filter = "Slide (*.slz)")
                                                     
        dir_name, file_name = path.split(str(file_fullpath))
        dir_name = path.normpath(dir_name)
        temp_file = str(int(round(time.time())))+'.sli'
        
        if (not file_name):
            return
                                                     
        for cell in slide_scene.items():
            if(cell.isVisible()):
                cell_list.append([cell.x() + (slide_scene.CELL_SCALE_SIZE / 2),
                                  cell.y() + (slide_scene.CELL_SCALE_SIZE / 2),
                                  cell.zValue(),
                                  cell.sprite_rotation,
                                  cell.sprite_type])

        with open(temp_file,'wb') as output:
            pickle.dump(cell_list, output)
            
        try:
            import zlib
            compression = zipfile.ZIP_DEFLATED
        except:
            compression = zipfile.ZIP_STORED
        
        with zipfile.ZipFile(path.join(dir_name, file_name), 'w') as slidezip:
            slidezip.write(temp_file, compress_type=compression)
        
        #remove temp
        os.remove(temp_file)
    
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

        if (this_count < 15):
            max_blobs = this_count
        else:
            max_blobs = 15

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

                #create cell
                slide_scene.placeCell(x_offset, y_offset, depth, deg_rotation, sprite_type)

            #plot point around the center
            else:
                r = triangular(0, R)
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

                    #create cell
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
            
            #create cell
            slide_scene.placeCell(x_offset, y_offset, depth, deg_rotation, sprite_type)
        
        slide_scene.updateSlide()
