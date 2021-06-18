# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EventEdit(object):
    def setupUi(self, EventEdit):
        if not EventEdit.objectName():
            EventEdit.setObjectName(u"EventEdit")
        EventEdit.resize(593, 359)
        self.verticalLayout_2 = QVBoxLayout(EventEdit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(42, 0, 0, 0)
        self.splitter = QSplitter(EventEdit)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 5, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.dateEdit_end = QDateEdit(self.layoutWidget)
        self.dateEdit_end.setObjectName(u"dateEdit_end")

        self.gridLayout.addWidget(self.dateEdit_end, 2, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.dateEdit_begin = QDateEdit(self.layoutWidget)
        self.dateEdit_begin.setObjectName(u"dateEdit_begin")

        self.gridLayout.addWidget(self.dateEdit_begin, 1, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_color = QPushButton(self.layoutWidget)
        self.pushButton_color.setObjectName(u"pushButton_color")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setMaximumSize(QSize(15, 15))
        self.pushButton_color.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton_color)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(EventEdit)

        QMetaObject.connectSlotsByName(EventEdit)
    # setupUi

    def retranslateUi(self, EventEdit):
        EventEdit.setWindowTitle(QCoreApplication.translate("EventEdit", u"EventEdit", None))
        self.label_4.setText(QCoreApplication.translate("EventEdit", u"Color", None))
        self.label_6.setText(QCoreApplication.translate("EventEdit", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("EventEdit", u"Date End", None))
        self.label.setText(QCoreApplication.translate("EventEdit", u"Date Begin", None))
        self.pushButton_color.setText("")
        self.label_3.setText(QCoreApplication.translate("EventEdit", u"Description", None))
        self.label_5.setText(QCoreApplication.translate("EventEdit", u"Picture List", None))
    # retranslateUi

