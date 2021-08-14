from DTPySide import *

from LifeTimelineModule.Ui_EventEdit import Ui_EventEdit
class EventEdit(Ui_EventEdit,QWidget):
	def __init__(self,EventEditSession,birthday,color):
		super().__init__(EventEditSession)
		self.setupUi(self)
		
		self.EventEditSession=EventEditSession

		self.color=color
		self.dateEdit_begin.setDate(birthday)
		self.dateEdit_end.setDate(birthday)
		self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;min-width:15px;min-height:15px;max-width:15px;max-height:15px;}"%self.color)
		self.pushButton_color.clicked.connect(self.setColor)

		self.pushButton_delete.clicked.connect(self.deleteEvent)
		self.pushButton_delete.setIcon(IconFromCurrentTheme("trash-2.svg"))
	
	def setColor(self):
		color = QColorDialog.getColor(self.color,self)
		if color.isValid():
			self.color=color.name()
			self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)
	
	def deleteEvent(self):
		if DTFrame.DTConfirmBox(self,"Delete Event Confirm","Do you want to delete event: \n"+self.lineEdit_name.text()).exec_():
			self.EventEditSession.deleteEventQuit()