from functools import partial
from DongliTeahousePySideWheel.DongliTeahouseTemplate import *
from LifeTimelineWidget import *

###################################################################################################

# Setting

from Ui_ModuleSettingPage import Ui_ModuleSettingPage
class SettingPageModule(Ui_ModuleSettingPage,QStackedWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.PAPA=parent
		self.spinBox_lifespan.setValue(parent.lifespan)
		self.pushButton_lifespan.clicked.connect(self.setLifespan)

		self.dateEdit_birthday.setDate(parent.birthday)
		self.pushButton_birthday.clicked.connect(self.setBirthday)
	
	def setLifespan(self):
		self.PAPA.lifespan=self.spinBox_lifespan.value()
		self.PAPA.UserSetting().setValue("lifespan",Fernet_Encrypt(self.PAPA.password(),self.PAPA.lifespan))
		self.PAPA.LifeWeekChart.updateView()
	
	def setBirthday(self):
		self.PAPA.birthday=self.dateEdit_birthday.date()
		self.PAPA.UserSetting().setValue("birthday",Fernet_Encrypt(self.PAPA.password(),QDate_to_Str(self.PAPA.birthday)))
		self.PAPA.LifeWeekChart.updateView()

class SettingDialog(DongliTeahouseSettingDialog):
	def __init__(self, parent):
		super().__init__(parent)

		self.SettingPages=SettingPageModule(parent)

		MenuButton1=DongliTeahouseSettingButton(QIcon(":/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)


###################################################################################################

# Event Edit

from Ui_ModuleEventEdit import Ui_ModuleEventEdit
class ModuleEventEdit(Ui_ModuleEventEdit,QWidget):
	def __init__(self,parent,birthday,color):
		super().__init__(parent)
		self.setupUi(self)
		self.color=color
		self.dateEdit_begin.setDate(birthday)
		self.dateEdit_end.setDate(birthday)
		self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)
		self.pushButton_color.clicked.connect(self.setColor)
	
	def setColor(self):
		color = QColorDialog.getColor(self.color, self)
		if color.isValid():
			self.color=color.name()
			self.pushButton_color.setStyleSheet("QPushButton{background-color:%s;}"%self.color)

class EventEditDialog(DongliTeahouseDialog):
	def __init__(self,parent,color="#E6E6E6"):
		super().__init__(parent,"Add New Event")
		self.eventedit=ModuleEventEdit(self,parent.birthday,color)
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
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.PAPA=parent
		
		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):

		self.scene=QGraphicsScene()
		self.graphicsView.setScene(self.scene)
		self.updateView()

	def initializeSignal(self):
		self.actionAdd_Event.triggered.connect(self.eventAdd)
		self.addAction(self.actionAdd_Event)

		self.PAPA.addActionToMainMenu(self.actionAdd_Event)
		self.PAPA.addSeparatorToMainMenu()

	def updateView(self):
		self.scene.clear()

		now=self.PAPA.birthday
		for i in range(self.PAPA.lifespan):
			for j in range(52):
				
				colorList=[]
				for event in self.PAPA.data:
					if QDate_to_Str(now) >= event["begin"] and QDate_to_Str(now) <= event["end"]:
						colorList.append(event["color"])
				
				temp=WeekCube(self.PAPA.birthday,now,colorList,self)
				# QGraphicsRectItem并不是QWidget，不能设定signal和connect
				# temp.clicked.connect(self.updateInfoArea)
				self.scene.addItem(temp)

				now=now.addDays(7)
	
	def updateInfoArea(self,date):
		self.dateEdit_SelectedData.setDate(date)
		Clear_Layout(self.verticalLayout_EventButtons)
		
		index=0
		for event in self.PAPA.data:
			if Str_To_QDate(event["begin"])<=date<=Str_To_QDate(event["end"]):
				button=DongliTeahouseCapsuleButton(self,event["name"],event["color"])
				button.clicked.connect(partial(self.eventEdit,index))
				self.verticalLayout_EventButtons.addWidget(button)
				index+=1
		
	
	def eventEdit(self,index):
		
		dlg=EventEditDialog(self.PAPA,self.PAPA.data[index]["color"])
		dlg.eventedit.lineEdit_name.setText(self.PAPA.data[index]["name"])
		dlg.eventedit.dateEdit_begin.setDate(Str_To_QDate(self.PAPA.data[index]["begin"]))
		dlg.eventedit.dateEdit_end.setDate(Str_To_QDate(self.PAPA.data[index]["end"]))
		dlg.eventedit.plainTextEdit.setPlainText(self.PAPA.data[index]["description"])
		# dlg.eventedit.listWidget

		if dlg.exec_():
			name=dlg.eventedit.lineEdit_name.text()
			end=QDate_to_Str(dlg.eventedit.dateEdit_end.date())
			begin=QDate_to_Str(dlg.eventedit.dateEdit_begin.date())
			description=dlg.eventedit.plainTextEdit.toPlainText()
			color=dlg.eventedit.color
			# dlg.eventedit.listWidget

			self.PAPA.data[index]={
				"name":name,
				"begin":begin,
				"end":end,
				"description":description,
				"color":color
			}

			self.updateView()

	def eventAdd(self):
		dlg=EventEditDialog(self.PAPA)
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

			self.PAPA.data.append(event)

			self.updateView()

###################################################################################################

# Mainwidow

class MainWindow(DongliTeahouseMainWindow):
	def __init__(self, app):
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

	def saveData(self):
		super().saveData()

		Fernet_Encrypt_Save(self.password(),self.data,"./LifeTimelime.dlcw")
	
	def SaveAllEncryptData(self):
		super().SaveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("lifespan",Fernet_Encrypt(self.password(),self.lifespan))
		self.UserSetting().setValue("birthday",Fernet_Encrypt(self.password(),QDate_to_Str(self.birthday)))
	
	def setting(self):
		dlg=SettingDialog(self)
		dlg.exec_()