from DTPySide import *

from LifeTimelineModule.Ui_SettingPage import Ui_SettingPage
class SettingPage(Ui_SettingPage,QStackedWidget):
	def __init__(self,Headquarter):
		super().__init__(Headquarter)
		self.setupUi(self)
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)

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
