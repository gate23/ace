"""
MainWindow
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QTransform
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QBrush

from PyQt4 import QtCore

from random import randint, uniform

WIN_WIDTH, WIN_HEIGHT = 800,800
VIEW_WIDTH,VIEW_HEIGHT = 700, 689
WIN_X, WIN_Y = 10,10

scale_size = 15

class SlideGen(QtGui.QWidget):
	MIN_COUNT = 500
	MAX_COUNT = 5000
	
	def __init__(self):
		#Scene:	Contains the items to be drawn
		#
		#Initialize scene:	first two numbers set origin for added items,
		#					second sets size of the view
		self.scene = QtGui.QGraphicsScene(QtCore.QRectF(0,0,VIEW_WIDTH,VIEW_HEIGHT))
		
		#View:	Contains the scene. Is the actual graphics widget to be included
		#
		#Inititialize view:			
		self.view = QtGui.QGraphicsView(self.scene, self)
		self.view.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.SmoothPixmapTransform)
		
		#set background of the view
		self.bg_texture = QtGui.QPixmap('background.jpg')
		background = QBrush(self.bg_texture)
		self.scene.setBackgroundBrush(background)
		
		#load and scale the texture for the algae cells
		self.texture = QtGui.QPixmap('apathano1.png')
		self.texture = self.texture.scaled( QtCore.QSize(scale_size,scale_size) )
		
		self.setLayout(self.hbox)

		self.cell_count = 0

		self.gen_colony()
		
		#not sure if this is necessary at this point	
		#self.show()
	
	def gen_colony(self):
		this_count = randint(MainWindow.MIN_COUNT, MainWindow.MAX_COUNT)
		
		self.scene.clear()
		
		for i in range (0, this_count-1):
			cell = QtGui.QGraphicsPixmapItem(self.texture)
			#cell.setScale(0.7)

			x_offset = uniform(0.0,VIEW_WIDTH) 
			y_offset = uniform(0.0,VIEW_HEIGHT)
			
			cell.setPos( x_offset, y_offset)

			deg_rotation = uniform(0.0,359.9)
			cell.setRotation( deg_rotation)
			
			self.scene.addItem(cell)	
			
		#self.cell_list.append(cell)
		self.cell_count = this_count

			
			
			
			
		
		
		
