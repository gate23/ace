# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACE.ui'
#
# Created: Tue May 20 18:12:31 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1021, 721))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.MainPage = QtGui.QWidget()
        self.MainPage.setObjectName(_fromUtf8("MainPage"))
        self.verticalLayoutWidget = QtGui.QWidget(self.MainPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 110, 301, 391))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        #CLICK EVENT FO TRAINER
        self.pushButton_2.clicked.connect(self.trainerButtonClicked)

        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #CLICK EVENT FO TRAINER
        self.pushButton.clicked.connect(self.editorButtonClicked)



        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))


        #CLICK EVENT FO EXIT
        self.pushButton_3.clicked.connect(QtGui.qApp.quit)



        self.verticalLayout.addWidget(self.pushButton_3)
        self.stackedWidget.addWidget(self.MainPage)
        self.Trainer = QtGui.QWidget()
        self.Trainer.setObjectName(_fromUtf8("Trainer"))
        self.layoutWidget = QtGui.QWidget(self.Trainer)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 961, 621))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(100, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 617))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 61, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 61, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.algaeFrame = QtGui.QFrame(self.layoutWidget)
        self.algaeFrame.setMinimumSize(QtCore.QSize(700, 0))
        self.algaeFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.algaeFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.algaeFrame.setObjectName(_fromUtf8("algaeFrame"))
        self.label = QtGui.QLabel(self.algaeFrame)
        self.label.setGeometry(QtCore.QRect(230, 240, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_4 = QtGui.QPushButton(self.algaeFrame)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 580, 16, 16))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.algaeFrame)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 580, 16, 16))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_4 = QtGui.QLabel(self.algaeFrame)
        self.label_4.setGeometry(QtCore.QRect(605, 573, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.algaeFrame)
        self.label_5.setGeometry(QtCore.QRect(10, 550, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.algaeFrame)
        self.label_6.setGeometry(QtCore.QRect(505, 573, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_6 = QtGui.QPushButton(self.algaeFrame)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 580, 16, 16))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.algaeFrame)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 580, 16, 16))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_8 = QtGui.QLabel(self.algaeFrame)
        self.label_8.setGeometry(QtCore.QRect(10, 580, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.algaeFrame)
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 145, 617))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 60, 71, 21))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.Trainer)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.layoutWidget_2 = QtGui.QWidget(self.page)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 40, 951, 631))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.algaeFrame_2 = QtGui.QFrame(self.layoutWidget_2)
        self.algaeFrame_2.setMinimumSize(QtCore.QSize(700, 0))
        self.algaeFrame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.algaeFrame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.algaeFrame_2.setObjectName(_fromUtf8("algaeFrame_2"))
        self.label_10 = QtGui.QLabel(self.algaeFrame_2)
        self.label_10.setGeometry(QtCore.QRect(230, 240, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_9 = QtGui.QPushButton(self.algaeFrame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(650, 580, 16, 16))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.algaeFrame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 580, 16, 16))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_11 = QtGui.QLabel(self.algaeFrame_2)
        self.label_11.setGeometry(QtCore.QRect(605, 573, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.algaeFrame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 550, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.algaeFrame_2)
        self.label_13.setGeometry(QtCore.QRect(505, 573, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.pushButton_11 = QtGui.QPushButton(self.algaeFrame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 580, 16, 16))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.algaeFrame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(570, 580, 16, 16))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.label_14 = QtGui.QLabel(self.algaeFrame_2)
        self.label_14.setGeometry(QtCore.QRect(10, 580, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.algaeFrame_2)
        self.scrollArea_3 = QtGui.QScrollArea(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 241, 627))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 131, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_13 = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 60, 71, 21))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.textEdit_2 = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_2.setGeometry(QtCore.QRect(-1, 90, 241, 514))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.addWidget(self.scrollArea_3)
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionMain_Menu = QtGui.QAction(MainWindow)
        self.actionMain_Menu.setObjectName(_fromUtf8("actionMain_Menu"))

        #MAIN MENU CLICKZ
        self.actionMain_Menu.triggered.connect(self.mainMenuClicked)

        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        #CLOSE CLICKZ
        self.actionClose.triggered.connect(QtGui.qApp.quit)

        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionZoom_in = QtGui.QAction(MainWindow)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionLighting = QtGui.QAction(MainWindow)
        self.actionLighting.setObjectName(_fromUtf8("actionLighting"))
        self.actionFocus = QtGui.QAction(MainWindow)
        self.actionFocus.setObjectName(_fromUtf8("actionFocus"))
        self.actionFocus_2 = QtGui.QAction(MainWindow)
        self.actionFocus_2.setObjectName(_fromUtf8("actionFocus_2"))
        self.actionDraw_Shape = QtGui.QAction(MainWindow)
        self.actionDraw_Shape.setObjectName(_fromUtf8("actionDraw_Shape"))
        self.actionAdjust_Density = QtGui.QAction(MainWindow)
        self.actionAdjust_Density.setObjectName(_fromUtf8("actionAdjust_Density"))
        self.actionChange_Algae_Type = QtGui.QAction(MainWindow)
        self.actionChange_Algae_Type.setObjectName(_fromUtf8("actionChange_Algae_Type"))
        self.actionInstructions = QtGui.QAction(MainWindow)
        self.actionInstructions.setObjectName(_fromUtf8("actionInstructions"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMain_Menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionLighting)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFocus)
        self.menuView.addAction(self.actionFocus_2)
        self.menuTools.addAction(self.actionDraw_Shape)
        self.menuTools.addAction(self.actionAdjust_Density)
        self.menuTools.addAction(self.actionChange_Algae_Type)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ACE (Algae Count Estimator)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Trainer", None))
        self.pushButton.setText(_translate("MainWindow", "Editor", None))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.label_7.setText(_translate("MainWindow", "Tool List", None))
        self.label_9.setText(_translate("MainWindow", "Buttons!", None))
        self.label.setText(_translate("MainWindow", "[Super Realistic Algae Here]", None))
        self.pushButton_4.setText(_translate("MainWindow", "-", None))
        self.pushButton_5.setText(_translate("MainWindow", "+", None))
        self.label_4.setText(_translate("MainWindow", "Zoom", None))
        self.label_5.setText(_translate("MainWindow", "Stuff to put on status bar below  when we get coding:", None))
        self.label_6.setText(_translate("MainWindow", "Focus", None))
        self.pushButton_6.setText(_translate("MainWindow", "-", None))
        self.pushButton_7.setText(_translate("MainWindow", "+", None))
        self.label_8.setText(_translate("MainWindow", "Zoom level | Focus level | Algae Type", None))
        self.pushButton_8.setText(_translate("MainWindow", "Submit", None))
        self.label_2.setText(_translate("MainWindow", "Tool adjustments", None))
        self.label_3.setText(_translate("MainWindow", "Sliders and stuff!", None))
        self.label_10.setText(_translate("MainWindow", "[Super Realistic Algae Here]", None))
        self.pushButton_9.setText(_translate("MainWindow", "-", None))
        self.pushButton_10.setText(_translate("MainWindow", "+", None))
        self.label_11.setText(_translate("MainWindow", "Zoom", None))
        self.label_12.setText(_translate("MainWindow", "Stuff to put on status bar below  when we get coding:", None))
        self.label_13.setText(_translate("MainWindow", "Focus", None))
        self.pushButton_11.setText(_translate("MainWindow", "-", None))
        self.pushButton_12.setText(_translate("MainWindow", "+", None))
        self.label_14.setText(_translate("MainWindow", "Zoom level | Focus level | Algae Type", None))
        self.label_15.setText(_translate("MainWindow", "Algae Count Guess:", None))
        self.label_16.setText(_translate("MainWindow", "Slide 9 / 10", None))
        self.pushButton_13.setText(_translate("MainWindow", "Submit", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 8 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 174 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 235</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> -61 <span style=\" font-style:italic;\">(25.96% off) </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 7 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 <span style=\" font-style:italic;\">(1.68% off) </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 5 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) <br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 4 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 3 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 2 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 1 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>)</p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionMain_Menu.setText(_translate("MainWindow", "Main Menu", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionLighting.setText(_translate("MainWindow", "Lighting", None))
        self.actionFocus.setText(_translate("MainWindow", "Focus+", None))
        self.actionFocus_2.setText(_translate("MainWindow", "Focus-", None))
        self.actionDraw_Shape.setText(_translate("MainWindow", "Draw Shape", None))
        self.actionAdjust_Density.setText(_translate("MainWindow", "Adjust Density", None))
        self.actionChange_Algae_Type.setText(_translate("MainWindow", "Change Algae Type", None))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    #BUTTON CLICKZ

    def editorButtonClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def trainerButtonClicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def mainMenuClicked(self):
        self.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setGeometry(QtCore.QRect(10, 10, 1024,728))
    MainWindow.show()
    sys.exit(app.exec_())

