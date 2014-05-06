/********************************************************************************
** Form generated from reading UI file 'editor.ui'
**
** Created: Tue May 6 15:48:43 2014
**      by: Qt User Interface Compiler version 4.8.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef EDITOR_H
#define EDITOR_H

#include <QtCore/QVariant>
#include <QAction>
#include <QApplication>
#include <QButtonGroup>
#include <QFrame>
#include <QHBoxLayout>
#include <QHeaderView>
#include <QLabel>
#include <QMainWindow>
#include <QMenu>
#include <QMenuBar>
#include <QPushButton>
#include <QScrollArea>
#include <QStatusBar>
#include <QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionNew;
    QAction *actionOpen;
    QAction *actionSave;
    QAction *actionInsructions;
    QAction *actionAbout;
    QAction *actionZoom;
    QAction *actionZoom_Out;
    QAction *actionPolarized;
    QAction *actionPhase_Contrast;
    QAction *actionDIC;
    QAction *actionMain_Menu;
    QAction *actionClose;
    QAction *actionFocus;
    QAction *actionFocus_2;
    QAction *actionAdjust_Density;
    QAction *actionDraw_Shape;
    QAction *actionUndo;
    QAction *actionRedo;
    QAction *actionChange_Algae_Type;
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout_3;
    QHBoxLayout *horizontalLayout_2;
    QScrollArea *scrollArea_2;
    QWidget *scrollAreaWidgetContents_2;
    QLabel *label_7;
    QLabel *label_9;
    QFrame *algaeFrame;
    QLabel *label;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QLabel *label_8;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QPushButton *pushButton;
    QLabel *label_2;
    QLabel *label_3;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuView;
    QMenu *menuLighting;
    QMenu *menuHelp;
    QMenu *menuTools;
    QMenu *menuEdit;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(971, 670);
        MainWindow->setTabShape(QTabWidget::Rounded);
        MainWindow->setDockNestingEnabled(false);
        actionNew = new QAction(MainWindow);
        actionNew->setObjectName(QString::fromUtf8("actionNew"));
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QString::fromUtf8("actionOpen"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        actionInsructions = new QAction(MainWindow);
        actionInsructions->setObjectName(QString::fromUtf8("actionInsructions"));
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionZoom = new QAction(MainWindow);
        actionZoom->setObjectName(QString::fromUtf8("actionZoom"));
        actionZoom_Out = new QAction(MainWindow);
        actionZoom_Out->setObjectName(QString::fromUtf8("actionZoom_Out"));
        actionPolarized = new QAction(MainWindow);
        actionPolarized->setObjectName(QString::fromUtf8("actionPolarized"));
        actionPhase_Contrast = new QAction(MainWindow);
        actionPhase_Contrast->setObjectName(QString::fromUtf8("actionPhase_Contrast"));
        actionDIC = new QAction(MainWindow);
        actionDIC->setObjectName(QString::fromUtf8("actionDIC"));
        actionMain_Menu = new QAction(MainWindow);
        actionMain_Menu->setObjectName(QString::fromUtf8("actionMain_Menu"));
        actionClose = new QAction(MainWindow);
        actionClose->setObjectName(QString::fromUtf8("actionClose"));
        actionFocus = new QAction(MainWindow);
        actionFocus->setObjectName(QString::fromUtf8("actionFocus"));
        actionFocus_2 = new QAction(MainWindow);
        actionFocus_2->setObjectName(QString::fromUtf8("actionFocus_2"));
        actionAdjust_Density = new QAction(MainWindow);
        actionAdjust_Density->setObjectName(QString::fromUtf8("actionAdjust_Density"));
        actionDraw_Shape = new QAction(MainWindow);
        actionDraw_Shape->setObjectName(QString::fromUtf8("actionDraw_Shape"));
        actionUndo = new QAction(MainWindow);
        actionUndo->setObjectName(QString::fromUtf8("actionUndo"));
        actionRedo = new QAction(MainWindow);
        actionRedo->setObjectName(QString::fromUtf8("actionRedo"));
        actionChange_Algae_Type = new QAction(MainWindow);
        actionChange_Algae_Type->setObjectName(QString::fromUtf8("actionChange_Algae_Type"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout_3 = new QHBoxLayout(centralwidget);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        scrollArea_2 = new QScrollArea(centralwidget);
        scrollArea_2->setObjectName(QString::fromUtf8("scrollArea_2"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(scrollArea_2->sizePolicy().hasHeightForWidth());
        scrollArea_2->setSizePolicy(sizePolicy);
        scrollArea_2->setMinimumSize(QSize(100, 0));
        scrollArea_2->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 98, 601));
        label_7 = new QLabel(scrollAreaWidgetContents_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(20, 30, 61, 17));
        label_9 = new QLabel(scrollAreaWidgetContents_2);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(20, 170, 61, 17));
        scrollArea_2->setWidget(scrollAreaWidgetContents_2);

        horizontalLayout_2->addWidget(scrollArea_2);

        algaeFrame = new QFrame(centralwidget);
        algaeFrame->setObjectName(QString::fromUtf8("algaeFrame"));
        algaeFrame->setMinimumSize(QSize(700, 0));
        algaeFrame->setFrameShape(QFrame::StyledPanel);
        algaeFrame->setFrameShadow(QFrame::Raised);
        label = new QLabel(algaeFrame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(230, 240, 271, 81));
        QFont font;
        font.setPointSize(16);
        label->setFont(font);
        pushButton_2 = new QPushButton(algaeFrame);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(650, 580, 16, 16));
        pushButton_3 = new QPushButton(algaeFrame);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(670, 580, 16, 16));
        label_4 = new QLabel(algaeFrame);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(605, 573, 51, 31));
        QFont font1;
        font1.setPointSize(10);
        label_4->setFont(font1);
        label_5 = new QLabel(algaeFrame);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(10, 550, 331, 21));
        label_5->setFont(font1);
        label_6 = new QLabel(algaeFrame);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(505, 573, 51, 31));
        label_6->setFont(font1);
        pushButton_4 = new QPushButton(algaeFrame);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        pushButton_4->setGeometry(QRect(550, 580, 16, 16));
        pushButton_5 = new QPushButton(algaeFrame);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setGeometry(QRect(570, 580, 16, 16));
        label_8 = new QLabel(algaeFrame);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(10, 580, 321, 21));
        label_8->setFont(font1);
        label->raise();
        pushButton_2->raise();
        pushButton_3->raise();
        label_4->raise();
        label_5->raise();
        label_6->raise();
        pushButton_4->raise();
        pushButton_5->raise();
        label_8->raise();
        scrollArea_2->raise();

        horizontalLayout_2->addWidget(algaeFrame);

        scrollArea = new QScrollArea(centralwidget);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(scrollArea->sizePolicy().hasHeightForWidth());
        scrollArea->setSizePolicy(sizePolicy1);
        scrollArea->setMaximumSize(QSize(16777215, 16777215));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 137, 601));
        pushButton = new QPushButton(scrollAreaWidgetContents);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(150, 60, 71, 21));
        label_2 = new QLabel(scrollAreaWidgetContents);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(10, 30, 121, 17));
        label_3 = new QLabel(scrollAreaWidgetContents);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 170, 121, 17));
        scrollArea->setWidget(scrollAreaWidgetContents);
        pushButton->raise();
        algaeFrame->raise();
        algaeFrame->raise();
        algaeFrame->raise();
        label_2->raise();
        label_3->raise();

        horizontalLayout_2->addWidget(scrollArea);


        horizontalLayout_3->addLayout(horizontalLayout_2);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 971, 25));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuView = new QMenu(menubar);
        menuView->setObjectName(QString::fromUtf8("menuView"));
        menuLighting = new QMenu(menuView);
        menuLighting->setObjectName(QString::fromUtf8("menuLighting"));
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        menuTools = new QMenu(menubar);
        menuTools->setObjectName(QString::fromUtf8("menuTools"));
        menuEdit = new QMenu(menubar);
        menuEdit->setObjectName(QString::fromUtf8("menuEdit"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuEdit->menuAction());
        menubar->addAction(menuView->menuAction());
        menubar->addAction(menuTools->menuAction());
        menubar->addAction(menuHelp->menuAction());
        menuFile->addAction(actionNew);
        menuFile->addAction(actionSave);
        menuFile->addAction(actionOpen);
        menuFile->addSeparator();
        menuFile->addAction(actionMain_Menu);
        menuFile->addAction(actionClose);
        menuView->addAction(actionZoom);
        menuView->addAction(actionZoom_Out);
        menuView->addSeparator();
        menuView->addAction(menuLighting->menuAction());
        menuView->addSeparator();
        menuView->addAction(actionFocus);
        menuView->addAction(actionFocus_2);
        menuLighting->addAction(actionPolarized);
        menuLighting->addAction(actionPhase_Contrast);
        menuLighting->addAction(actionDIC);
        menuHelp->addAction(actionInsructions);
        menuHelp->addSeparator();
        menuHelp->addAction(actionAbout);
        menuTools->addAction(actionDraw_Shape);
        menuTools->addAction(actionAdjust_Density);
        menuTools->addAction(actionChange_Algae_Type);
        menuEdit->addAction(actionUndo);
        menuEdit->addAction(actionRedo);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Edit", 0, QApplication::UnicodeUTF8));
        actionNew->setText(QApplication::translate("MainWindow", "New...", 0, QApplication::UnicodeUTF8));
        actionOpen->setText(QApplication::translate("MainWindow", "Open", 0, QApplication::UnicodeUTF8));
        actionSave->setText(QApplication::translate("MainWindow", "Save", 0, QApplication::UnicodeUTF8));
        actionInsructions->setText(QApplication::translate("MainWindow", "Instructions", 0, QApplication::UnicodeUTF8));
        actionAbout->setText(QApplication::translate("MainWindow", "About", 0, QApplication::UnicodeUTF8));
        actionZoom->setText(QApplication::translate("MainWindow", "Zoom In", 0, QApplication::UnicodeUTF8));
        actionZoom_Out->setText(QApplication::translate("MainWindow", "Zoom Out", 0, QApplication::UnicodeUTF8));
        actionPolarized->setText(QApplication::translate("MainWindow", "Bright Field", 0, QApplication::UnicodeUTF8));
        actionPhase_Contrast->setText(QApplication::translate("MainWindow", "Phase Contrast", 0, QApplication::UnicodeUTF8));
        actionDIC->setText(QApplication::translate("MainWindow", "DIC", 0, QApplication::UnicodeUTF8));
        actionMain_Menu->setText(QApplication::translate("MainWindow", "Main Menu", 0, QApplication::UnicodeUTF8));
        actionClose->setText(QApplication::translate("MainWindow", "Close", 0, QApplication::UnicodeUTF8));
        actionFocus->setText(QApplication::translate("MainWindow", "Focus +", 0, QApplication::UnicodeUTF8));
        actionFocus_2->setText(QApplication::translate("MainWindow", "Focus -", 0, QApplication::UnicodeUTF8));
        actionAdjust_Density->setText(QApplication::translate("MainWindow", "Adjust Density", 0, QApplication::UnicodeUTF8));
        actionDraw_Shape->setText(QApplication::translate("MainWindow", "Draw Shape", 0, QApplication::UnicodeUTF8));
        actionUndo->setText(QApplication::translate("MainWindow", "Undo", 0, QApplication::UnicodeUTF8));
        actionRedo->setText(QApplication::translate("MainWindow", "Redo", 0, QApplication::UnicodeUTF8));
        actionChange_Algae_Type->setText(QApplication::translate("MainWindow", "Change Algae Type", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("MainWindow", "Tool List", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindow", "Buttons!", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "[Super Realistic Algae Here]", 0, QApplication::UnicodeUTF8));
        pushButton_2->setText(QApplication::translate("MainWindow", "-", 0, QApplication::UnicodeUTF8));
        pushButton_3->setText(QApplication::translate("MainWindow", "+", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "Zoom", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "Stuff to put on status bar below  when we get coding:", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindow", "Focus", 0, QApplication::UnicodeUTF8));
        pushButton_4->setText(QApplication::translate("MainWindow", "-", 0, QApplication::UnicodeUTF8));
        pushButton_5->setText(QApplication::translate("MainWindow", "+", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("MainWindow", "Zoom level | Focus level | Algae Type", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("MainWindow", "Submit", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Tool adjustments", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "Sliders and stuff!", 0, QApplication::UnicodeUTF8));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", 0, QApplication::UnicodeUTF8));
        menuView->setTitle(QApplication::translate("MainWindow", "View", 0, QApplication::UnicodeUTF8));
        menuLighting->setTitle(QApplication::translate("MainWindow", "Lighting", 0, QApplication::UnicodeUTF8));
        menuHelp->setTitle(QApplication::translate("MainWindow", "Help", 0, QApplication::UnicodeUTF8));
        menuTools->setTitle(QApplication::translate("MainWindow", "Tools", 0, QApplication::UnicodeUTF8));
        menuEdit->setTitle(QApplication::translate("MainWindow", "Edit", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // EDITOR_H
