from DTPySide import *


from LifeTimelineModule.SettingPage import SettingPage
class SettingSession(DTSession.DTSettingSession):
	def __init__(self,Headquarter,app):
		super().__init__(Headquarter,app)

		self.SettingPages=SettingPage(Headquarter)

		MenuButton1=DTWidget.DTSettingButton(QIcon(":/icon/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)