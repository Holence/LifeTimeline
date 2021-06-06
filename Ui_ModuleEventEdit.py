# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleEventEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModuleEventEdit(object):
    def setupUi(self, ModuleEventEdit):
        if not ModuleEventEdit.objectName():
            ModuleEventEdit.setObjectName(u"ModuleEventEdit")
        ModuleEventEdit.resize(791, 484)
        self.verticalLayout = QVBoxLayout(ModuleEventEdit)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(52, 0, 0, 0)
        self.splitter = QSplitter(ModuleEventEdit)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.dateEdit_begin = QDateEdit(self.layoutWidget_2)
        self.dateEdit_begin.setObjectName(u"dateEdit_begin")

        self.gridLayout_2.addWidget(self.dateEdit_begin, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.dateEdit_end = QDateEdit(self.layoutWidget_2)
        self.dateEdit_end.setObjectName(u"dateEdit_end")

        self.gridLayout_2.addWidget(self.dateEdit_end, 3, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 5, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget_2)
        self.layoutWidget_3 = QWidget(self.splitter)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.gridLayout = QGridLayout(self.layoutWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_color = QPushButton(self.layoutWidget_3)
        self.pushButton_color.setObjectName(u"pushButton_color")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setMaximumSize(QSize(15, 15))
        self.pushButton_color.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton_color)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)

        self.listWidget = QListWidget(self.layoutWidget_3)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 3, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget_3)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(ModuleEventEdit)

        QMetaObject.connectSlotsByName(ModuleEventEdit)
    # setupUi

    def retranslateUi(self, ModuleEventEdit):
        ModuleEventEdit.setWindowTitle(QCoreApplication.translate("ModuleEventEdit", u"EventEdit", None))
        self.label.setText(QCoreApplication.translate("ModuleEventEdit", u"Date Begin", None))
        self.label_2.setText(QCoreApplication.translate("ModuleEventEdit", u"Date End", None))
        self.label_3.setText(QCoreApplication.translate("ModuleEventEdit", u"Description", None))
        self.label_4.setText(QCoreApplication.translate("ModuleEventEdit", u"Color", None))
        self.pushButton_color.setText("")
        self.label_5.setText(QCoreApplication.translate("ModuleEventEdit", u"Picture List", None))
    # retranslateUi

