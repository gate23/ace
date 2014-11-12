from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
  
class HistogramView(QListView):  
    def __init__(self,parent):  
        super(HistogramView,self).__init__()  
        self.listRegionM = []  
        self.listRegionF = []  
        self.listRegionS = []  
        self.region = QRegion()  
      
    def paintEvent(self,QPaintEvent):  
        painter = QPainter(self.viewport())  
        painter.setPen(Qt.black)  

	#the left/bottom coordinates of the histogram
        x0 = 40  
        y0 = 250  

	#y-axis
        painter.drawLine(x0,y0,40,30)
	#arror at end of axis  
        painter.drawLine(38,32,40,30)  
        painter.drawLine(40,30,42,32)
	#y-axis label  
        painter.drawText(30,20,"num")  
          
	#x-axis
        painter.drawLine(x0,y0,260,250)
	#arror at end of x-axis  
        painter.drawLine(258,248,260,250)  
        painter.drawLine(260,250,258,252)
	#x-axis label  
        painter.drawText(270,250,"department")  
          
	#label each part of histogram from first col of table
        posD = x0 + 20  
        for row in xrange(self.model().rowCount(self.rootIndex())):  
            index = self.model().index(row,0,self.rootIndex())  
            dep = self.model().data(index).toString()  
              
            painter.drawText(posD,y0+20,dep)  
            posD += 50  
        
	#draw the rectangles for the first col  
        posM = x0 + 20  
        for row in xrange(self.model().rowCount(self.rootIndex())):  
            index = self.model().index(row,1,self.rootIndex())  
            male = self.model().data(index).toDouble()[0]  
              
            width = 10  
            if self.selections.isSelected(index):  
                painter.setBrush(QBrush(Qt.blue,Qt.Dense3Pattern))  
            else:  
                painter.setBrush(Qt.blue)  
            painter.drawRect(QRect(posM,y0 - male * 10,width,male * 10))  
            regionM = QRegion(posM,y0 - male *10 ,width,male * 10)  
            self.listRegionM.append(regionM)  
            posM += 50  

	#draw the rectangles for the second col
        posF = x0 + 30  
        for row in xrange(self.model().rowCount(self.rootIndex())):  
            index = self.model().index(row,2,self.rootIndex())  
            female = self.model().data(index).toDouble()[0]  
            width = 10  
            if self.selections.isSelected(index):  
                painter.setBrush(QBrush(Qt.red,Qt.Dense3Pattern))  
            else:  
                painter.setBrush(Qt.red)  
            painter.drawRect(QRect(posF,y0 - female * 10,width,female * 10))  
            regionF = QRegion(posF,y0 - female *10 ,width,female * 10)  
            self.listRegionF.append(regionF)  
            posF += 50  

	#draw the rectangles for the third col
        posS = x0 + 40  
        for row in xrange(self.model().rowCount(self.rootIndex())):  
            index = self.model().index(row,3,self.rootIndex())  
            sum = self.model().data(index).toDouble()[0]  
            width = 10  
            if self.selections.isSelected(index):  
                painter.setBrush(QBrush(Qt.green,Qt.Dense3Pattern))  
            else:  
                painter.setBrush(Qt.green)  
            painter.drawRect(QRect(posS,y0 - sum * 10,width,sum * 10))  
            regionS = QRegion(posS,y0 - sum *10 ,width,sum * 10)  
            self.listRegionS.append(regionS)  
            posS += 50  
          
    def datachanged(self,topLeft,bottomRight):  
        QAbstractItemView.dataChanged(topLeft,bottomRight)  
        self.viewport().update()  
      
    def setSelectionModel(self,sectionModel):  
        self.selections = sectionModel  
          
    def selectionChanged(self,selected,deselected):  
        self.viewport().update()  
      
    def setSelection(self,rect,flags):  
        rows = self.model().rowCount(self.rootIndex())  
        columns = self.model().columnCount(self.rootIndex())  
        selectedIndex = QModelIndex()  
        for row in xrange(rows):  
            for column in xrange(1,columns):  
                index = self.model().index(row,column,self.rootIndex())  
                self.region = self.itemRegion(index)  
                if not region.intersected(contentsRect).isEmpty():  
                    selectedIndex = index  
        if selectedIndex.isValid():  
            self.selections.select(selectedindex,flags)  
        else:  
            noIndex = QModelIndex()  
            self.selections.select(noIndex,flags)   
      
    def itemRegion(self,index):  
        if index.column() == 1:  
            self.region = self.listRegionM(index.row())  
        if index.column() == 2:  
            self.region = self.listRegionF(index.row())  
        if index.column() == 3:  
            self.region = self.listRegionS(index.row())  
        return self.region  
      
    def indexAt(self,point):  
        newPoint = QPoint(point.x(),point.y())  
        region = QRegion()  
        for region in self.listRegionM:  
            if region.contains(newPoint):  
                row = self.listRegionM.indexOf(region)  
                index = self.model().index(row,1,self.rootIndex())  
                return index  
        for region in self.listRegionF:  
            if region.contains(newPoint):  
                row = self.listRegionF.indexOf(region)  
                index = self.model().index(row,1,self.rootIndex())  
                return index  
        for region in self.listRegionS:  
            if region.contains(newPoint):  
                row = self.listRegionS.indexOf(region)  
                index = self.model().index(row,1,self.rootIndex())  
                return index  
        return QModelIndex() 
 
class MainWindow(QMainWindow):  
    def __init__(self,parent=None):  
        super(MainWindow,self).__init__()  
        self.name = QString()  
        self.strList = QStringList()  
        self.splitter = QSplitter(Qt.Horizontal)    
        
        self.setupModel()  
        self.setupView()  
  
    def setupModel(self):  
        self.model = QStandardItemModel(4,4,self)  
        self.model.setHeaderData(0,Qt.Horizontal,"department")  
        self.model.setHeaderData(1,Qt.Horizontal,"male")  
        self.model.setHeaderData(2,Qt.Horizontal,"female")  
        self.model.setHeaderData(3,Qt.Horizontal,"retrie")  
      
    def setupView(self):  
        table = QTableView()  
        histogram = HistogramView(self.splitter, stats)  
          
        table.setModel(self.model)  
        self.setCentralWidget(table)  
        histogram.setModel(self.model)  
        self.dockWidget = QDockWidget()  
        self.dockWidget.setWidget(histogram)  
        self.addDockWidget(Qt.BottomDockWidgetArea,self.dockWidget)     
          
        selectionModel = QItemSelectionModel(self.model)  
        table.setSelectionModel(selectionModel)  
        histogram.setSelectionModel(selectionModel)  
          
        histogram.connect(selectionModel,SIGNAL("selectionChanged(QItemSelection,QItemSelection)"),histogram.selectionChanged)  
        table.connect(selectionModel,SIGNAL("selectionChanged(QItemSelection,QItemSelection)"),histogram.selectionChanged)  
      
app=QApplication(sys.argv)  
window=MainWindow()  
window.show()  
app.exec_()  
