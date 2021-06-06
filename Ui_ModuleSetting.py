# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleSetting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_ModuleSetting(object):
    def setupUi(self, ModuleSetting):
        if not ModuleSetting.objectName():
            ModuleSetting.setObjectName(u"ModuleSetting")
        ModuleSetting.resize(645, 468)
        ModuleSetting.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(ModuleSetting)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_page1 = QPushButton(ModuleSetting)
        self.pushButton_page1.setObjectName(u"pushButton_page1")
        icon = QIcon()
        icon.addFile(u":/white/white_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_page1.setIcon(icon)
        self.pushButton_page1.setIconSize(QSize(32, 32))
        self.pushButton_page1.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_page1)

        self.pushButton_page2 = QPushButton(ModuleSetting)
        self.pushButton_page2.setObjectName(u"pushButton_page2")
        icon1 = QIcon()
        icon1.addFile(u":/white/white_hard-drive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_page2.setIcon(icon1)
        self.pushButton_page2.setIconSize(QSize(32, 32))
        self.pushButton_page2.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_page2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.stackedWidget = QStackedWidget(ModuleSetting)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.spinBox = QSpinBox(self.page)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)

        self.dateEdit = QDateEdit(self.page)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(ModuleSetting)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ModuleSetting)
    # setupUi

    def retranslateUi(self, ModuleSetting):
        ModuleSetting.setWindowTitle(QCoreApplication.translate("ModuleSetting", u"Form", None))
        self.pushButton_page1.setText("")
        self.pushButton_page2.setText("")
        self.label.setText(QCoreApplication.translate("ModuleSetting", u"Lifespan", None))
        self.label_2.setText(QCoreApplication.translate("ModuleSetting", u"Birthday", None))
    # retranslateUi

