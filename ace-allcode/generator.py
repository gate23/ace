"""
trainer.py

Trainer is the class representing the trainer mode (duh)
Makes use of SlideGen class for generating and viewing slides
"""

import math

from PyQt4 import QtGui, QtCore
from slidegen import SlideGen
from enum import ModeEnum
from session import Session,Estimate
from math import log
import time
import os.path

class Generator(QtGui.QWidget):
    def __init__(self, parent):
        
        super(Generator,self).__init__(parent)
        
        self.initUI()
        self.parent = parent
        self.num_cells = 8
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        slide_layout = self.initSlideLayout()      
        layout.addLayout(slide_layout)
        
        self.setLayout(layout)

        
        
    def initSlideLayout(self):
        self.slide_display = SlideGen(self)
        self.slide_display.genSlide(self, -1)
        self.slide_display.setMaximumSize(540,540)

        zoom_layout = QtGui.QHBoxLayout()

        focus_text = QtGui.QLabel("Focus: ")
        self.focus_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.focus_slider.setSliderPosition((self.slide_display.current_focus+1)*15)
        focus_plus_btn = QtGui.QPushButton("+")
        focus_minus_btn = QtGui.QPushButton("-")
        focus_plus_btn.setMaximumWidth(25)
        focus_minus_btn.setMaximumWidth(25)
        focus_plus_btn.connect(focus_plus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_display.focusUp)
        focus_minus_btn.connect(focus_minus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_display.focusDown)
        self.focus_slider.sliderMoved.connect(self.slide_display.sliderFocus)

        zoom_layout.addWidget(focus_text)
        zoom_layout.addWidget(focus_plus_btn)
        zoom_layout.addWidget(focus_minus_btn)
        zoom_layout.addWidget(self.focus_slider)
  
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slide_display)
        layout.addLayout(zoom_layout)
        
        return layout

    def genNewSlide(self):
        
        session_length_input = QtGui.QInputDialog(self)     
        
        self.num_cells, ok = QtGui.QInputDialog.getInt(self, 'Slide Generator', 
            'How many algae cells would you like to generate?',
            0, 1, 2048)

        if ok:
            self.slide_display.genSlide(self, self.num_cells)
            return True
        else:
            return False