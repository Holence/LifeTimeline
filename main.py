from DongliTeahousePySideWheel.DongliTeahousePalette import *
from MyComponent import *

app=QApplication(sys.argv)

app.setStyle("Fusion")
app.setPalette(MyDarkPalette())
app.setQuitOnLastWindowClosed(False)

window=MainWindow()
window.quitApp.connect(app.quit)

sys.exit(app.exec_())