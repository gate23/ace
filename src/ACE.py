from PyQt4 import QtCore, QtGui
from ACEUI import Ui_MainWindow


#NOTE: I couldn't get this to work using 'self'... dunno if using 'ui' like this
#is the best idea but hey neat it works
def trainerButtonClicked():
	ui.stackedWidget.setCurrentIndex(2)

def editorButtonClicked():
	ui.stackedWidget.setCurrentIndex(1)

def mainMenuClicked():
    ui.stackedWidget.setCurrentIndex(0)

def connectActions(ui):
	ui.pushButton.clicked.connect(editorButtonClicked)
	ui.pushButton_2.clicked.connect(trainerButtonClicked)
	ui.pushButton_3.clicked.connect(QtGui.qApp.quit)
	ui.actionMain_Menu.triggered.connect(mainMenuClicked)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    #connectactions events for UI
    ui.setupUi(MainWindow)    
    connectActions(ui) 
    MainWindow.setGeometry(QtCore.QRect(10, 10, 1024,728))
    MainWindow.show()
    sys.exit(app.exec_())