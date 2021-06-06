# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleLifeTimeLine.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_ModuleLifeTimeline(object):
    def setupUi(self, ModuleLifeTimeline):
        if not ModuleLifeTimeline.objectName():
            ModuleLifeTimeline.setObjectName(u"ModuleLifeTimeline")
        ModuleLifeTimeline.resize(401, 164)
        self.actionAdd_Event = QAction(ModuleLifeTimeline)
        self.actionAdd_Event.setObjectName(u"actionAdd_Event")
        icon = QIcon()
        icon.addFile(u":/white/white_plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Event.setIcon(icon)
        self.horizontalLayout = QHBoxLayout(ModuleLifeTimeline)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.splitter = QSplitter(ModuleLifeTimeline)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.graphicsView = QGraphicsView(self.splitter)
        self.graphicsView.setObjectName(u"graphicsView")
        self.splitter.addWidget(self.graphicsView)
        self.listWidget = QListWidget(self.splitter)
        self.listWidget.setObjectName(u"listWidget")
        self.splitter.addWidget(self.listWidget)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(ModuleLifeTimeline)

        QMetaObject.connectSlotsByName(ModuleLifeTimeline)
    # setupUi

    def retranslateUi(self, ModuleLifeTimeline):
        ModuleLifeTimeline.setWindowTitle(QCoreApplication.translate("ModuleLifeTimeline", u"Form", None))
        self.actionAdd_Event.setText(QCoreApplication.translate("ModuleLifeTimeline", u"Add Event", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Event.setShortcut(QCoreApplication.translate("ModuleLifeTimeline", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

