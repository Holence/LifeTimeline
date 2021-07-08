from DTPySide import *

from LifeTimelineModule.Ui_EventEdit import Ui_EventEdit
class EventEdit(Ui_EventEdit,QWidget):
	def __init__(self,EventEditSession,birthday,color):
		super().__init__(EventEditSession)
		self.setupUi(self)
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		
		self.EventEditSession=EventEditSession

		self.color=color
		self.dateEdit_begin.setDate(birthday)
		self.dateEdit_end.setDate(birthday)
		self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)
		self.pushButton_color.clicked.connect(self.setColor)

		self.pushButton_delete.clicked.connect(self.deleteEvent)
	
	def setColor(self):
		color = QColorDialog.getColor(self.color,self)
		if color.isValid():
			self.color=color.name()
			self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)
	
	def deleteEvent(self):
		dlg=DTFrame.DTDialog(self,"Delete Event Confirm")
		
		text="Do you want to delete event: \n"+self.lineEdit_name.text()
		
		#要继承字体就得设置好parent
		label=QLabel(text,dlg)
		# 要继承字体就得加上这句
		label.setAttribute(Qt.WA_WindowPropagation)
		
		dlg.centralWidget.addWidget(label)

		if dlg.exec_():
			self.EventEditSession.deleteEventQuit()