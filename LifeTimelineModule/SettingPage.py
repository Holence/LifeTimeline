from DTPySide import *

from LifeTimelineSession.MainSession import MainSession
from LifeTimelineModule.Ui_SettingPage import Ui_SettingPage
class SettingPage(Ui_SettingPage,QStackedWidget):
	def __init__(self, Headquarter: MainSession):
		super().__init__(Headquarter)
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
		self.Headquarter.UserSetting().setValue("lifespan",Symmetric_Encrypt(self.Headquarter.password(), self.Headquarter.lifespan, iteration=self.Headquarter.iteration()))
		self.Headquarter.LifeWeekChart.updateView()
	
	def setBirthday(self):
		self.Headquarter.birthday=self.dateEdit_birthday.date()
		self.Headquarter.UserSetting().setValue("birthday",Symmetric_Encrypt(self.Headquarter.password(), self.birthday.toString("yyyyMMdd"), iteration=self.Headquarter.iteration()))
		self.Headquarter.LifeWeekChart.updateView()
	
	def setCubeWidth(self):
		self.Headquarter.cubewidth=self.spinBox_cubewidth.value()
		self.Headquarter.UserSetting().setValue("cubewidth",Symmetric_Encrypt(self.Headquarter.password(), self.Headquarter.cubewidth, iteration=self.Headquarter.iteration()))
		self.Headquarter.LifeWeekChart.updateView()
