from PySide6.QtCore import QCoreApplication, QRect
from PySide6.QtGui import QAction, QGuiApplication
from PySide6.QtWidgets import QWidget, QMenu, QMenuBar
import resource

VERSION = u"Code Vein II Character Builder v0.0.1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(960, 540)

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
        self.add_menu_bar(MainWindow)
        self.retranslateUi(MainWindow)

    def add_menu_bar(self, MainWindow):
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 960, 21))
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)

        # window submenu
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menubar.addAction(self.menuWindow.menuAction())

        self.menuSize = QMenu(self.menuWindow)
        self.menuSize.setObjectName(u"menuSize")
        self.menuWindow.addAction(self.menuSize.menuAction())

        self.action960x540 = QAction(MainWindow)
        self.action960x540.setObjectName(u"action_resize_window_960x540")
        self.action1440x810 = QAction(MainWindow)
        self.action1440x810.setObjectName(u"action_resize_window_1440x810")
        self.action1920x1080 = QAction(MainWindow)
        self.action1920x1080.setObjectName(u"action_resize_window_1920x1080")
        self.action2880x1620 = QAction(MainWindow)
        self.action2880x1620.setObjectName(u"action_resize_window_2880x1620")
        self.action3840x2160 = QAction(MainWindow)
        self.action3840x2160.setObjectName(u"action_resize_window_3840x2160")

        self.action960x540.setCheckable(True)
        self.action960x540.setChecked(True)
        self.action1440x810.setCheckable(True)
        self.action1920x1080.setCheckable(True)
        self.action2880x1620.setCheckable(True)
        self.action3840x2160.setCheckable(True)

        self.action960x540.triggered.connect(self.resize_window)
        self.action1440x810.triggered.connect(self.resize_window)
        self.action1920x1080.triggered.connect(self.resize_window)
        self.action2880x1620.triggered.connect(self.resize_window)
        self.action3840x2160.triggered.connect(self.resize_window)

        self.menuSize.addAction(self.action960x540)
        self.menuSize.addAction(self.action1440x810)
        self.menuSize.addAction(self.action1920x1080)
        self.menuSize.addAction(self.action2880x1620)
        self.menuSize.addAction(self.action3840x2160)

        self.disable_unsupported_window_size()

    def resize_window(self):
        width, height = self.sender().text().split("x")
        width, height = int(width), int(height)

        # availableGeometry() - excludes taskbar - returns height = 1040
        # geometry() - includes taskbar - returns height = 1080
        screen_rectangle = QGuiApplication.primaryScreen().availableGeometry()

        if screen_rectangle.width() < width:
            return
        if screen_rectangle.height() < height:
            return

        self.window().setFixedSize(width, height)
        self.center_window()

        for action in self.findChildren(QAction):
            if "action_resize_window_" in action.objectName():
                action.setChecked(False)
        self.sender().setChecked(True)

    def center_window(self):
        screen_center = QGuiApplication.primaryScreen().availableGeometry().center()
        window_rectangle = self.frameGeometry()
        window_rectangle.moveCenter(screen_center)
        self.move(window_rectangle.topLeft())

    def disable_unsupported_window_size(self):
        screen_rectangle = QGuiApplication.primaryScreen().availableGeometry()

        for action in self.findChildren(QAction):
            if "action_resize_window_" in action.objectName():
                size = action.objectName().replace("action_resize_window_", "")
                width, height = size.split("x")
                width, height = int(width), int(height)

                if screen_rectangle.width() < width:
                    action.setEnabled(False)
                if screen_rectangle.height() < height:
                    action.setEnabled(False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", VERSION, None))

        # menu
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuSize.setTitle(QCoreApplication.translate("MainWindow", u"Size", None))
        self.action960x540.setText(QCoreApplication.translate("MainWindow", u"960x540", None))
        self.action1440x810.setText(QCoreApplication.translate("MainWindow", u"1440x810", None))
        self.action1920x1080.setText(QCoreApplication.translate("MainWindow", u"1920x1080", None))
        self.action2880x1620.setText(QCoreApplication.translate("MainWindow", u"2880x1620", None))
        self.action3840x2160.setText(QCoreApplication.translate("MainWindow", u"3840x2160", None))
