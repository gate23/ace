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
    LOW_POW2, HIGH_POW2 = 3,10 #defines upper and lower ranges
    
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
                        self.slide_scene.focusUp)
        focus_minus_btn.connect(focus_minus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_scene.focusDown)
        
        self.focus_slider.valueChanged.connect(self.slide_scene.sliderFocus)

        #add controls
        focus_layout.addWidget(focus_text)
        focus_layout.addWidget(focus_minus_btn)
        focus_layout.addWidget(focus_plus_btn)
        focus_layout.addWidget(self.focus_slider)
  
        layout = QtGui.QVBoxLayout()
        
        layout.addWidget(self.view)
        layout.addLayout(focus_layout)
        
        return layout

    def initNumCellsLayout(self):
        widget = QtGui.QWidget(self)
        self.guess_group = QtGui.QButtonGroup(widget)
        
        #create range selector buttons        
        for _range in range(Generator.LOW_POW2, Generator.HIGH_POW2+1):
            low = 2**_range
            high = 2*low -1
            btn_str = str(low)+"-"+str(high) 
            temp_btn = QtGui.QRadioButton(btn_str)
            
            #add the button as a member of the class so it persists
            member_name = "r"+str(_range)
            setattr(self, member_name, temp_btn);
            btn = getattr(self, member_name)
            self.guess_group.addButton( btn)
            self.guess_group.setId(btn, _range)
            
        loadsave_layout = QtGui.QHBoxLayout()
        
        
        buttonLoad = QtGui.QPushButton("Load Slide")
        buttonLoad.connect( buttonLoad, QtCore.SIGNAL("pressed()"),
                        self.loadSlide)

        buttonSave = QtGui.QPushButton("Save Slide")
        buttonSave.connect( buttonSave, QtCore.SIGNAL("pressed()"),
                        self.saveSlide)
                        
        loadsave_layout.addWidget(buttonSave)
        loadsave_layout.addWidget(buttonLoad)
        
        #button to submit estimate
        buttonGen = QtGui.QPushButton("Generate New Slide")
        buttonGen.connect( buttonGen, QtCore.SIGNAL("pressed()"),
                        self.genNewSlide)
        
        self.exact_display = QtGui.QTextEdit('Exact Count: ' + str(0))
        self.exact_display.setReadOnly(True)
        
        num_cells_layout = QtGui.QVBoxLayout()
        num_cells_layout.addLayout(loadsave_layout)
        num_cells_layout.addWidget(self.exact_display)
        buttons = self.guess_group.buttons()
        for btn in buttons:
            num_cells_layout.addWidget(btn)
        num_cells_layout.addWidget(buttonGen)
        
        return num_cells_layout
        
    def loadSlide(self):
        self.slide_gen.loadSlide(self.slide_scene)
        self.exact_display.append('Exact Count: ' + str(self.slide_scene.cell_count))
        
    def saveSlide(self):
        self.slide_gen.saveSlide(self.slide_scene)

    def genNewSlide(self):
        pow2_range = self.guess_group.checkedId()
        if (not pow2_range):
            return False
        
        low = 2**pow2_range
        high = 2*low -1
        self.num_cells = int( triangular(low,high))
        
        self.slide_gen.genSlide(self.slide_scene, self.num_cells)
        self.exact_display.append('Exact Count: ' + str(self.num_cells))