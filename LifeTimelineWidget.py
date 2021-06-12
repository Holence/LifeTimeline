from DongliTeahousePySideWheel.DongliTeahouseWidget import *

class WeekCube(QGraphicsRectItem):
	
	def __init__(self,begin,now,colorList,parent):
		super().__init__(0,0,10,10)
		self.PAPA=parent
		self.now=now

		weeks=int(begin.daysTo(now)/7)
		y=weeks//52*15
		x=weeks%52*15
		self.setPos(float(x),float(y))
		
		self.color=Generate_ConicalGradientColor(colorList)
		self.setBrush(self.color)
		self.setAcceptHoverEvents(True)
	
	def hoverEnterEvent(self,event):
		super().hoverEnterEvent(event)
		pen=QPen()
		pen.setWidth(2)
		self.setPen(pen)
		
		tooltip_text=QDate_to_Str(self.now,".")+"\n"
		for event in self.PAPA.PAPA.data:
			if Str_To_QDate(event["begin"])<=self.now<=Str_To_QDate(event["end"]):
				tooltip_text+=event["name"]+"\n"
		tooltip_text=tooltip_text[:-1]

		# 设置parent为graphicsView
		self.tooltip=DongliTeahouseToolTip(self.PAPA.graphicsView,tooltip_text)
		
		# 以graphicsView为坐标系，计算相对坐标
		position=self.PAPA.graphicsView.mapFromScene(self.pos()-QPoint(0,self.tooltip.height()))
		
		# 靠上了，下移
		if position.y()<0:
			position=position+QPoint(0,self.tooltip.height()+15)
		
		# 靠右了，左移
		if position.x()+self.tooltip.width()>self.PAPA.graphicsView.width():
			position=position-QPoint(self.tooltip.width()-15,0)
			
			# 朝左，还得这么麻烦得重新设置qss……
			self.tooltip.setStyleSheet(""" 
				QLabel {
					background-color: #0C0B0B;	
					color: #E6E6E6;
					padding-left: 10px;
					padding-right: 10px;
					border-radius: 17px;
					border: 1px solid #0C0B0B;
					border-right: 3px solid #FF6265;
				}
			""")

			# setStyleSheet会自动清空font，这里还得手动set一下
			self.tooltip.setFont(self.PAPA.font())
		
		# move操作是以parent（graphicsView）为坐标原点的相对位移
		self.tooltip.move(position)
		
		self.tooltip.show()
	
	def hoverLeaveEvent(self,event):
		super().hoverLeaveEvent(event)
		pen=QPen()
		pen.setWidth(0)
		self.setPen(pen)

		self.tooltip.deleteLater()
	
	def mousePressEvent(self,event):
		super().mousePressEvent(event)
		# QGraphicsRectItem并不是QWidget，不能设定signal和connect
		# 这里就直接用parent指针调用函数了
		self.PAPA.updateInfoArea(self.now)