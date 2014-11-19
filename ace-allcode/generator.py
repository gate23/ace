"""
generator.py

Generator is the class representing the slide generator
It provides a view of the slides being generated as well as a 
way to save a slide
"""

from PyQt4 import QtGui, QtCore
from slide_gen import SlideGen
from slide_scene import SlideScene
from random import triangular

class Generator(QtGui.QWidget):
    SLIDE_WIDTH,SLIDE_HEIGHT = 540,540
    
    def __init__(self, parent):
        super(Generator,self).__init__(parent)
        self.parent = parent
        self.num_cells = 8

        self.slide_gen = SlideGen(self, 2, 2048)
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        slide_layout = self.initSlideLayout()
        numCells_layout = self.initNumCellsLayout()       
        layout.addLayout(slide_layout)
        layout.addLayout(numCells_layout)
        
        self.setLayout(layout)
        
    def initSlideLayout(self):
        self.slide_scene = SlideScene(QtCore.QRectF(0,
                                                    0,
                                                    self.SLIDE_WIDTH,
                                                    self.SLIDE_HEIGHT), 
                                                    self) #generator is parent
                                          
        #build the view
        self.view = QtGui.QGraphicsView(self.slide_scene,
                                        self) #generator is parent

        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.view.setSizePolicy(QtGui.QSizePolicy.Fixed,
                                QtGui.QSizePolicy.Fixed)        

        focus_layout = QtGui.QHBoxLayout()

        #Controls
        focus_text = QtGui.QLabel("Focus: ")
        self.focus_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.focus_slider.setSliderPosition((self.slide_scene.current_focus+1)*15)
        
        focus_plus_btn = QtGui.QPushButton("+")
        focus_minus_btn = QtGui.QPushButton("-")
        focus_plus_btn.setMaximumWidth(25)
        focus_minus_btn.setMaximumWidth(25)

        #connect         
        focus_plus_btn.connect(focus_plus_btn, QtCore.SIGNAL("pressed()"),
                        self.focusUp)
        focus_minus_btn.connect(focus_minus_btn, QtCore.SIGNAL("pressed()"),
                        self.focusDown)
        
        self.focus_slider.valueChanged.connect(self.sliderFocus)

        #add controls
        focus_layout.addWidget(focus_text)
        focus_layout.addWidget(focus_plus_btn)
        focus_layout.addWidget(focus_minus_btn)
        focus_layout.addWidget(self.focus_slider)
  
        layout = QtGui.QVBoxLayout()
        
        layout.addWidget(self.view)
        layout.addLayout(focus_layout)
        
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
        
        self.exact_display = QtGui.QTextEdit('Exact Count: ' + str(0))
        self.exact_display.setReadOnly(True)
        
        num_cells_layout = QtGui.QVBoxLayout()
        num_cells_layout.addWidget(self.exact_display)
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
            self.num_cells = int(triangular(8,15))
        elif self.r1.isChecked():
            self.num_cells = int(triangular(16,31))
        elif self.r2.isChecked():
            self.num_cells = int(triangular(32,63))
        elif self.r3.isChecked():
            self.num_cells = int(triangular(64,127))
        elif self.r4.isChecked():
            self.num_cells = int(triangular(128,255))
        elif self.r5.isChecked():
            self.num_cells = int(triangular(256,511))
        elif self.r6.isChecked():
            self.num_cells = int(triangular(512,1023))
        elif self.r7.isChecked():
            self.num_cells = int(triangular(1024,2047))
        
        if (self.num_cells == 0):
            return False

        self.slide_gen.genSlide(self.slide_scene, self.num_cells)
        self.exact_display.append('Exact Count: ' + str(self.num_cells))

    def focusDown(self):
        self.slide_scene.changeFocus(-1)

    def focusUp(self):
        self.slide_scene.changeFocus(1)
        
    def sliderFocus(self,value):
        """Called when the slider is moved - value between 0 and 100"""
#        print "Slider val="+str(value)
        self.slide_scene.setFocus(((value/3) * self.slide_scene.SLIDE_FOCUS_STEP) - 1)
