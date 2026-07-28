from PySide6.QtCore import QCoreApplication, QRect, Qt
from PySide6.QtGui import QAction, QGuiApplication
from PySide6.QtWidgets import QWidget, QMenu, QMenuBar, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSpacerItem, \
    QSizePolicy, QToolButton, QPushButton, QProgressBar
import resource

VERSION = u"Code Vein II Character Builder v0.0.1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1440, 810 + 21) # menu size

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"""
                #centralwidget {
                    border-image: url(:/background/Background960.png) 0 0 0 0 stretch stretch;
                    background: black;
                }

                QLabel {
                    color: white;
                }

                QToolButton {
                    color: white;
                    border: none;
                    background: transparent;
                }

                QPushButton {
                    color: white;
                    border: none;
                    background: transparent;
                }
            """)

        # main vertical layout
        self.main_vertical_layout_widget = QWidget(self.centralwidget)
        self.main_vertical_layout_widget.setObjectName(u"main_vertical_layout_widget")
        self.main_vertical_layout_widget.setGeometry(QRect(0, 0, 960, 810))
        self.main_vertical_layout = QVBoxLayout(self.main_vertical_layout_widget)
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.main_vertical_layout.setContentsMargins(0, 0, 0, 0)

        # 1st horizontal layout
        self.main_horizontal_layout_1 = QHBoxLayout()
        self.main_horizontal_layout_1.setObjectName(u"main_horizontal_layout_1")
        self.main_horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_1)

        # 1st horizontal layout content
        self.label_h1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_1.setObjectName(u"label_h1_1")
        self.label_h1_1.setText(QCoreApplication.translate("MainWindow", u"Attack", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_1)

        # self.horizontal_spacer_h1_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_1)

        self.label_h1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_2.setObjectName(u"label_h1_2")
        self.label_h1_2.setText(QCoreApplication.translate("MainWindow", u"Max Ichor", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_2)

        # self.horizontal_spacer_h1_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_2)

        self.label_h1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_3.setObjectName(u"label_h1_3")
        self.label_h1_3.setText(QCoreApplication.translate("MainWindow", u"Partner", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_3)

        # 3rd horizontal layout
        self.main_horizontal_layout_3 = QHBoxLayout()
        self.main_horizontal_layout_3.setObjectName(u"main_horizontal_layout_3")
        self.main_horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_3)

        # 3rd horizontal layout content - grid layout 1
        self.grid_layout_h3_1 = QGridLayout()
        self.grid_layout_h3_1.setObjectName(u"grid_layout_h3_1")
        self.main_horizontal_layout_3.addLayout(self.grid_layout_h3_1)

        # 3rd horizontal layout content - grid layout 1 content
        self.tool_button_h3_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_1.setObjectName(u"tool_button_h3_1")
        self.tool_button_h3_1.setText(QCoreApplication.translate("MainWindow", u"Dodge Effectiveness", None)) # move to re-translate
        self.tool_button_h3_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_1, 0, 0, 1, 1)

        self.tool_button_h3_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_2.setObjectName(u"tool_button_h3_2")
        self.tool_button_h3_2.setText(QCoreApplication.translate("MainWindow", u"Quick", None)) # move to re-translate
        self.tool_button_h3_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tool_button_h3_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_3.setObjectName(u"tool_button_h3_3")
        self.tool_button_h3_3.setText(QCoreApplication.translate("MainWindow", u"Defensive Formae", None)) # move to re-translate
        self.tool_button_h3_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_3, 2, 0, 1, 1)

        self.tool_button_h3_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_4.setObjectName(u"tool_button_h3_4")
        self.tool_button_h3_4.setText(QCoreApplication.translate("MainWindow", u"30", None)) # move to re-translate
        self.tool_button_h3_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_4, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        # 3rd horizontal layout content - vertical layout 1
        self.vertical_layout_h3_1 = QVBoxLayout()
        self.vertical_layout_h3_1.setObjectName(u"vertical_layout_h3_1")
        self.vertical_layout_h3_1.setContentsMargins(0, 0, 0, 0)
        self.main_horizontal_layout_3.addLayout(self.vertical_layout_h3_1)

        # 3rd horizontal layout content - vertical layout 1 content
        self.label_h3_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_1.setObjectName(u"label_h3_1")
        self.label_h3_1.setText(QCoreApplication.translate("MainWindow", u"Attributes & Burden", None)) # move to re-translate
        self.label_h3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout_h3_1.addWidget(self.label_h3_1)

        # 3rd horizontal layout content - vertical layout 1 content - grid layout 2
        self.grid_layout_h3_2 = QGridLayout()
        self.grid_layout_h3_2.setObjectName(u"grid_layout_h3_2")
        self.vertical_layout_h3_1.addLayout(self.grid_layout_h3_2)

        # 3rd horizontal layout content - vertical layout 1 content - spacer
        # self.horizontal_spacer_h3_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.vertical_layout_h3_1.addItem(self.horizontal_spacer_h3_1)

        # 3rd horizontal layout content - vertical layout 1 content - grid layout 2 content
        self.tool_button_h3_1 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_1.setObjectName(u"tool_button_h3_1")
        self.tool_button_h3_1.setText(QCoreApplication.translate("MainWindow", u"Strength", None)) # move to re-translate

        self.tool_button_h3_2 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_2.setObjectName(u"tool_button_h3_2")
        self.tool_button_h3_2.setText(QCoreApplication.translate("MainWindow", u"Dexterity", None)) # move to re-translate

        self.tool_button_h3_3 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_3.setObjectName(u"tool_button_h3_3")
        self.tool_button_h3_3.setText(QCoreApplication.translate("MainWindow", u"Mind", None)) # move to re-translate

        self.tool_button_h3_4 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_4.setObjectName(u"tool_button_h3_4")
        self.tool_button_h3_4.setText(QCoreApplication.translate("MainWindow", u"Willpower", None)) # move to re-translate

        self.tool_button_h3_5 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_5.setObjectName(u"tool_button_h3_5")
        self.tool_button_h3_5.setText(QCoreApplication.translate("MainWindow", u"Vitality", None)) # move to re-translate

        self.tool_button_h3_6 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_6.setObjectName(u"tool_button_h3_6")
        self.tool_button_h3_6.setText(QCoreApplication.translate("MainWindow", u"Fortitude", None)) # move to re-translate

        self.label_h3_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_1.setObjectName(u"label_h3_1")
        self.label_h3_1.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_2.setObjectName(u"label_h3_2")
        self.label_h3_2.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_3.setObjectName(u"label_h3_3")
        self.label_h3_3.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_4.setObjectName(u"label_h3_4")
        self.label_h3_4.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_5.setObjectName(u"label_h3_5")
        self.label_h3_5.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_6.setObjectName(u"label_h3_6")
        self.label_h3_6.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_1 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_1.setObjectName(u"progress_bar_h3_1")
        self.progress_bar_h3_1.setValue(24)
        self.progress_bar_h3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_2 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_2.setObjectName(u"progress_bar_h3_2")
        self.progress_bar_h3_2.setValue(24)
        self.progress_bar_h3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_3 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_3.setObjectName(u"progress_bar_h3_3")
        self.progress_bar_h3_3.setValue(24)
        self.progress_bar_h3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_4 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_4.setObjectName(u"progress_bar_h3_4")
        self.progress_bar_h3_4.setValue(24)
        self.progress_bar_h3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_5 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_5.setObjectName(u"progress_bar_h3_5")
        self.progress_bar_h3_5.setValue(24)
        self.progress_bar_h3_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_6 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_6.setObjectName(u"progress_bar_h3_6")
        self.progress_bar_h3_6.setValue(24)
        self.progress_bar_h3_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_layout_h3_2.addWidget(self.tool_button_h3_1, 0, 0, 1, 1)
        self.grid_layout_h3_2.addWidget(self.tool_button_h3_2, 0, 1, 1, 1)
        self.grid_layout_h3_2.addWidget(self.tool_button_h3_3, 0, 2, 1, 1)
        self.grid_layout_h3_2.addWidget(self.tool_button_h3_4, 0, 3, 1, 1)
        self.grid_layout_h3_2.addWidget(self.tool_button_h3_5, 0, 4, 1, 1)
        self.grid_layout_h3_2.addWidget(self.tool_button_h3_6, 0, 5, 1, 1)

        self.grid_layout_h3_2.addWidget(self.label_h3_1, 1, 0, 1, 1)
        self.grid_layout_h3_2.addWidget(self.label_h3_2, 1, 1, 1, 1)
        self.grid_layout_h3_2.addWidget(self.label_h3_3, 1, 2, 1, 1)
        self.grid_layout_h3_2.addWidget(self.label_h3_4, 1, 3, 1, 1)
        self.grid_layout_h3_2.addWidget(self.label_h3_5, 1, 4, 1, 1)
        self.grid_layout_h3_2.addWidget(self.label_h3_6, 1, 5, 1, 1)

        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_1, 2, 0, 1, 1)
        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_2, 2, 1, 1, 1)
        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_3, 2, 2, 1, 1)
        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_4, 2, 3, 1, 1)
        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_5, 2, 4, 1, 1)
        self.grid_layout_h3_2.addWidget(self.progress_bar_h3_6, 2, 5, 1, 1)

        # 4th horizontal layout
        self.label_pre_h4 = QLabel(self.main_vertical_layout_widget)
        self.label_pre_h4.setObjectName(u"label_pre_h4")
        self.label_pre_h4.setText(QCoreApplication.translate("MainWindow", u"Defense", None)) # move to re-translate
        self.main_vertical_layout.addWidget(self.label_pre_h4)

        self.main_horizontal_layout_4 = QHBoxLayout()
        self.main_horizontal_layout_4.setObjectName(u"main_horizontal_layout_4")
        self.main_horizontal_layout_4.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_4)

        # # 4th horizontal layout content
        self.tool_button_h4_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_1.setObjectName(u"tool_button_h4_1")
        self.tool_button_h4_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_1)

        self.tool_button_h4_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_2.setObjectName(u"tool_button_h4_2")
        self.tool_button_h4_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_2)

        self.tool_button_h4_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_3.setObjectName(u"tool_button_h4_3")
        self.tool_button_h4_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_3)

        self.tool_button_h4_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_4.setObjectName(u"tool_button_h4_4")
        self.tool_button_h4_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_4)

        self.tool_button_h4_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_5.setObjectName(u"tool_button_h4_5")
        self.tool_button_h4_5.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_5)

        self.tool_button_h4_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_6.setObjectName(u"tool_button_h4_6")
        self.tool_button_h4_6.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_6)

        self.tool_button_h4_7 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_7.setObjectName(u"tool_button_h4_7")
        self.tool_button_h4_7.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_7)

        # 5th horizontal layout
        self.label_pre_h5 = QLabel(self.main_vertical_layout_widget)
        self.label_pre_h5.setObjectName(u"label_pre_h5")
        self.label_pre_h5.setText(QCoreApplication.translate("MainWindow", u"Guardian Defense", None)) # move to re-translate
        self.main_vertical_layout.addWidget(self.label_pre_h5)

        self.main_horizontal_layout_5 = QHBoxLayout()
        self.main_horizontal_layout_5.setObjectName(u"main_horizontal_layout_5")
        self.main_horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_5)

        # 5th horizontal layout content
        self.tool_button_h5_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_1.setObjectName(u"tool_button_h5_1")
        self.tool_button_h5_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_1)

        self.tool_button_h5_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_2.setObjectName(u"tool_button_h5_2")
        self.tool_button_h5_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_2)

        self.tool_button_h5_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_3.setObjectName(u"tool_button_h5_3")
        self.tool_button_h5_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_3)

        self.tool_button_h5_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_4.setObjectName(u"tool_button_h5_4")
        self.tool_button_h5_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_4)

        self.tool_button_h5_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_5.setObjectName(u"tool_button_h5_5")
        self.tool_button_h5_5.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_5)

        self.tool_button_h5_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_6.setObjectName(u"tool_button_h5_6")
        self.tool_button_h5_6.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_6)

        self.tool_button_h5_7 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_7.setObjectName(u"tool_button_h5_7")
        self.tool_button_h5_7.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_7)

        # 6th horizontal layout
        self.label_pre_h6 = QLabel(self.main_vertical_layout_widget)
        self.label_pre_h6.setObjectName(u"label_pre_h6")
        self.label_pre_h6.setText(QCoreApplication.translate("MainWindow", u"Resistances", None)) # move to re-translate
        self.main_vertical_layout.addWidget(self.label_pre_h6)

        self.main_horizontal_layout_6 = QHBoxLayout()
        self.main_horizontal_layout_6.setObjectName(u"main_horizontal_layout_6")
        self.main_horizontal_layout_6.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_6)

        # 6th horizontal layout content
        self.tool_button_h6_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_1.setObjectName(u"tool_button_h6_1")
        self.tool_button_h6_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_1)

        self.tool_button_h6_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_2.setObjectName(u"tool_button_h6_2")
        self.tool_button_h6_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_2)

        self.tool_button_h6_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_3.setObjectName(u"tool_button_h6_3")
        self.tool_button_h6_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_3)

        self.tool_button_h6_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_4.setObjectName(u"tool_button_h6_4")
        self.tool_button_h6_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_4)

        # dummy button
        self.tool_button_h6_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_5.setObjectName(u"tool_button_h6_5")
        self.tool_button_h6_5.setText(QCoreApplication.translate("MainWindow", u"", None)) # move to re-translate
        self.tool_button_h6_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_5)

        # dummy button
        self.tool_button_h6_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_6.setObjectName(u"tool_button_h6_6")
        self.tool_button_h6_6.setText(QCoreApplication.translate("MainWindow", u"", None)) # move to re-translate
        self.tool_button_h6_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_6)

        # dummy button
        self.tool_button_h6_7 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_7.setObjectName(u"tool_button_h6_7")
        self.tool_button_h6_7.setText(QCoreApplication.translate("MainWindow", u"", None)) # move to re-translate
        self.tool_button_h6_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_7)

        # end of setupUi
        MainWindow.setCentralWidget(self.centralwidget)
        self.add_menu_bar(MainWindow)
        self.retranslateUi(MainWindow)

    def add_menu_bar(self, MainWindow):
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1440, 21))
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
        self.action1440x810.setCheckable(True)
        self.action1440x810.setChecked(True)
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
