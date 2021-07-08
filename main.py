from DTPySide import *
from LifeTimelineSession.MainSession import MainSession

app=DTAPP([])

app.setApplicationName("Life Timeline")
app.setAuthor("Holence")
app.setApplicationVersion("0.0.0.0")
app.setWindowIcon(DTIcon.Holo2())

session=MainSession(app)
app.setMainSession(session)

# app.debugRun("123",True)
app.run()