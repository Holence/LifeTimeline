from DongliTeahousePySideWheel.DongliTeahouseTemplate import *

from Ui_ModuleSettingPage import Ui_ModuleSettingPage
class SettingPageModule(Ui_ModuleSettingPage,QStackedWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.parent=parent
		self.spinBox_lifespan.setValue(parent.lifespan)
		self.pushButton_lifespan.clicked.connect(self.setLifespan)

		self.dateEdit_birthday.setDate(parent.birthday)
		self.pushButton_birthday.clicked.connect(self.setBirthday)
	
	def setLifespan(self):
		self.parent.lifespan=self.spinBox_lifespan.value()
		self.parent.UserSetting.setValue("lifespan",Fernet_Encrypt(self.parent.password(),self.parent.lifespan))
		self.parent.lifetimeline.updateView()
	
	def setBirthday(self):
		self.parent.birthday=self.dateEdit_birthday.date()
		self.parent.UserSetting.setValue("birthday",Fernet_Encrypt(self.parent.password(),QDate_to_Str(self.parent.birthday)))
		self.parent.lifetimeline.updateView()

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
		dlg=EventEditDialog(self.parent)
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

class SettingDialog(DongliTeahouseSettingDialog):
	def __init__(self, parent):
		super().__init__(parent)

		self.SettingPages=SettingPageModule(parent)

		MenuButton1=DongliTeahouseSettingButton(QIcon(":/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)

class EventEditDialog(DongliTeahouseDialog):
	def __init__(self, parent):
		super().__init__(parent,"Add New Event")
		self.eventedit=ModuleEventEdit(self)
		self.centralWidget.addWidget(self.eventedit)
	
	def accept(self):
		if self.eventedit.dateEdit_begin.date()>=self.eventedit.dateEdit_end.date():
			DongliTeahouseMessageBox(self,"Warning","Wrong Date Range!",DongliTeahouseMessageIcon.Warning())
		else:
			super().accept()


class MainWindow(DongliTeahouseMainWindow):
	def __init__(self, app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		self.lifetimeline=ModuleLifeTimeline(self)
		self.setCentralWidget(self.lifetimeline)

	
	def dataLoad(self):
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
			self.lifespan=int(Fernet_Decrypt(self.password(),self.UserSetting.value("lifespan")))
			if self.lifespan==0:
				self.lifespan=150
		except:
			self.lifespan=150
		
		try:
			birthday=Fernet_Decrypt(self.password(),self.UserSetting.value("birthday"))
			self.birthday=QDate(int(birthday[:4]),int(birthday[4:6]),int(birthday[6:8]))
		except:
			self.birthday=QDate(1970,1,1)


	def dataSave(self):
		Fernet_Encrypt_Save(self.password(),self.data,"./LifeTimelime.dlcw")
		
	
	def UserSettingSave(self):
		super().UserSettingSave()
		self.UserSetting.setValue("lifespan",Fernet_Encrypt(self.password(),self.lifespan))
		self.UserSetting.setValue("birthday",Fernet_Encrypt(self.password(),QDate_to_Str(self.birthday)))

	
	def setting(self):
		dlg=SettingDialog(self)
		dlg.exec_()