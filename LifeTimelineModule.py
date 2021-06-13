from functools import partial
from DongliTeahousePySideWheel.DongliTeahouseTemplate import *
from LifeTimelineWidget import *

###################################################################################################

# Setting

from Ui_ModuleSettingPage import Ui_ModuleSettingPage
class SettingPageModule(Ui_ModuleSettingPage,QStackedWidget):
	def __init__(self,Headquarter):
		super().__init__()
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.spinBox_lifespan.setValue(self.Headquarter.lifespan)
		self.pushButton_lifespan.clicked.connect(self.setLifespan)

		self.dateEdit_birthday.setDate(self.Headquarter.birthday)
		self.pushButton_birthday.clicked.connect(self.setBirthday)

		self.spinBox_cubewidth.setValue(self.Headquarter.cubewidth)
		self.pushButton_cubewidth.clicked.connect(self.setCubeWidth)

	def setLifespan(self):
		self.Headquarter.lifespan=self.spinBox_lifespan.value()
		self.Headquarter.UserSetting().setValue("lifespan",Fernet_Encrypt(self.Headquarter.password(),self.Headquarter.lifespan))
		self.Headquarter.LifeWeekChart.updateView()
	
	def setBirthday(self):
		self.Headquarter.birthday=self.dateEdit_birthday.date()
		self.Headquarter.UserSetting().setValue("birthday",Fernet_Encrypt(self.Headquarter.password(),QDate_to_Str(self.Headquarter.birthday)))
		self.Headquarter.LifeWeekChart.updateView()
	
	def setCubeWidth(self):
		self.Headquarter.cubewidth=self.spinBox_cubewidth.value()
		self.Headquarter.UserSetting().setValue("cubewidth",Fernet_Encrypt(self.Headquarter.password(),self.Headquarter.cubewidth))
		self.Headquarter.LifeWeekChart.updateView()

class SettingDialog(DongliTeahouseSettingDialog):
	def __init__(self,Headquarter):
		super().__init__(Headquarter)

		self.SettingPages=SettingPageModule(Headquarter)

		MenuButton1=DongliTeahouseSettingButton(QIcon(":/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)


###################################################################################################

# Event Edit

from Ui_ModuleEventEdit import Ui_ModuleEventEdit
class ModuleEventEdit(Ui_ModuleEventEdit,QWidget):
	def __init__(self,EventEditDialog,birthday,color):
		super().__init__(EventEditDialog)
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

class EventEditDialog(DongliTeahouseDialog):
	def __init__(self,Headquarter,color="#E6E6E6"):
		super().__init__(Headquarter,"Add New Event")
		self.eventedit=ModuleEventEdit(self,Headquarter.birthday,color)
		self.centralWidget.addWidget(self.eventedit)
		self.adjustSize()
	
	def accept(self):
		if self.eventedit.dateEdit_begin.date()>=self.eventedit.dateEdit_end.date():
			DongliTeahouseMessageBox(self,"Warning","Wrong Date Range!",DongliTeahouseIcon.Warning())
		else:
			super().accept()

###################################################################################################

# Life Week Chart

from Ui_ModuleLifeWeekChart import Ui_ModuleLifeWeekChart
class ModuleLifeWeekChart(Ui_ModuleLifeWeekChart,QWidget):
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
				button=DongliTeahouseCapsuleButton(self,event["name"],event["color"])
				button.clicked.connect(partial(self.eventEdit,index))
				self.verticalLayout_EventButtons.addWidget(button)
			index+=1
		
	
	def eventEdit(self,index):
		
		event=self.data[index]

		dlg=EventEditDialog(self.Headquarter,event["color"])
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
		dlg=EventEditDialog(self.Headquarter)
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

###################################################################################################

# Mainwidow

class MainWindow(DongliTeahouseMainWindow):
	def __init__(self,app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		self.LifeWeekChart=ModuleLifeWeekChart(self)
		self.setCentralWidget(self.LifeWeekChart)

	def saveWindowStatus(self):
		super().saveWindowStatus()
		self.UserSetting().setValue("WindowStatus/LifeWeekChartSplitter",self.LifeWeekChart.splitter.saveState())
	
	def restoreWindowStatus(self):
		super().restoreWindowStatus()
		try:
			self.LifeWeekChart.splitter.restoreState(self.UserSetting().value("WindowStatus/LifeWeekChartSplitter"))
		except:
			pass

	def loadData(self):
		super().loadData()

		if os.path.exists("./LifeTimelime.dlcw"):
			self.data=Fernet_Decrypt_Load(self.password(),"./LifeTimelime.dlcw")
			if self.data==False:
				DongliTeahouseMessageBox(self,"Error","Data Error!")
				exit()
		else:
			self.data=[]
			Fernet_Encrypt_Save(self.password(),self.data,"./LifeTimelime.dlcw")
		print(self.data)

		try:
			self.lifespan=int(Fernet_Decrypt(self.password(),self.UserSetting().value("lifespan")))
			if self.lifespan==0:
				self.lifespan=150
		except:
			self.lifespan=150
		
		try:
			birthday=Fernet_Decrypt(self.password(),self.UserSetting().value("birthday"))
			self.birthday=Str_To_QDate(birthday)
		except:
			self.birthday=QDate(1970,1,1)

		try:
			self.cubewidth=int(Fernet_Decrypt(self.password(),self.UserSetting().value("cubewidth")))
			if self.cubewidth==0:
				self.cubewidth=20
		except:
			self.cubewidth=20


	def saveData(self):
		super().saveData()

		Fernet_Encrypt_Save(self.password(),self.data,"./LifeTimelime.dlcw")
	
	def SaveAllEncryptData(self):
		super().SaveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("lifespan",Fernet_Encrypt(self.password(),self.lifespan))
		self.UserSetting().setValue("birthday",Fernet_Encrypt(self.password(),QDate_to_Str(self.birthday)))
		self.UserSetting().setValue("cubewidth",Fernet_Encrypt(self.password(),self.cubewidth))
	
	def setting(self):
		dlg=SettingDialog(self)
		dlg.exec_()