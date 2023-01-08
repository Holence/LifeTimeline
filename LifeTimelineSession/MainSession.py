from DTPySide import *

class MainSession(DTSession.DTMainSession):
	def __init__(self,app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		from LifeTimelineModule.LifeWeekChart import LifeWeekChart
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
		
		if os.path.exists(data_dir):
			self.data=Symmetric_Decrypt_Load(self.password(), data_dir, iteration=self.iteration())
			if self.data==False:
				DTFrame.DTMessageBox(self,"Error", "Data Error!")
				self.app.quit()
		else:
			self.data=[]
			Symmetric_Encrypt_Save(self.password(), self.data, data_dir, iteration=self.iteration())

		try:
			self.lifespan=int(Symmetric_Decrypt(self.password(), self.UserSetting().value("lifespan"), iteration=self.iteration()))
			if self.lifespan==0:
				self.lifespan=150
		except:
			self.lifespan=150
		
		try:
			birthday=Symmetric_Decrypt(self.password(), self.UserSetting().value("birthday"), iteration=self.iteration())
			self.birthday=QDate().fromString(birthday,"yyyyMMdd")
		except:
			self.birthday=QDate(1970,1,1)

		try:
			self.cubewidth=int(Symmetric_Decrypt(self.password(), self.UserSetting().value("cubewidth"), iteration=self.iteration()))
			if self.cubewidth==0:
				self.cubewidth=20
		except:
			self.cubewidth=20


	def saveData(self):
		super().saveData()
		
		Symmetric_Encrypt_Save(self.password(), self.data,os.path.join(self.app.DataDir(),"LifeTimelime.dlcw"), iteration=self.iteration())
	
	def saveAllEncryptData(self):
		super().saveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("lifespan", Symmetric_Encrypt(self.password(), self.lifespan, iteration=self.iteration()))
		self.UserSetting().setValue("birthday", Symmetric_Encrypt(self.password(), self.birthday.toString("yyyyMMdd"), iteration=self.iteration()))
		self.UserSetting().setValue("cubewidth", Symmetric_Encrypt(self.password(), self.cubewidth, iteration=self.iteration()))
	
	def setting(self):
		from LifeTimelineSession.SettingSession import SettingSession
		dlg=SettingSession(self,self.app)
		dlg.exec_()