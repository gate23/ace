#include "editor.h"
#include "ui_editor.h"

editor::editor(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::editor)
{
    ui->setupUi(this);

    connect(ui->actionMain_Menu,SIGNAL(clicked())),this,SLOT(actionMain_MenuClicked());
}

editor::~editor()
{
    delete ui;
}

void editor::actionMain_MeduClicked()
{
    mw.show();
    this->hide;
}
