# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleLifeWeekChart.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_ModuleLifeWeekChart(object):
    def setupUi(self, ModuleLifeWeekChart):
        if not ModuleLifeWeekChart.objectName():
            ModuleLifeWeekChart.setObjectName(u"ModuleLifeWeekChart")
        ModuleLifeWeekChart.resize(647, 572)
        self.actionAdd_Event = QAction(ModuleLifeWeekChart)
        self.actionAdd_Event.setObjectName(u"actionAdd_Event")
        icon = QIcon()
        icon.addFile(u":/white/white_plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Event.setIcon(icon)
        self.horizontalLayout = QHBoxLayout(ModuleLifeWeekChart)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.splitter = QSplitter(ModuleLifeWeekChart)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.graphicsView = QGraphicsView(self.splitter)
        self.graphicsView.setObjectName(u"graphicsView")
        self.splitter.addWidget(self.graphicsView)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.dateEdit_SelectedData = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_SelectedData.setObjectName(u"dateEdit_SelectedData")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_SelectedData.sizePolicy().hasHeightForWidth())
        self.dateEdit_SelectedData.setSizePolicy(sizePolicy)
        self.dateEdit_SelectedData.setReadOnly(True)

        self.gridLayout.addWidget(self.dateEdit_SelectedData, 0, 1, 1, 1)

        self.verticalLayout_EventButtons = QVBoxLayout()
        self.verticalLayout_EventButtons.setSpacing(15)
        self.verticalLayout_EventButtons.setObjectName(u"verticalLayout_EventButtons")

        self.gridLayout.addLayout(self.verticalLayout_EventButtons, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(ModuleLifeWeekChart)

        QMetaObject.connectSlotsByName(ModuleLifeWeekChart)
    # setupUi

    def retranslateUi(self, ModuleLifeWeekChart):
        ModuleLifeWeekChart.setWindowTitle(QCoreApplication.translate("ModuleLifeWeekChart", u"ModuleLifeWeekChart", None))
        self.actionAdd_Event.setText(QCoreApplication.translate("ModuleLifeWeekChart", u"Add Event", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Event.setShortcut(QCoreApplication.translate("ModuleLifeWeekChart", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("ModuleLifeWeekChart", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("ModuleLifeWeekChart", u"Event List", None))
    # retranslateUi

