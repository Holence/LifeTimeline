from DTPySide import *

from LifeTimelineSession.MainSession import MainSession
from LifeTimelineModule.Ui_LifeWeekChart import Ui_LifeWeekChart
class LifeWeekChart(Ui_LifeWeekChart,QWidget):
	def __init__(self, Headquarter: MainSession):
		super().__init__(Headquarter)
		self.setupUi(self)
		self.Headquarter=Headquarter

		#这里为了便于访问，用self.data作为指针代替Headquarter.data
		self.data=Headquarter.data
		
		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):

		self.scene=QGraphicsScene()
		self.graphicsView.setScene(self.scene)
		
		# self.graphicsView.horizontalScrollBar().setPageStep(1)
		# self.graphicsView.horizontalScrollBar().setSingleStep(1)
		self.actionAdd_Event.setIcon(IconFromCurrentTheme("plus.svg"))
		
		self.updateView()

	def initializeSignal(self):
		self.actionAdd_Event.triggered.connect(self.eventAdd)
		self.addAction(self.actionAdd_Event)

		self.Headquarter.addActionToMainMenu(self.actionAdd_Event)
		self.Headquarter.addSeparatorToMainMenu()

	def updateView(self):
		from LifeTimelineWidget.WeekCube import WeekCube

		self.scene.clear()

		now=self.Headquarter.birthday
		for i in range(self.Headquarter.lifespan):
			for j in range(52):
				
				colorList=[]
				for event in self.data:
					if now.toString("yyyyMMdd") >= event["begin"] and now.toString("yyyyMMdd") <= event["end"]:
						colorList.append(event["color"])
				
				temp=WeekCube(self.Headquarter.birthday,now,colorList,self,self.Headquarter.cubewidth)
				# QGraphicsRectItem并不是QWidget，不能设定signal和connect
				# temp.clicked.connect(self.updateInfoArea)
				self.scene.addItem(temp)

				now=now.addDays(7)
		
		# 设置新的cubewidth后要使所有的item居中，重置SceneRect
		self.graphicsView.setSceneRect(self.scene.itemsBoundingRect())
	
	def updateInfoArea(self,date,clicked_pos):
		self.dateEdit_SelectedData.setDate(date)
		Clear_Layout(self.verticalLayout_EventButtons)
		
		try:
			self.current_weekcube.eraseBorder()
		except:
			pass
		self.current_weekcube=self.scene.itemAt(clicked_pos.x(),clicked_pos.y(),self.graphicsView.transform())
		self.current_weekcube.drawBorder()
		
		index=0
		for event in self.data:
			if QDate.fromString(event["begin"],"yyyyMMdd")<=date<=QDate.fromString(event["end"],"yyyyMMdd"):
				button=DTWidget.DTCapsuleButton(self,event["name"],event["color"])
				button.clicked.connect(partial(self.eventEdit,index))
				self.verticalLayout_EventButtons.addWidget(button)
			index+=1
		
	
	def eventEdit(self,index):
		
		event=self.data[index]
		
		from LifeTimelineSession.EventEditSession import EventEditSession
		dlg=EventEditSession(self.Headquarter,"Edit Event",event["color"])
		dlg.eventedit.lineEdit_name.setText(event["name"])
		dlg.eventedit.dateEdit_begin.setDate(QDate.fromString(event["begin"],"yyyyMMdd"))
		dlg.eventedit.dateEdit_end.setDate(QDate.fromString(event["end"],"yyyyMMdd"))
		dlg.eventedit.plainTextEdit.setPlainText(event["description"])
		# dlg.eventedit.listWidget

		dlg.adjustSize()
		MoveToCenterOfScreen(dlg)

		if dlg.exec_():
			name=dlg.eventedit.lineEdit_name.text()
			end=dlg.eventedit.dateEdit_end.date().toString("yyyyMMdd")
			begin=dlg.eventedit.dateEdit_begin.date().toString("yyyyMMdd")
			description=dlg.eventedit.plainTextEdit.toPlainText()
			color=dlg.eventedit.color
			# dlg.eventedit.listWidget

			event["name"]=name
			event["begin"]=begin
			event["end"]=end
			event["description"]=description
			event["color"]=color

			try:
				pos=self.current_weekcube.pos()
				self.updateView()
				self.updateInfoArea(self.dateEdit_SelectedData.date(),pos)
			except:
				self.updateView()
		else:
			if dlg.isDeletingEvent==True:
				self.data.pop(index)
			
				try:
					pos=self.current_weekcube.pos()
					self.updateView()
					self.updateInfoArea(self.dateEdit_SelectedData.date(),pos)
				except:
					self.updateView()

	def eventAdd(self):
		from LifeTimelineSession.EventEditSession import EventEditSession
		dlg=EventEditSession(self.Headquarter,"Add New Event")
		
		dlg.eventedit.pushButton_delete.hide()

		dlg.adjustSize()
		MoveToCenterOfScreen(dlg)

		if dlg.exec_():
			name=dlg.eventedit.lineEdit_name.text()
			end=dlg.eventedit.dateEdit_end.date().toString("yyyyMMdd")
			begin=dlg.eventedit.dateEdit_begin.date().toString("yyyyMMdd")
			description=dlg.eventedit.plainTextEdit.toPlainText()
			color=dlg.eventedit.color
			# dlg.eventedit.listWidget

			event={
				"name":name,
				"begin":begin,
				"end":end,
				"description":description,
				"color":color
			}

			self.data.append(event)
			
			try:
				pos=self.current_weekcube.pos()
				self.updateView()
				self.updateInfoArea(self.dateEdit_SelectedData.date(),pos)
			except:
				self.updateView()