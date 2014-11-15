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
        numCells_layout = self.initNumCellsLayout()       
        layout.addLayout(slide_layout)
        layout.addLayout(numCells_layout)
        
        self.setLayout(layout)
        
    def initSlideLayout(self):
        self.slide_display = SlideGen(self)
        self.slide_display.genSlide(self, -1)
        self.slide_display.setMinimumSize(540,540)

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

    def initNumCellsLayout(self):
        widget = QtGui.QWidget(self)
        self.guess_group = QtGui.QButtonGroup(widget)
        self.r0 = QtGui.QRadioButton("8-15")
        self.guess_group.addButton(self.r0)
        self.r1 = QtGui.QRadioButton("16-31")
        self.guess_group.addButton(self.r1)
        self.r2 = QtGui.QRadioButton("32-63")
        self.guess_group.addButton(self.r2)
        self.r3 = QtGui.QRadioButton("64-127")
        self.guess_group.addButton(self.r3)
        self.r4 = QtGui.QRadioButton("128-255")
        self.guess_group.addButton(self.r4)
        self.r5 = QtGui.QRadioButton("256-511")
        self.guess_group.addButton(self.r5)
        self.r6 = QtGui.QRadioButton("512-1023")
        self.guess_group.addButton(self.r6)
        self.r7 = QtGui.QRadioButton("1024-2047")
        self.guess_group.addButton(self.r7)
        
        #button to submit estimate
        button = QtGui.QPushButton("Generate New Slide")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.genNewSlide)
        #allow Enter press to submit estimate
        #button.connect(
        #        button, QtCore.SIGNAL("returnPressed()"),
        #        button, QtCore.SIGNAL("pressed()")  )
        
        #estimate_display: shows list of previous estimates
        self.display = QtGui.QTextEdit()
        self.display.setReadOnly(1)    
        
        num_cells_layout = QtGui.QVBoxLayout()
        num_cells_layout.addWidget(self.display)
        num_cells_layout.addWidget(self.r0)
        num_cells_layout.addWidget(self.r1)
        num_cells_layout.addWidget(self.r2)
        num_cells_layout.addWidget(self.r3)
        num_cells_layout.addWidget(self.r4)
        num_cells_layout.addWidget(self.r5)
        num_cells_layout.addWidget(self.r6)
        num_cells_layout.addWidget(self.r7)
        num_cells_layout.addWidget(button)


        
        return num_cells_layout

    def genNewSlide(self):

        self.num_cells = 0
        
        if self.r0.isChecked():
            self.num_cells = 8
        elif self.r1.isChecked():
            self.num_cells = 16
        elif self.r2.isChecked():
            self.num_cells = 32
        elif self.r3.isChecked():
            self.num_cells = 64
        elif self.r4.isChecked():
            self.num_cells = 128
        elif self.r5.isChecked():
            self.num_cells = 256
        elif self.r6.isChecked():
            self.num_cells = 512
        elif self.r7.isChecked():
            self.num_cells = 1024
        
        if (self.num_cells == 0):
            return False

        self.slide_display.genSlide(self, self.num_cells)