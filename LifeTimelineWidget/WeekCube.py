from DTPySide import *

class WeekCube(QGraphicsRectItem):
	
	def __init__(self,birthday,week_start,colorList,moduleLifeWeekChart,cubewidth):
		self.cubewidth=cubewidth
		super().__init__(0,0,self.cubewidth,self.cubewidth)
		self.moduleLifeWeekChart=moduleLifeWeekChart
		self.week_start=week_start

		weeks=int(birthday.daysTo(self.week_start)/7)
		y=weeks//52*(self.cubewidth/2*3)
		x=weeks%52*(self.cubewidth/2*3)
		self.setPos(float(x),float(y))
		
		self.color=Generate_ConicalGradientColor(colorList,self.cubewidth)
		self.setBrush(self.color)
		self.setAcceptHoverEvents(True)
	
	def hoverEnterEvent(self,event):
		super().hoverEnterEvent(event)
		
		tooltip_text=QDate_to_Str(self.week_start,".")+"\n"
		for event in self.moduleLifeWeekChart.data:
			if Str_To_QDate(event["begin"]) <= self.week_start <= Str_To_QDate(event["end"]):
				tooltip_text+=event["name"]+"\n"
		tooltip_text=tooltip_text[:-1]

		# 设置父组件为graphicsView
		self.tooltip=DTWidget.DTToolTip(self.moduleLifeWeekChart.graphicsView,tooltip_text)
		
		# 以graphicsView为坐标系，计算相对坐标
		position=self.moduleLifeWeekChart.graphicsView.mapFromScene(self.pos()-QPoint(0,self.tooltip.height()))
		
		# 靠上了，下移
		if position.y()<0:
			position=position+QPoint(0,self.tooltip.height()+self.cubewidth)
		
		# 靠右了，左移
		if position.x()+self.tooltip.width() > self.moduleLifeWeekChart.graphicsView.width():
			position=position-QPoint(self.tooltip.width()-self.cubewidth,0)
			
			# 朝左，还得这么麻烦得重新设置qss……
			self.tooltip.setStyleSheet(""" 
				QLabel {
					background-color: #0C0B0B;	
					color: #E6E6E6;
					padding-left: 10px;
					padding-right: 10px;
					border-radius: %spx;
					border: 1px solid #0C0B0B;
					border-right: 3px solid #FF6265;
				}
			"""%(self.tooltip.font().pointSize()//2))

			# setStyleSheet会自动清空font，这里还得手动set一下
			self.tooltip.setFont(self.moduleLifeWeekChart.font())
		
		# move操作是以父组件（graphicsView）为坐标原点的相对位移
		self.tooltip.move(position)
		
		self.tooltip.show()
	
	def hoverLeaveEvent(self,event):
		super().hoverLeaveEvent(event)

		self.tooltip.deleteLater()
	
	def mousePressEvent(self,event):
		super().mousePressEvent(event)
		# QGraphicsRectItem并不是QWidget，不能设定signal和connect
		# 这里就直接用parent指针调用函数了
		self.moduleLifeWeekChart.updateInfoArea(self.week_start,self.pos())
	
	def drawBorder(self):
		pen=QPen()
		pen.setColor("#ffff00")
		pen.setWidth(int(self.cubewidth/5))
		self.setPen(pen)
	
	def eraseBorder(self):
		pen=QPen()
		pen.setWidth(0)
		self.setPen(pen)