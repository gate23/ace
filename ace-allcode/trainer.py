"""
trainer.py

Trainer is the class representing the trainer mode (duh)
Makes use of SlideGen class for generating and viewing slides
"""

import math
import pickle

from PyQt4 import QtGui, QtCore
from slidegen import SlideGen

MAX_ESTIMATE = 9999

class Trainer(QtGui.QWidget):
    def __init__(self, parent):
        super(Trainer,self).__init__(parent)
        
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
                
        slide_layout = self.initSlideLayout()
        estimate_layout = self.initEstimateLayout()        
        layout.addLayout(slide_layout)
        layout.addLayout(estimate_layout)
        
        self.setLayout(layout)

        #10-estimate session error/sum values to hand off to stats
        self.session_error = 0.0
        self.session_error_sum = 0.0
        
        #stats stuff
        try:
            file = open('stats.ace')
            opened = pickle.load(file)
            
            self.estimate_count = opened[0]
            self.error_sum = opened[1]
            
        except:
            self.estimate_count = 0
            self.error_sum = 0.0
            self.session_error_sum = 0.0
    
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
        self.estimate_number = 1
        self.estimate_label = QtGui.QLabel("Estimate " +  str(self.estimate_number) + "/10")      
        
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addWidget(self.estimate_label)
        estimate_layout.addWidget(self.estimate_display)
        estimate_layout.addWidget(button)
        estimate_layout.addWidget(self.estimate_entry)
        
        return estimate_layout
        
    def submitEstimate(self):
        if self.estimate_entry.text().length() > 0 :
            if self.estimate_number < 10:
                #Increment guess number and change text display
                self.estimate_number += 1
                self.estimate_label.setText("Estimate " +  str(self.estimate_number) + "/10")

                estimate = float(self.estimate_entry.text())
                actual = float(self.slide_display.count())
                     
                raw_percent_err = (math.fabs(estimate - actual) / actual) * 100.0

                self.estimate_count += 1
                self.error_sum += raw_percent_err
                self.session_error_sum += raw_percent_err
                #print "Total Average Err: " + str(self.error_sum/self.estimate_count)           
                
                #format for less precision
                percent_err = "{:.2f}".format(raw_percent_err)
                
                self.estimate_display.append(
                        "Estimate: " + str(self.estimate_entry.text()) +
                        " Actual Count: " + str(self.slide_display.count()) )
                self.estimate_entry.clear()
                
                self.slide_display.genSlide()
            
            #there's a better way to check for the 10th guess number
            if self.estimate_number == 10:
                self.endMessage = QtGui.QMessageBox()
                self.endMessage.setText("10/10 estimates complete!")
                self.endMessage.open()

                #stats for 10-estimate session
                self.session_error = self.session_error_sum/10

            #TODO: Make it so clicking msgBox button returns to main menu here?


    def dumpStats(self):
        stat_list = (self.estimate_count, self.error_sum)
        
        output = open('stats.ace','wb')
        pickle.dump(stat_list, output)
        
        output.close()