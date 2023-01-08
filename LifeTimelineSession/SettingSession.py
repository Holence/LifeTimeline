from DTPySide import *

from LifeTimelineSession.MainSession import MainSession
class SettingSession(DTSession.DTSettingSession):
	def __init__(self, Headquarter: MainSession, app):
		super().__init__(Headquarter, app)

		from LifeTimelineModule.SettingPage import SettingPage
		self.SettingPages=SettingPage(Headquarter)

		MenuButton1=DTWidget.DTSettingButton(IconFromCurrentTheme("menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)