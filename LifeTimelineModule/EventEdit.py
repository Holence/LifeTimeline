from DongliTeahousePySideWheel import *

from LifeTimelineModule.Ui_EventEdit import Ui_EventEdit
class EventEdit(Ui_EventEdit,QWidget):
	def __init__(self,EventEditSession,birthday,color):
		super().__init__(EventEditSession)
		self.setupUi(self)
		self.color=color
		self.dateEdit_begin.setDate(birthday)
		self.dateEdit_end.setDate(birthday)
		self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)
		self.pushButton_color.clicked.connect(self.setColor)
	
	def setColor(self):
		color = QColorDialog.getColor(self.color,self)
		if color.isValid():
			self.color=color.name()
			self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)