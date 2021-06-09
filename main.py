from LifeTimelineModule import *

app=DongliTeahouseAPP([])

app.setApplicationName("Life Timeline")
app.setAuthor("Holence")
app.setApplicationVersion("0.0.0.0")

window=MainWindow(app)
app.setMainWindow(window)

app.run()