from DongliTeahousePySideWheel import *
from LifeTimelineWidget.WeekCube import WeekCube
from LifeTimelineSession.EventEditSession import EventEditSession

from LifeTimelineModule.Ui_LifeWeekChart import Ui_LifeWeekChart
class LifeWeekChart(Ui_LifeWeekChart,QWidget):
	def __init__(self,Headquarter):
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
		
		self.updateView()

	def initializeSignal(self):
		self.actionAdd_Event.triggered.connect(self.eventAdd)
		self.addAction(self.actionAdd_Event)

		self.Headquarter.addActionToMainMenu(self.actionAdd_Event)
		self.Headquarter.addSeparatorToMainMenu()

	def updateView(self):
		self.scene.clear()

		now=self.Headquarter.birthday
		for i in range(self.Headquarter.lifespan):
			for j in range(52):
				
				colorList=[]
				for event in self.data:
					if QDate_to_Str(now) >= event["begin"] and QDate_to_Str(now) <= event["end"]:
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
			if Str_To_QDate(event["begin"])<=date<=Str_To_QDate(event["end"]):
				button=DongliTeahouseWidget.DongliTeahouseCapsuleButton(self,event["name"],event["color"])
				button.clicked.connect(partial(self.eventEdit,index))
				self.verticalLayout_EventButtons.addWidget(button)
			index+=1
		
	
	def eventEdit(self,index):
		
		event=self.data[index]

		dlg=EventEditSession(self.Headquarter,event["color"])
		dlg.eventedit.lineEdit_name.setText(event["name"])
		dlg.eventedit.dateEdit_begin.setDate(Str_To_QDate(event["begin"]))
		dlg.eventedit.dateEdit_end.setDate(Str_To_QDate(event["end"]))
		dlg.eventedit.plainTextEdit.setPlainText(event["description"])
		# dlg.eventedit.listWidget

		if dlg.exec_():
			name=dlg.eventedit.lineEdit_name.text()
			end=QDate_to_Str(dlg.eventedit.dateEdit_end.date())
			begin=QDate_to_Str(dlg.eventedit.dateEdit_begin.date())
			description=dlg.eventedit.plainTextEdit.toPlainText()
			color=dlg.eventedit.color
			# dlg.eventedit.listWidget

			event["name"]=name
			event["begin"]=begin
			event["end"]=end
			event["description"]=description
			event["color"]=color

			self.updateView()
			try:
				self.updateInfoArea(self.dateEdit_SelectedData.date())
			except:
				pass

	def eventAdd(self):
		dlg=EventEditSession(self.Headquarter)
		if dlg.exec_():
			name=dlg.eventedit.lineEdit_name.text()
			end=QDate_to_Str(dlg.eventedit.dateEdit_end.date())
			begin=QDate_to_Str(dlg.eventedit.dateEdit_begin.date())
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

			self.updateView()
			try:
				self.updateInfoArea(self.dateEdit_SelectedData.date())
			except:
				pass
