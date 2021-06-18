from DongliTeahousePySideWheel import DongliTeahouseAPP
from LifeTimelineSession.MainSession import MainSession

app=DongliTeahouseAPP([])

app.setApplicationName("Life Timeline")
app.setAuthor("Holence")
app.setApplicationVersion("0.0.0.0")

session=MainSession(app)
app.setMainSession(session)

# app.debugRun("123",True)
app.run()