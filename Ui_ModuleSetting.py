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


class Ui_ModuleSetting(object):
    def setupUi(self, ModuleSetting):
        if not ModuleSetting.objectName():
            ModuleSetting.setObjectName(u"ModuleSetting")
        ModuleSetting.resize(427, 346)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_lifesapn = QLabel(self.page)
        self.label_lifesapn.setObjectName(u"label_lifesapn")

        self.gridLayout_2.addWidget(self.label_lifesapn, 0, 0, 1, 1)

        self.label_birthday = QLabel(self.page)
        self.label_birthday.setObjectName(u"label_birthday")

        self.gridLayout_2.addWidget(self.label_birthday, 2, 0, 1, 1)

        self.spinBox_lifespan = QSpinBox(self.page)
        self.spinBox_lifespan.setObjectName(u"spinBox_lifespan")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_lifespan.sizePolicy().hasHeightForWidth())
        self.spinBox_lifespan.setSizePolicy(sizePolicy)
        self.spinBox_lifespan.setMaximum(1000)

        self.gridLayout_2.addWidget(self.spinBox_lifespan, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 273, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.dateEdit_birthday = QDateEdit(self.page)
        self.dateEdit_birthday.setObjectName(u"dateEdit_birthday")
        sizePolicy.setHeightForWidth(self.dateEdit_birthday.sizePolicy().hasHeightForWidth())
        self.dateEdit_birthday.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.dateEdit_birthday, 3, 0, 1, 1)

        self.pushButton_lifespan = QPushButton(self.page)
        self.pushButton_lifespan.setObjectName(u"pushButton_lifespan")

        self.gridLayout_2.addWidget(self.pushButton_lifespan, 1, 1, 1, 1)

        self.pushButton_birthday = QPushButton(self.page)
        self.pushButton_birthday.setObjectName(u"pushButton_birthday")

        self.gridLayout_2.addWidget(self.pushButton_birthday, 3, 1, 1, 1)

        ModuleSetting.addWidget(self.page)

        self.retranslateUi(ModuleSetting)

        QMetaObject.connectSlotsByName(ModuleSetting)
    # setupUi

    def retranslateUi(self, ModuleSetting):
        ModuleSetting.setWindowTitle(QCoreApplication.translate("ModuleSetting", u"ModuleSetting", None))
        self.label_lifesapn.setText(QCoreApplication.translate("ModuleSetting", u"Lifespan", None))
        self.label_birthday.setText(QCoreApplication.translate("ModuleSetting", u"Birthday", None))
        self.pushButton_lifespan.setText(QCoreApplication.translate("ModuleSetting", u"Apply", None))
        self.pushButton_birthday.setText(QCoreApplication.translate("ModuleSetting", u"Apply", None))
    # retranslateUi

