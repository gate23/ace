# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 23:05:52 2014

This is the sprite factory

@author: younga25
"""

from PyQt4 import QtGui, QtCore
from sets import Set
import math
import os

class Depth:
    TOP = "0"    
    NEAR = "1"
    CENTER = "2"
    FAR = "3"
    BACK = "4"
    
class CellType:
    APHANOTHECE_OUTLINE = "0"
    
    
class SpriteFactory:
    
    def __init__(self, directory):
        self.directory = directory
        self.sprite_paths = {}
        self.load()

    def load(self):
        for dirname, dirnames, filenames in os.walk( self.directory ):
            for filename in filenames:
                #fullpath = os.path.join(dirname, filename)
                #tokens = fullpath.split("/")
                #code = tokens[3]
                #depth = tokens[4]
                
                rotation = filename.split(".")[0][1:]
                #print dirname, filename, rotation
                if not rotation.isdigit():
                    break
                elif(self.sprite_paths.has_key(dirname)):
                    self.sprite_paths[dirname].add(int(rotation))
                else:
                    self.sprite_paths[dirname] = Set([int(rotation)])
                
                #rotation = tokens[5].split(".")[0]
               
                #pixmap = QtGui.QPixmap(fullpath)
                #scaled_size = QtCore.QSize(pixmap.width*self.scale, pixmap.height*self.scale)
                #self.scaled_sprites[fullpath] = pixmap.scaled(scaled_size,
                #                            QtCore.Qt.KeepAspectRatio, 
                #                            QtCore.Qt.SmoothTransformation)
                
                #print tokens[3], tokens[4], tokens[5].split(".")[0]

    """ 
    Get the sprite with the closest rotation and return the amount require to rotate
    """                
    def get_sprite(self, code, depth, rotation):
        dirname = self.directory+"t"+str(code)+"/d"+str(depth)
        filename = None
        diff = 360

        if dirname in self.sprite_paths:
            closest = -1
            #print str(rotation % 360)
            rotation_rounded = ((int)(math.floor(rotation)/15)*15)
            filename = "r"+str(rotation_rounded)+".png"
            
            for degree in self.sprite_paths[dirname]:
                if degree == 0 and rotation > 180:
                    degree = 360
                test = (rotation - degree)
                if math.fabs(test) <= math.fabs(diff):
                    diff = test
                    closest = degree
            #print dirname, filename, self.sprite_paths[dirname]
            filename = "r"+str(closest%360)+".png"
            
        #print "Closest", filename, diff
        return dirname+"/"+filename, diff

        
                
# testing
#sf = SpriteFactory("./img/sprites/")
#sf.get_texture(CellType.APHANOTHECE_OUTLINE, Depth.NEAR, 300.0)