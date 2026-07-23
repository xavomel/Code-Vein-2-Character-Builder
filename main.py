from PySide6.QtWidgets import QApplication, QMainWindow
import builder_ui

class MainWindow(QMainWindow, builder_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication([])
    form = MainWindow()
    form.show()
    app.exec()
    

main()
