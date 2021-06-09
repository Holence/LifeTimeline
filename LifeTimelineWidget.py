from DongliTeahousePySideWheel import DongliTeahouseMessageIcon
from DongliTeahousePySideWheel import DongliTeahousePalette
from DongliTeahousePySideWheel.DongliTeahouseFunction import *

class WeekCube(QGraphicsRectItem):
	def __init__(self,begin,now,colorList,parent):
		super().__init__(0,0,10,10)
		self.PAPA=parent
		self.now=now

		weeks=int(begin.daysTo(now)/7)
		y=weeks//52*15
		x=weeks%52*15
		self.setPos(float(x),float(y))
		
		#竟然可以直接略过QBrush？！
		# self.setBrush(QBrush(QColor("#FF6265")))
		# self.setBrush(QColor("#FF6265"))
		self.color=Generate_ConicalGradientColor(colorList)
		self.setBrush(self.color)
		self.setAcceptHoverEvents(True)
	
	def hoverEnterEvent(self,event):
		super().hoverEnterEvent(event)
		pen=QPen()
		pen.setWidth(2)
		self.setPen(pen)
	
	def hoverLeaveEvent(self,event):
		super().hoverLeaveEvent(event)
		pen=QPen()
		pen.setWidth(0)
		self.setPen(pen)
	
	def mousePressEvent(self,event):
		super().mousePressEvent(event)
