from DTPySide import *

from LifeTimelineSession.SettingSession import SettingSession
from LifeTimelineModule.LifeWeekChart import LifeWeekChart

class MainSession(DTSession.DTMainSession):
	def __init__(self,app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		self.LifeWeekChart=LifeWeekChart(self)
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
				DTFrame.DTMessageBox(self,"Error","Data Error!")
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
		dlg=SettingSession(self,self.app)
		dlg.exec_()