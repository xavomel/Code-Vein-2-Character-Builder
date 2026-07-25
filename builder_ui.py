from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget
import resource


VERSION = u"Code Vein II Character Builder v0.0.1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"""
                #centralwidget {
                    border-image: url(:/background/Background960.png) 0 0 0 0 stretch stretch;
                    background: black;
                }
            """)

        # end of setupUi
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", VERSION, None))
