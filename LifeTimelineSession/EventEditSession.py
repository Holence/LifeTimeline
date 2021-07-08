from DTPySide import *

from LifeTimelineModule.EventEdit import EventEdit

class EventEditSession(DTFrame.DTDialog):
	def __init__(self,Headquarter,title,color="#E6E6E6"):
		super().__init__(Headquarter,title)
		
		self.eventedit=EventEdit(self,Headquarter.birthday,color)
		self.centralWidget.addWidget(self.eventedit)
		self.adjustSize()

		self.isDeletingEvent=False
	
	def accept(self):
		if self.eventedit.dateEdit_begin.date()>=self.eventedit.dateEdit_end.date():
			DTFrame.DTMessageBox(self,"Warning","Wrong Date Range!",DTIcon.Warning())
		else:
			super().accept()

	def deleteEventQuit(self):
		self.isDeletingEvent=True
		self.reject()