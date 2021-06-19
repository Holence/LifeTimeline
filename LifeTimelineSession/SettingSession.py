from DTPySide.DTFunction import *
from DTPySide.DTSession import DTSettingSession
from DTPySide.DTWidget import DTSettingButton

from LifeTimelineModule.SettingPage import SettingPage

class SettingSession(DTSettingSession):
	def __init__(self,Headquarter):
		super().__init__(Headquarter)

		self.SettingPages=SettingPage(Headquarter)

		MenuButton1=DTSettingButton(QIcon(":/icon/white/white_menu.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page)