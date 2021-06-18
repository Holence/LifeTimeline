from DongliTeahousePySideWheel import *
from LifeTimelineModule.SettingPage import SettingPage

class SettingSession(DongliTeahouseSession.DongliTeahouseSettingSession):
	def __init__(self,Headquarter):
		super().__init__(Headquarter)

		self.SettingPages=SettingPage(Headquarter)

		MenuButton1=DongliTeahouseWidget.DongliTeahouseSettingButton(QIcon(":/icon/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)