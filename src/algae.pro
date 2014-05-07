#-------------------------------------------------
#
# Project created by QtCreator 2014-05-02T15:06:21
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = algae
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    editor.cpp \
    trainer.cpp

HEADERS  += mainwindow.h\
    editor.h \
    trainer.h

FORMS    += \
    editor.ui \
    trainer.ui \
    mainwindow.ui
