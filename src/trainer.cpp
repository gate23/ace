#include "trainer.h"
#include "ui_trainer.h"

trainer::trainer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::trainer)
{
    ui->setupUi(this);

    connect(ui->actionMain_Menu,SIGNAL(triggered()),this,SLOT(mainMenuClicked()));
}

trainer::~trainer()
{
    delete ui;
}

void trainer::mainMenuClicked(){
    e.show();
    this->close();
}
