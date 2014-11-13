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

#MAX_ESTIMATE = 9999

class Trainer(QtGui.QWidget):
    def __init__(self, parent, stats):
        self.estimate_number = 1
        self.max_session_length = 100
        
        super(Trainer,self).__init__(parent)
        
        self.initUI()
        self.parent = parent
        self.stats_ref = stats
        
        self.has_active_session = False
        
        self.current_session = Session()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        slide_layout = self.initSlideLayout()
        estimate_layout = self.initEstimateLayout()        
        layout.addLayout(slide_layout)
        layout.addLayout(estimate_layout)
        
        self.setLayout(layout)

        
        
    def initSlideLayout(self):
        self.slide_display = SlideGen(self)
        self.slide_display.genSlide()
    
        zoom_layout = QtGui.QHBoxLayout()
        zoom_text = QtGui.QLabel("Magnification: <Current Zoom>")
        zoom_in_btn = QtGui.QPushButton("+")
        zoom_out_btn = QtGui.QPushButton("-")
        zoom_in_btn.setMaximumWidth(25)
        zoom_out_btn.setMaximumWidth(25)

        zoom_layout.addWidget(zoom_in_btn)
        zoom_layout.addWidget(zoom_out_btn)
        zoom_layout.addWidget(zoom_text)

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

    def initEstimateLayout(self):
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

        #validator = QtGui.QIntValidator(0,MAX_ESTIMATE,self.estimate_entry)
        #self.estimate_entry.setValidator(validator)
        
        #button to submit estimate
        button = QtGui.QPushButton("Estimate Algae Count")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.submitEstimate)
        #allow Enter press to submit estimate
        #self.estimate_entry.connect(
        #        self.estimate_entry, QtCore.SIGNAL("returnPressed()"),
        #        button, QtCore.SIGNAL("pressed()")  )
        
        #estimate_display: shows list of previous estimates
        self.estimate_display = QtGui.QTextEdit()
        self.estimate_display.setReadOnly(1)

        #guess_label: shows which number guess user is making
        self.estimate_label = QtGui.QLabel("Slide " +  str(self.estimate_number) + "/10")      
        
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addWidget(self.estimate_label)
        estimate_layout.addWidget(self.estimate_display)
        estimate_layout.addWidget(self.r0)
        estimate_layout.addWidget(self.r1)
        estimate_layout.addWidget(self.r2)
        estimate_layout.addWidget(self.r3)
        estimate_layout.addWidget(self.r4)
        estimate_layout.addWidget(self.r5)
        estimate_layout.addWidget(self.r6)
        estimate_layout.addWidget(self.r7)
        estimate_layout.addWidget(button)
        #estimate_layout.addWidget(self.estimate_entry)


        
        return estimate_layout
        
    def submitEstimate(self):
        estimate = 0
        
        if self.r0.isChecked():
            estimate = 8
        elif self.r1.isChecked():
            estimate = 16
        elif self.r2.isChecked():
            estimate = 32
        elif self.r3.isChecked():
            estimate = 64
        elif self.r4.isChecked():
            estimate = 128
        elif self.r5.isChecked():
            estimate = 256
        elif self.r6.isChecked():
            estimate = 512
        elif self.r7.isChecked():
            estimate = 1024
        
        if (estimate == 0):
            return False
            
        estimate_range = str(estimate) + '-' + str(estimate * 2 - 1)

        actual = self.slide_display.count()

        log_estimate = int(log(estimate, 2))
        log_actual = int(log(actual,2))

        low = 2**int(log(actual,2))
        actual_range = str(low) + '-' + str(low * 2 - 1)
        
        log_error = log_estimate - log_actual

        if log_error == 0:
            status = " - Correct!"
        else:
            status = " - Incorrect"

        self.estimate_display.append(
                "Slide " + str(self.estimate_number) + status +
                "\nEstimate: " + estimate_range +
                "\nActual Range: " + actual_range +
                "\nExact Count: " + str(actual) +
                "\nLog Error: " + str(log_error) + "\n")

        #add estimate to list
        this_estimate = Estimate(estimate, actual)
        self.current_session.addEstimate(this_estimate)

        
        self.current_session.error_sum += log_error
        self.current_session.total_estimates += 1
        bias = 7
        self.current_session.log_err_list[log_error+bias] += 1
        filename = "thum_"+str(int(round(time.time())))+"_"+str(self.estimate_number)+".png"
        imagePath = os.path.normpath("./session/"+filename)
        self.current_session.addImage(self.slide_display.save_image(imagePath, 100, 100))

        #update display            
        self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/" + str(self.num_slides))
        if (self.estimate_number < self.num_slides):
            self.slide_display.genSlide()
            self.estimate_number += 1
                       
        elif (self.estimate_number == self.num_slides):
            self.stats_ref.recordSession(self.current_session)
            
            #display stats for 10-estimate session
            session_error = self.current_session.error_sum / self.num_slides
            
            self.estimate_display.append("\nSession complete!")
            self.estimate_display.append("Average log error for this session: " + 
                                            str(session_error) + "\n")

            #MessageBox - restart trainer or return to menu
            self.endMessage = QtGui.QMessageBox.question(self,'Message',
                 "10 estimates complete! Try again?",
                 QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

            if self.endMessage == QtGui.QMessageBox.Yes:
                self.startNewSession()
            elif self.endMessage == QtGui.QMessageBox.No:
                self.has_active_session = False
                self.parent.changeMode(ModeEnum.MENU)

    #when session is complete, reset stuff
    #TODO: THIS IS SLOPPY. This gets called in main window, repeating some actions
    def startNewSession(self):
        self.estimate_sum = 0
        self.actual_sum = 0
        self.estimate_number = 1
        
        session_length_input = QtGui.QInputDialog(self)     
        
        self.num_slides, ok = QtGui.QInputDialog.getInt(self, 'Trainer', 
            'How many algae slides would you like to generate?',
            10, 1, self.max_session_length)

        if ok:
            self.has_active_session = True
            self.num_slides = self.num_slides
            self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/" +
                str(self.num_slides))
            

            self.estimate_display.append("Beginning new session...")

            self.slide_display.genSlide()
            
            self.current_session = Session()
            return True
        else:
            self.has_active_session =False
            return False
