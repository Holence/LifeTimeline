from DongliTeahousePySideWheel.DongliTeahouseTemplate import *

from Ui_ModuleSetting import Ui_ModuleSetting
class ModuleSetting(Ui_ModuleSetting,QWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)

		self.spinBox.setValue(parent.lifespan)
		self.dateEdit.setDate(parent.birthday)

		self.pushButton_page1.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
		self.pushButton_page2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

from Ui_ModuleEventEdit import Ui_ModuleEventEdit
class ModuleEventEdit(Ui_ModuleEventEdit,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.color="#FFFFFF"
		
		self.pushButton_color.clicked.connect(self.setColor)
	
	def setColor(self):
		color = QColorDialog.getColor(Qt.red, self)
		if color.isValid():
			self.color=color.name()

from Ui_ModuleLifeTimeLine import Ui_ModuleLifeTimeline
class ModuleLifeTimeline(Ui_ModuleLifeTimeline,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.parent=parent

		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):
		self.splitter.setStretchFactor(0,3)
		self.splitter.setStretchFactor(1,2)
		
		self.scene=QGraphicsScene()
		self.graphicsView.setScene(self.scene)
		self.updateView()
	
	def initializeSignal(self):
		self.actionAdd_Event.triggered.connect(self.eventAdd)
		self.addAction(self.actionAdd_Event)

		self.parent.addActionToMainMenu(self.actionAdd_Event)
		self.parent.addSeparatorToMainMenu()

	def updateView(self):
		self.scene.clear()

		now=self.parent.birthday
		for i in range(self.parent.lifespan):
			for j in range(52):
				
				colorList=[]
				for event in self.parent.data:
					if QDate_to_Str(now) >= event["begin"] and QDate_to_Str(now) <= event["end"]:
						colorList.append(event["color"])
				
				temp=WeekCube(self.parent.birthday,now,colorList,self)
				self.scene.addItem(temp)

				now=now.addDays(7)
	
	def eventAdd(self):
		dlg=DialogEventEdit(self.parent)
		if dlg.exec_():
			begin=QDate_to_Str(dlg.eventedit.dateEdit_begin.date())
			end=QDate_to_Str(dlg.eventedit.dateEdit_end.date())
			description=dlg.eventedit.plainTextEdit.toPlainText()
			color=dlg.eventedit.color

			event={
				"begin":begin,
				"end":end,
				"description":description,
				"color":color
			}

			self.parent.data.append(event)

			self.updateView()


###############################################################################################################
###############################################################################################################
###############################################################################################################

class DialogSetting(DongliTeahouseDialog):
	def __init__(self, parent):
		super().__init__(parent, "Settings")
		self.setting=ModuleSetting(parent)
		self.centralWidget.addWidget(self.setting)

class DialogEventEdit(DongliTeahouseDialog):
	def __init__(self, parent):
		super().__init__(parent,"Add New Event")
		self.eventedit=ModuleEventEdit(self)
		self.centralWidget.addWidget(self.eventedit)


class MainWindow(DongliTeahouseMainWindow):
	def __init__(self):
		self.password="123456"
		super().__init__()
		self.setWindowTitle("Life Timeline")
		self.setMetaData("Life Timeline")

	def initializeWindow(self):
		super().initializeWindow()

		self.lifetimeline=ModuleLifeTimeline(self)
		self.setCentralWidget(self.lifetimeline)
	
	def dataLoad(self):
		if os.path.exists("./LifeTimelime.dlcw"):
			self.data=Fernet_Decrypt_Load(self.password,"./LifeTimelime.dlcw")
		else:
			self.data=[]
			Fernet_Encrypt_Save(self.password,self.data,"./LifeTimelime.dlcw")

		self.settings=QSettings("settings.ini",QSettings.IniFormat)
		try:
			self.lifespan=int(Fernet_Decrypt(self.password,self.settings.value("lifespan")))
			if self.lifespan==0:
				self.lifespan=150
		except:
			self.lifespan=150
		
		try:
			birthday=Fernet_Decrypt(self.password,self.settings.value("birthday"))
			self.birthday=QDate(int(birthday[:4]),int(birthday[4:6]),int(birthday[6:8]))
		except:
			self.birthday=QDate(1970,1,1)
		
		# print(self.lifespan,self.birthday)
		# print(self.data)
	
	def dataSave(self):
		Fernet_Encrypt_Save(self.password,self.data,"./LifeTimelime.dlcw")
		self.settings.setValue("lifespan",Fernet_Encrypt(self.password,self.lifespan))
		self.settings.setValue("birthday",Fernet_Encrypt(self.password,QDate_to_Str(self.birthday)))
	
	def setting(self):
		dlg=DialogSetting(self)
		if dlg.exec_():
			self.birthday=dlg.setting.dateEdit.date()
			self.lifespan=dlg.setting.spinBox.value()
			self.lifetimeline.updateView()