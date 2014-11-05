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
import time
import os.path

MAX_ESTIMATE = 9999

class Trainer(QtGui.QWidget):
    def __init__(self, parent, stats):
        self.estimate_number = 1
        
        super(Trainer,self).__init__(parent)
        
        self.initUI()
        self.parent = parent
        self.stats_ref = stats
        
        self.current_session = Session()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
                
        slide_layout = self.initSlideLayout()
        estimate_layout = self.initEstimateLayout()        
        layout.addLayout(slide_layout)
        layout.addLayout(estimate_layout)
        
        self.setLayout(layout)

        #stats per session to hand off to stats
        
        
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
  
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slide_display)
        layout.addLayout(zoom_layout)
        
        return layout
    
    def initEstimateLayout(self):
        #estimate_entry: input line for estimate
        self.estimate_entry = QtGui.QLineEdit()
        validator = QtGui.QIntValidator(0,MAX_ESTIMATE,self.estimate_entry)
        self.estimate_entry.setValidator(validator)
        
        #button to submit estimate
        button = QtGui.QPushButton("Estimate Algae Count")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.submitEstimate)
        #allow Enter press to submit estimate
        self.estimate_entry.connect(
                self.estimate_entry, QtCore.SIGNAL("returnPressed()"),
                button, QtCore.SIGNAL("pressed()")  )
        
        #estimate_display: shows list of previous estimates
        self.estimate_display = QtGui.QTextEdit()
        self.estimate_display.setReadOnly(1)

        #guess_label: shows which number guess user is making
        self.estimate_label = QtGui.QLabel("Slide " +  str(self.estimate_number) + "/10")      
        
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addWidget(self.estimate_label)
        estimate_layout.addWidget(self.estimate_display)
        estimate_layout.addWidget(button)
        estimate_layout.addWidget(self.estimate_entry)
        
        return estimate_layout
        
    def submitEstimate(self):
        if self.estimate_entry.text().length() > 0 :

            estimate = float(self.estimate_entry.text())
            actual = float(self.slide_display.count())
            
            
            raw_percent_err = (math.fabs(estimate - actual) / actual) * 100.0
            percent_err = "{:.1f}".format(raw_percent_err)

            self.estimate_display.append(
                    "Slide "+str(self.estimate_number)+
                    "\nEstimate: " + str(self.estimate_entry.text()) +
                    "\nActual Count: " + str(self.slide_display.count()) +
                    "\nPercentage Error: " + str(percent_err))
            self.estimate_entry.clear()
            
            #add estimate to list
            this_estimate = Estimate(estimate, actual)
            self.current_session.addEstimate(this_estimate)
            
            self.current_session.error_sum += raw_percent_err
            filename = "thum_"+str(int(round(time.time())))+"_"+str(self.estimate_number)+".png"
            imagePath = os.path.normpath("./session/"+filename)
            self.current_session.addImage(self.slide_display.save_image(imagePath, 100, 100))

            #update display            
            self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/10")
 
            if self.estimate_number < 10:
                self.slide_display.genSlide()
                self.estimate_number += 1
                           
            elif self.estimate_number == 10:
                self.stats_ref.recordSession(self.current_session)
                
                #display stats for 10-estimate session
                raw_session_error = self.current_session.error_sum / 10
                session_error ="{:.2f}".format(raw_session_error)
                
                self.estimate_display.append("\n10-slide session complete!")
                self.estimate_display.append("Average error for this session: " + 
                                                str(session_error) + "%\n")

                #MessageBox - restart trainer or return to menu
                self.endMessage = QtGui.QMessageBox.question(self,'Message',
                     "10 estimates complete! Try again?",
                     QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

                if self.endMessage == QtGui.QMessageBox.Yes:
                    self.startNewSession()
                elif self.endMessage == QtGui.QMessageBox.No:
                    self.startNewSession()
                    self.parent.changeMode(ModeEnum.MENU)

    #when session is complete, reset stuff
    def startNewSession(self):
        self.estimate_sum = 0
        self.actual_sum = 0
        
        self.estimate_number = 1
        self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/10")

        self.estimate_display.append("Beginning new session...")

        self.estimate_entry.clear()
        self.slide_display.genSlide()
        
        self.current_session = Session()