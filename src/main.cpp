#include "mainwindow.h"
//#include "ui_editor.h"
//#include "ui_trainer.h"
#include "editor.h"
#include "trainer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    //editor e;
    //trainer t;

    w.show();
//    w.close();
//    e.show();
//    t.show();

    return a.exec();

}
