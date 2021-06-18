from DongliTeahousePySideWheel import *
from LifeTimelineModule.EventEdit import EventEdit

class EventEditSession(DongliTeahouseFrame.DongliTeahouseDialog):
	def __init__(self,Headquarter,color="#E6E6E6"):
		super().__init__(Headquarter,"Add New Event")
		self.eventedit=EventEdit(self,Headquarter.birthday,color)
		self.centralWidget.addWidget(self.eventedit)
		self.adjustSize()
	
	def accept(self):
		if self.eventedit.dateEdit_begin.date()>=self.eventedit.dateEdit_end.date():
			DongliTeahouseFrame.DongliTeahouseMessageBox(self,"Warning","Wrong Date Range!",DongliTeahouseIcon.Warning())
		else:
			super().accept()
