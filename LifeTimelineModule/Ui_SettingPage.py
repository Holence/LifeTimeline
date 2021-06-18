# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SettingPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingPage(object):
    def setupUi(self, SettingPage):
        if not SettingPage.objectName():
            SettingPage.setObjectName(u"SettingPage")
        SettingPage.resize(400, 300)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 185, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.dateEdit_birthday = QDateEdit(self.page)
        self.dateEdit_birthday.setObjectName(u"dateEdit_birthday")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_birthday.sizePolicy().hasHeightForWidth())
        self.dateEdit_birthday.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.dateEdit_birthday, 3, 0, 1, 1)

        self.pushButton_birthday = QPushButton(self.page)
        self.pushButton_birthday.setObjectName(u"pushButton_birthday")

        self.gridLayout.addWidget(self.pushButton_birthday, 3, 1, 1, 1)

        self.pushButton_lifespan = QPushButton(self.page)
        self.pushButton_lifespan.setObjectName(u"pushButton_lifespan")

        self.gridLayout.addWidget(self.pushButton_lifespan, 1, 1, 1, 1)

        self.label_birthday = QLabel(self.page)
        self.label_birthday.setObjectName(u"label_birthday")

        self.gridLayout.addWidget(self.label_birthday, 2, 0, 1, 1)

        self.label_cubewidth = QLabel(self.page)
        self.label_cubewidth.setObjectName(u"label_cubewidth")

        self.gridLayout.addWidget(self.label_cubewidth, 4, 0, 1, 1)

        self.label_lifesapn = QLabel(self.page)
        self.label_lifesapn.setObjectName(u"label_lifesapn")

        self.gridLayout.addWidget(self.label_lifesapn, 0, 0, 1, 1)

        self.spinBox_lifespan = QSpinBox(self.page)
        self.spinBox_lifespan.setObjectName(u"spinBox_lifespan")
        sizePolicy.setHeightForWidth(self.spinBox_lifespan.sizePolicy().hasHeightForWidth())
        self.spinBox_lifespan.setSizePolicy(sizePolicy)
        self.spinBox_lifespan.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox_lifespan, 1, 0, 1, 1)

        self.spinBox_cubewidth = QSpinBox(self.page)
        self.spinBox_cubewidth.setObjectName(u"spinBox_cubewidth")
        sizePolicy.setHeightForWidth(self.spinBox_cubewidth.sizePolicy().hasHeightForWidth())
        self.spinBox_cubewidth.setSizePolicy(sizePolicy)
        self.spinBox_cubewidth.setMinimum(5)
        self.spinBox_cubewidth.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox_cubewidth, 5, 0, 1, 1)

        self.pushButton_cubewidth = QPushButton(self.page)
        self.pushButton_cubewidth.setObjectName(u"pushButton_cubewidth")

        self.gridLayout.addWidget(self.pushButton_cubewidth, 5, 1, 1, 1)

        SettingPage.addWidget(self.page)

        self.retranslateUi(SettingPage)

        QMetaObject.connectSlotsByName(SettingPage)
    # setupUi

    def retranslateUi(self, SettingPage):
        SettingPage.setWindowTitle(QCoreApplication.translate("SettingPage", u"SettingPage", None))
        self.pushButton_birthday.setText(QCoreApplication.translate("SettingPage", u"Apply", None))
        self.pushButton_lifespan.setText(QCoreApplication.translate("SettingPage", u"Apply", None))
        self.label_birthday.setText(QCoreApplication.translate("SettingPage", u"Birthday", None))
        self.label_cubewidth.setText(QCoreApplication.translate("SettingPage", u"Week Cube Width", None))
        self.label_lifesapn.setText(QCoreApplication.translate("SettingPage", u"Lifespan", None))
        self.pushButton_cubewidth.setText(QCoreApplication.translate("SettingPage", u"Apply", None))
    # retranslateUi

