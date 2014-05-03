#include "mainwindow.h"
//#include "ui_editor.h"
//#include "ui_trainer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.show();

    //editor e;
    //e.show();

    return a.exec();
}
