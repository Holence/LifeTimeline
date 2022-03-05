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

		data_dir=os.path.join(self.app.DataDir(),"LifeTimelime.dlcw")
		print(data_dir)
		if os.path.exists(data_dir):
			self.data=Fernet_Decrypt_Load(self.password(), data_dir)
			if self.data==False:
				DTFrame.DTMessageBox(self,"Error", "Data Error!")
				self.app.quit()
		else:
			self.data=[]
			Fernet_Encrypt_Save(self.password(), self.data, data_dir)

		try:
			self.lifespan=int(Fernet_Decrypt(self.password(),self.UserSetting().value("lifespan")))
			if self.lifespan==0:
				self.lifespan=150
		except:
			self.lifespan=150
		
		try:
			birthday=Fernet_Decrypt(self.password(),self.UserSetting().value("birthday"))
			self.birthday=QDate().fromString(birthday,"yyyyMMdd")
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
		
		Fernet_Encrypt_Save(self.password(),self.data,os.path.join(self.app.DataDir(),"LifeTimelime.dlcw"))
	
	def saveAllEncryptData(self):
		super().saveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("lifespan",Fernet_Encrypt(self.password(),self.lifespan))
		self.UserSetting().setValue("birthday",Fernet_Encrypt(self.password(),self.birthday.toString("yyyyMMdd")))
		self.UserSetting().setValue("cubewidth",Fernet_Encrypt(self.password(),self.cubewidth))
	
	def setting(self):
		dlg=SettingSession(self,self.app)
		dlg.exec_()