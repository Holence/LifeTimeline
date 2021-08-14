from DTPySide import *
from LifeTimelineSession.MainSession import MainSession

app=DTAPP(sys.argv)

app.setApplicationName("Life Timeline")
app.setWindowIcon(DTIcon.HoloIcon2())
app.setAuthor("Holence")
app.setApplicationVersion("0.0.0.0")
app.setLoginEnable(True)

session=MainSession(app)
app.setMainSession(session)

# app.debugRun("123",True)
app.run()