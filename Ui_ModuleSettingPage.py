# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleSettingPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModuleSettingPage(object):
    def setupUi(self, ModuleSettingPage):
        if not ModuleSettingPage.objectName():
            ModuleSettingPage.setObjectName(u"ModuleSettingPage")
        ModuleSettingPage.resize(400, 300)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_lifesapn = QLabel(self.page)
        self.label_lifesapn.setObjectName(u"label_lifesapn")

        self.gridLayout.addWidget(self.label_lifesapn, 0, 0, 1, 1)

        self.spinBox_lifespan = QSpinBox(self.page)
        self.spinBox_lifespan.setObjectName(u"spinBox_lifespan")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_lifespan.sizePolicy().hasHeightForWidth())
        self.spinBox_lifespan.setSizePolicy(sizePolicy)
        self.spinBox_lifespan.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox_lifespan, 1, 0, 1, 1)

        self.pushButton_lifespan = QPushButton(self.page)
        self.pushButton_lifespan.setObjectName(u"pushButton_lifespan")

        self.gridLayout.addWidget(self.pushButton_lifespan, 1, 1, 1, 1)

        self.label_birthday = QLabel(self.page)
        self.label_birthday.setObjectName(u"label_birthday")

        self.gridLayout.addWidget(self.label_birthday, 2, 0, 1, 1)

        self.dateEdit_birthday = QDateEdit(self.page)
        self.dateEdit_birthday.setObjectName(u"dateEdit_birthday")
        sizePolicy.setHeightForWidth(self.dateEdit_birthday.sizePolicy().hasHeightForWidth())
        self.dateEdit_birthday.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.dateEdit_birthday, 3, 0, 1, 1)

        self.pushButton_birthday = QPushButton(self.page)
        self.pushButton_birthday.setObjectName(u"pushButton_birthday")

        self.gridLayout.addWidget(self.pushButton_birthday, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 185, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        ModuleSettingPage.addWidget(self.page)

        self.retranslateUi(ModuleSettingPage)

        QMetaObject.connectSlotsByName(ModuleSettingPage)
    # setupUi

    def retranslateUi(self, ModuleSettingPage):
        ModuleSettingPage.setWindowTitle(QCoreApplication.translate("ModuleSettingPage", u"StackedWidget", None))
        self.label_lifesapn.setText(QCoreApplication.translate("ModuleSettingPage", u"Lifespan", None))
        self.pushButton_lifespan.setText(QCoreApplication.translate("ModuleSettingPage", u"Apply", None))
        self.label_birthday.setText(QCoreApplication.translate("ModuleSettingPage", u"Birthday", None))
        self.pushButton_birthday.setText(QCoreApplication.translate("ModuleSettingPage", u"Apply", None))
    # retranslateUi

