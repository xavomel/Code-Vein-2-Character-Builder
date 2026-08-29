from PySide6.QtCore import QCoreApplication, QRect, Qt, QSize, QDir, QPointF
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QFont, QFontDatabase, \
    QPainter, QPen, QColor, QPolygonF, QPixmap
from PySide6.QtWidgets import QWidget, QMenu, QMenuBar, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSpacerItem, \
    QSizePolicy, QToolButton, QPushButton, QProgressBar, QApplication, QListView, QListWidget, QListWidgetItem, \
    QAbstractScrollArea, QTextEdit, QInputDialog, QMessageBox, QFileDialog, QLineEdit
import warnings
import cv2_resources
from game_data_classes import *
from utility import escape_filename
import re


VERSION = u"Code Vein II Character Builder v0.0.1"


class Ui_MainWindow(object):
    def placeDynamicUIElements(self):
        # widgets in layout have position only after window is shown
        # if we want to place a widget outside layout, but matching position of widget in layout
        # then we can only do so after window is shown

        # get source widget dimensions and create dynamic element in same place
        # weapon 1 transform
        wp1_geo = self.tool_button_h2_v1_h1_1.geometry()
        self.tool_button_h2_v1_h1_1a.setGeometry(QRect(wp1_geo.x(), wp1_geo.y(), 25, 25))
        self.tool_button_h2_v1_h1_1a.raise_()
        self.tool_button_h2_v1_h1_1a.show()

        # weapon 2 transform
        wp2_geo = self.tool_button_h2_v2_h1_1.geometry()
        self.tool_button_h2_v2_h1_1a.setGeometry(QRect(wp2_geo.x(), wp2_geo.y(), 25, 25))
        self.tool_button_h2_v2_h1_1a.raise_()
        self.tool_button_h2_v2_h1_1a.show()

        # defensive transform
        def_geo = self.tool_button_h2_v3_h1_2.geometry()
        self.tool_button_h2_v3_h1_2a.setGeometry(QRect(def_geo.x(), def_geo.y(), 25, 25))
        self.tool_button_h2_v3_h1_2a.raise_()
        self.tool_button_h2_v3_h1_2a.show()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1440, 810 + 21) # menu size

        # fonts
        # TODO: after testing remove unnecessary fonts from directory
        font_directory = "Fonts/"
        db = QFontDatabase()
        for fi in QDir(font_directory).entryInfoList(["*.ttf"]):
            db.addApplicationFont(fi.absoluteFilePath())

        # fonts - default (Cabin from Fonts directory)
        font_default = QFont()
        font_default.setFamily(u"Cabin")
        QApplication.setFont(font_default, "QLabel")
        QApplication.setFont(font_default, "MyQPushButton")
        QApplication.setFont(font_default, "MyQToolButton")

        # fonts - specific uses
        # TODO move to retranslateUI ? different fonts for different languages
        self.font_numbers_bleed = db.font("Pirata One", "Regular", 9)
        self.font_numbers_attribute = db.font("Science Gothic", "ExtraLight", 20)
        self.font_numbers_progress_bar = db.font("Science Gothic", "ExtraLight", 10)
        self.font_numbers_defense = db.font("Science Gothic", "Regular", 10)
        self.font_defensive_formae = db.font("Pirata One", "Regular", 28)

        # icons
        icon_slot_blood_code_size = QSize(150, 150)
        icon_slot_item_size = QSize(75, 75)
        icon_slot_item_addon_size = QSize(24, 24)
        icon_slot_forma_size = QSize(30, 30)
        icon_attribute_size = QSize(24, 24)
        icon_defense_size = QSize(24, 24)
        icon_side_menu_button_size = QSize(24, 32)
        icon_side_menu_content_size = QSize(70, 70)

        icon_slot_blood_code = QIcon()
        icon_slot_blood_code.addFile(u":/All/UI/Slot_Blood_Code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_slot_item = QIcon()
        icon_slot_item.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_slot_item_addon = QIcon()
        icon_slot_item_addon.addFile(u":/All/Transform/Transform_Off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_slot_forma = QIcon()
        icon_slot_forma.addFile(u":/All/UI/Slot_Forma", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_attribute_strength = QIcon()
        icon_attribute_strength.addFile(u":/All/UI/Attribute_Strength.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_dexterity = QIcon()
        icon_attribute_dexterity.addFile(u":/All/UI/Attribute_Dexterity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_mind = QIcon()
        icon_attribute_mind.addFile(u":/All/UI/Attribute_Mind", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_willpower = QIcon()
        icon_attribute_willpower.addFile(u":/All/UI/Attribute_Willpower.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_vitality = QIcon()
        icon_attribute_vitality.addFile(u":/All/UI/Attribute_Vitality.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_fortitude = QIcon()
        icon_attribute_fortitude.addFile(u":/All/UI/Attribute_Fortitude.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_defense_slash = QIcon()
        icon_defense_slash.addFile(u":/All/UI/Defense_Slash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_crush = QIcon()
        icon_defense_crush.addFile(u":/All/UI/Defense_Crush.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_pierce = QIcon()
        icon_defense_pierce.addFile(u":/All/UI/Defense_Pierce", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_blood = QIcon()
        icon_defense_blood.addFile(u":/All/UI/Defense_Blood.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_fire = QIcon()
        icon_defense_fire.addFile(u":/All/UI/Defense_Fire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_ice = QIcon()
        icon_defense_ice.addFile(u":/All/UI/Defense_Ice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_thunder = QIcon()
        icon_defense_thunder.addFile(u":/All/UI/Defense_Thunder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_resistance_disease = QIcon()
        icon_resistance_disease.addFile(u":/All/UI/Resistance_Disease.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_wound = QIcon()
        icon_resistance_wound.addFile(u":/All/UI/Resistance_Wound.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_bleed = QIcon()
        icon_resistance_bleed.addFile(u":/All/UI/Resistance_Bleed", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_curse = QIcon()
        icon_resistance_curse.addFile(u":/All/UI/Resistance_Curse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_text_arrow = QIcon()
        icon_text_arrow.addFile(u":/All/UI/Text_Arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"""
                #centralwidget {
                    border-image: url(:/All/UI/Background1440.png) 0 0 0 0 stretch stretch;
                    background: black;
                }

                QListWidget {
                    border: none;
                    background: transparent;
                }

                QLabel, QListWidget::item {
                    color: #c2c2c2; /*light grey*/
                }

                MyQToolButton, QTextEdit {
                    color: #c2c2c2; /*light grey*/
                    border: none;
                    background: transparent;
                }

                MyQPushButton {
                    color: #c2c2c2; /*light grey*/
                    border: none;
                    background: transparent;
                }

                #Weapon_1_Forma_1:hover, #Weapon_1_Forma_2:hover, #Weapon_1_Forma_3:hover, #Weapon_1_Forma_4:hover,
                #Weapon_2_Forma_1:hover, #Weapon_2_Forma_2:hover, #Weapon_2_Forma_3:hover, #Weapon_2_Forma_4:hover,
                #Booster_1_Button:hover, #Booster_2_Button:hover, #Booster_3_Button:hover,
                #Booster_4_Button:hover, #Booster_5_Button:hover, #Booster_6_Button:hover {
                    border : 1px solid #c2c2c2; /*light grey*/
                }

                #tool_button_h3_v1_g1_1, #tool_button_h3_v1_g1_2, #tool_button_h3_v1_g1_3, #tool_button_h3_v1_g1_4,
                #tool_button_h3_v1_g1_5, #tool_button_h3_v1_g1_6,
                #label_h3_v1_1,
                #tool_button_h3_g1_1, #tool_button_h3_g1_2, #tool_button_h3_g1_3, #tool_button_h3_g1_4,
                #label_h2_v3_h1_g1_1, #label_h2_v3_h1_g1_2, #label_h2_v3_h1_g1_3, #label_h2_v3_h1_g1_4,
                #label_h2_v3_h1_g1_5, #label_h2_v3_h1_g1_6, #label_h2_v3_h1_g1_7, #label_h2_v3_h1_g1_8,
                #label_h2_v1_h1_g1_1, #label_h2_v1_h1_g1_2, #label_h2_v1_h1_g1_3, #label_h2_v1_h1_g1_4,
                #label_h2_v1_h1_g1_5, #label_h2_v1_h1_g1_6, #label_h2_v1_h1_g1_7, #label_h2_v1_h1_g1_8,
                #label_h2_v1_h1_g1_9, #label_h2_v1_h1_g1_10, #label_h2_v1_h1_g1_11, #label_h2_v1_h1_g1_12,
                #label_h2_v1_h1_g1_13, #label_h2_v1_h1_g1_14, #label_h2_v1_h1_g1_15, #label_h2_v1_h1_g1_16,
                #label_h2_v2_h1_g1_1, #label_h2_v2_h1_g1_2, #label_h2_v2_h1_g1_3, #label_h2_v2_h1_g1_4,
                #label_h2_v2_h1_g1_5, #label_h2_v2_h1_g1_6, #label_h2_v2_h1_g1_7, #label_h2_v2_h1_g1_8,
                #label_h2_v2_h1_g1_9, #label_h2_v2_h1_g1_10, #label_h2_v2_h1_g1_11, #label_h2_v2_h1_g1_12,
                #label_h2_v2_h1_g1_13, #label_h2_v2_h1_g1_14, #label_h2_v2_h1_g1_15, #label_h2_v2_h1_g1_16 {
                    color: #b6a98d; /*light brown*/
                }

                #tool_button_pre_h6, #tool_button_h6_1, #tool_button_h6_2, #tool_button_h6_3, #tool_button_h6_4 {
                    color: #9d9deb; /*purple*/
                }

                #Weapon_1_Button, #Weapon_2_Button,
                #Offensive_Button, #Defensive_Button, #Jail_Button {
                    color: #abddea; /*cyan*/
                }

                #Blood_Code_Button:hover,
                #Weapon_1_Button:hover, #Weapon_2_Button:hover,
                #Offensive_Button:hover, #Defensive_Button:hover, #Jail_Button:hover,
                #Transform_Weapon_1_Button:hover, #Transform_Weapon_2_Button:hover, #Transform_Defensive_Button:hover {
                    border : 1px solid #b6a98d; /*light brown*/
                }

                #label_h1_2, #tool_button_h1_2 {
                    color: #afcbde; /*pale cyan*/
                }

                #label_h1_3, #tool_button_h1_3{
                    color: #00adf1; /*blue*/
                }

                #Blood_Code_Button,
                #label_h3_v1_g1_1, #label_h3_v1_g1_2, #label_h3_v1_g1_3, #label_h3_v1_g1_4, #label_h3_v1_g1_6,
                #label_h3_v1_g1_5,
                #tool_button_h4_1, #tool_button_h4_2, #tool_button_h4_3, #tool_button_h4_4, #tool_button_h4_5,
                #tool_button_h4_6, #tool_button_h4_7,
                #tool_button_h5_1, #tool_button_h5_2, #tool_button_h5_3, #tool_button_h5_4, #tool_button_h5_5,
                #tool_button_h5_6, #tool_button_h5_7 {
                    color: white
                }

                QScrollBar:vertical {
                    width: 10px;
                    background: transparent; /*does nothing but other css doesn't work without it*/
                }

                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: #95C2CE;
                    border: 4px solid #171717;
                }

                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    background: none;
                }

                QScrollBar::handle:vertical {
                    background: #95C2CE;
                }
            """)

        # side menu common
        self.margin_size = 24
        self.margin_size_overlapping = 0

        # side vertical layout 1
        self.side_vertical_layout_widget_1 = QWidget(self.centralwidget)
        self.side_vertical_layout_widget_1.setObjectName(u"side_vertical_layout_widget_1")
        side_vertical_layout_widget_1_width = 340
        self.side_vertical_layout_widget_1.setGeometry(QRect(1080, 0, side_vertical_layout_widget_1_width, 810))
        self.side_vertical_layout_1 = QVBoxLayout(self.side_vertical_layout_widget_1)
        self.side_vertical_layout_1.setObjectName(u"side_vertical_layout_1")
        self.side_vertical_layout_1.setContentsMargins(self.margin_size, self.margin_size, 0, self.margin_size_overlapping)
        self.side_vertical_layout_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # side vertical layout 1 content - list widget 1 - menu buttons
        self.selected_side_menu = {
            "Menu": "",
            "Count": 0
        }

        self.side_menu_buttons = MyQListWidget(self.centralwidget)
        self.side_menu_buttons.setObjectName(u"side_menu_buttons")
        self.side_menu_buttons.setFlow(QListView.LeftToRight)
        self.side_menu_buttons.setWrapping(True)
        self.side_menu_buttons.setMinimumWidth(side_vertical_layout_widget_1_width)
        self.side_menu_buttons.setMaximumWidth(side_vertical_layout_widget_1_width)
        self.side_menu_buttons.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.side_menu_buttons.setIconSize(icon_side_menu_button_size)
        self.side_vertical_layout_1.addWidget(self.side_menu_buttons)
        self.side_menu_buttons.setMouseTracking(True)

        # side vertical layout 2
        self.side_vertical_layout_widget_2 = QWidget(self.centralwidget)
        self.side_vertical_layout_widget_2.setObjectName(u"side_vertical_layout_widget_2")
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, self.margin_size, 360, 810 - self.margin_size))
        self.side_vertical_layout_2 = QVBoxLayout(self.side_vertical_layout_widget_2)
        self.side_vertical_layout_2.setObjectName(u"side_vertical_layout_2")
        self.side_vertical_layout_2.setContentsMargins(self.margin_size, self.margin_size_overlapping, self.margin_size, self.margin_size)
        self.side_vertical_layout_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # side vertical layout 2 content - list widget 2 - menu content
        self.side_menu_content = MyQListWidget(self.centralwidget)
        self.side_menu_content.setObjectName(u"side_menu_content")
        self.side_menu_content.setFlow(QListView.LeftToRight)
        self.side_menu_content.setWrapping(True)
        self.side_menu_content.setMinimumWidth(360 - 2 * self.margin_size)
        self.side_menu_content.setMaximumWidth(360 - 2 * self.margin_size)
        self.side_menu_content.setIconSize(icon_side_menu_content_size)
        self.side_menu_content.setGridSize(icon_side_menu_content_size)
        self.side_menu_content.setUniformItemSizes(True)
        self.side_vertical_layout_2.addWidget(self.side_menu_content)
        self.side_menu_content.setMouseTracking(True)

        self.side_menu_text = QTextEdit(self.centralwidget)
        self.side_menu_text.setObjectName(u"side_menu_text")
        self.side_menu_text.setReadOnly(True)
        self.side_menu_text.setMinimumWidth(360 - 2 * self.margin_size)
        self.side_menu_text.setMaximumWidth(360 - 2 * self.margin_size)
        self.side_menu_text.setMinimumHeight(360)
        self.side_menu_text.setMaximumHeight(360)
        self.side_vertical_layout_2.addWidget(self.side_menu_text)

        # main vertical layout
        self.main_vertical_layout_widget = QWidget(self.centralwidget)
        self.main_vertical_layout_widget.setObjectName(u"main_vertical_layout_widget")
        self.main_vertical_layout_widget.setGeometry(QRect(0, 0, 940, 810))
        self.main_vertical_layout = QVBoxLayout(self.main_vertical_layout_widget)
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.main_vertical_layout.setContentsMargins(self.margin_size, self.margin_size, self.margin_size, self.margin_size)

        # 1st horizontal layout
        self.main_horizontal_layout_1 = QHBoxLayout()
        self.main_horizontal_layout_1.setObjectName(u"main_horizontal_layout_1")
        self.main_horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_1)

        # 1st horizontal layout content
        self.tool_button_h1_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h1_1.setObjectName(u"tool_button_h1_1")
        self.tool_button_h1_1.setText(QCoreApplication.translate("MainWindow", u"Attack", None)) # move to re-translate
        self.tool_button_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_h1_1.setIcon(icon_text_arrow)
        self.main_horizontal_layout_1.addWidget(self.tool_button_h1_1)

        self.horizontal_spacer_h1_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_1)

        self.label_h1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_2.setObjectName(u"label_h1_2")
        self.label_h1_2.setText(QCoreApplication.translate("MainWindow", u"Max Ichor", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_2)

        self.tool_button_h1_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h1_2.setObjectName(u"tool_button_h1_2")
        self.tool_button_h1_2.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.main_horizontal_layout_1.addWidget(self.tool_button_h1_2)

        self.horizontal_spacer_h1_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_2)

        self.label_h1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_3.setObjectName(u"label_h1_3")
        # TODO
        #self.label_h1_3.setText(QCoreApplication.translate("MainWindow", u"Partner", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_3)

        self.tool_button_h1_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h1_3.setObjectName(u"tool_button_h1_3")
        # TODO
        #self.tool_button_h1_3.setText(QCoreApplication.translate("MainWindow", u"", None)) # move to re-translate
        self.tool_button_h1_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.main_horizontal_layout_1.addWidget(self.tool_button_h1_3)

        self.horizontal_spacer_h1_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_3)

        # 2nd horizontal layout
        self.main_horizontal_layout_2 = QHBoxLayout()
        self.main_horizontal_layout_2.setObjectName(u"main_horizontal_layout_2")
        self.main_horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_2)

        # 2nd horizontal layout content - vertical layout 1
        self.vertical_layout_h2_1 = QVBoxLayout()
        self.vertical_layout_h2_1.setObjectName(u"vertical_layout_h2_1")
        self.vertical_layout_h2_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_1)

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout
        self.horizontal_layout_h2_v1_1 = QHBoxLayout()
        self.horizontal_layout_h2_v1_1.setObjectName(u"horizontal_layout_h2_v1_1")
        self.horizontal_layout_h2_v1_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_1.addLayout(self.horizontal_layout_h2_v1_1)

        # 2nd horizontal layout content - vertical layout 1 content - buttons
        self.push_button_h2_v1_1 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_1.setObjectName(u"Weapon_1_Forma_1")
        self.push_button_h2_v1_1.setText(QCoreApplication.translate("MainWindow", u"Forma 1: None", None)) # move to re-translate
        self.push_button_h2_v1_1.setIcon(icon_slot_forma)
        self.push_button_h2_v1_1.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_1, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v1_1.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v1_1.set_button_type("Forma")

        self.push_button_h2_v1_2 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_2.setObjectName(u"Weapon_1_Forma_2")
        self.push_button_h2_v1_2.setText(QCoreApplication.translate("MainWindow", u"Forma 2: None", None)) # move to re-translate
        self.push_button_h2_v1_2.setIcon(icon_slot_forma)
        self.push_button_h2_v1_2.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_2, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v1_2.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v1_2.set_button_type("Forma")

        self.push_button_h2_v1_3 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_3.setObjectName(u"Weapon_1_Forma_3")
        self.push_button_h2_v1_3.setText(QCoreApplication.translate("MainWindow", u"Forma 3: None", None)) # move to re-translate
        self.push_button_h2_v1_3.setIcon(icon_slot_forma)
        self.push_button_h2_v1_3.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_3, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v1_3.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v1_3.set_button_type("Forma")

        self.push_button_h2_v1_4 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_4.setObjectName(u"Weapon_1_Forma_4")
        self.push_button_h2_v1_4.setText(QCoreApplication.translate("MainWindow", u"Forma 4: None", None)) # move to re-translate
        self.push_button_h2_v1_4.setIcon(icon_slot_forma)
        self.push_button_h2_v1_4.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_4, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v1_4.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v1_4.set_button_type("Forma")

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout content
        self.tool_button_h2_v1_h1_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v1_h1_1.setObjectName(u"Weapon_1_Button")
        self.tool_button_h2_v1_h1_1.setText(QCoreApplication.translate("MainWindow", u"Weapon 1", None)) # move to re-translate
        self.tool_button_h2_v1_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v1_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v1_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v1_1.addWidget(self.tool_button_h2_v1_h1_1)
        self.tool_button_h2_v1_h1_1.clicked.connect(self.fill_side_menu_weapon)
        self.tool_button_h2_v1_h1_1.set_button_type("Weapon")

        self.tool_button_h2_v1_h1_1a = MyQToolButton(self.centralwidget)
        self.tool_button_h2_v1_h1_1a.setObjectName(u"Transform_Weapon_1_Button")
        self.tool_button_h2_v1_h1_1a.setIcon(icon_slot_item_addon)
        self.tool_button_h2_v1_h1_1a.setIconSize(icon_slot_item_addon_size)
        self.tool_button_h2_v1_h1_1a.clicked.connect(self.fill_side_menu_transform)
        # self.tool_button_h2_v1_h1_1a.set_button_type("Transform")  # TODO

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout content - grid layout
        self.grid_layout_h2_v1_h1_1 = QGridLayout()
        self.grid_layout_h2_v1_h1_1.setObjectName(u"grid_layout_h2_v1_h1_1")
        self.grid_layout_h2_v1_h1_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.horizontal_layout_h2_v1_1.addLayout(self.grid_layout_h2_v1_h1_1)

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout content - grid layout content
        self.label_h2_v1_h1_g1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_1.setObjectName(u"label_h2_v1_h1_g1_1")
        self.label_h2_v1_h1_g1_1.setText(QCoreApplication.translate("MainWindow", u"Reliability ", None))  # move to re-translate

        self.label_h2_v1_h1_g1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_2.setObjectName(u"label_h2_v1_h1_g1_2")
        self.label_h2_v1_h1_g1_2.setText(QCoreApplication.translate("MainWindow", u"Handling ", None))  # move to re-translate

        self.label_h2_v1_h1_g1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_3.setObjectName(u"label_h2_v1_h1_g1_3")
        self.label_h2_v1_h1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Conversion ", None))  # move to re-translate

        self.label_h2_v1_h1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_4.setObjectName(u"label_h2_v1_h1_g1_4")
        self.label_h2_v1_h1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Conductivity ", None))  # move to re-translate

        self.label_h2_v1_h1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_5.setObjectName(u"label_h2_v1_h1_g1_5")
        self.label_h2_v1_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_6.setObjectName(u"label_h2_v1_h1_g1_6")
        self.label_h2_v1_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_7.setObjectName(u"label_h2_v1_h1_g1_7")
        self.label_h2_v1_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_8.setObjectName(u"label_h2_v1_h1_g1_8")
        self.label_h2_v1_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_9 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_9.setObjectName(u"label_h2_v1_h1_g1_9")
        self.label_h2_v1_h1_g1_9.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v1_h1_g1_10 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_10.setObjectName(u"label_h2_v1_h1_g1_10")
        self.label_h2_v1_h1_g1_10.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v1_h1_g1_11 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_11.setObjectName(u"label_h2_v1_h1_g1_11")
        self.label_h2_v1_h1_g1_11.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v1_h1_g1_12 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_12.setObjectName(u"label_h2_v1_h1_g1_12")
        self.label_h2_v1_h1_g1_12.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v1_h1_g1_13 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_13.setObjectName(u"label_h2_v1_h1_g1_13")
        self.label_h2_v1_h1_g1_13.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_14 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_14.setObjectName(u"label_h2_v1_h1_g1_14")
        self.label_h2_v1_h1_g1_14.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_15 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_15.setObjectName(u"label_h2_v1_h1_g1_15")
        self.label_h2_v1_h1_g1_15.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v1_h1_g1_16 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_16.setObjectName(u"label_h2_v1_h1_g1_16")
        self.label_h2_v1_h1_g1_16.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_1, 0, 0, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_2, 1, 0, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_3, 2, 0, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_4, 3, 0, 1, 1)

        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_5, 0, 1, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_6, 1, 1, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_7, 2, 1, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_8, 3, 1, 1, 1)

        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_9,  0, 2, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_10, 1, 2, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_11, 2, 2, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_12, 3, 2, 1, 1)

        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_13, 0, 3, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_14, 1, 3, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_15, 2, 3, 1, 1)
        self.grid_layout_h2_v1_h1_1.addWidget(self.label_h2_v1_h1_g1_16, 3, 3, 1, 1)

        # 2nd horizontal layout content - vertical layout 2
        self.vertical_layout_h2_2 = QVBoxLayout()
        self.vertical_layout_h2_2.setObjectName(u"vertical_layout_h2_2")
        self.vertical_layout_h2_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_2)

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout
        self.horizontal_layout_h2_v2_1 = QHBoxLayout()
        self.horizontal_layout_h2_v2_1.setObjectName(u"horizontal_layout_h2_v2_1")
        self.horizontal_layout_h2_v2_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_2.addLayout(self.horizontal_layout_h2_v2_1)

        # 2nd horizontal layout content - vertical layout 2 content - buttons
        self.push_button_h2_v2_1 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_1.setObjectName(u"Weapon_2_Forma_1")
        self.push_button_h2_v2_1.setText(QCoreApplication.translate("MainWindow", u"Forma 1: None", None))  # move to re-translate
        self.push_button_h2_v2_1.setIcon(icon_slot_forma)
        self.push_button_h2_v2_1.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_1, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v2_1.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v2_1.set_button_type("Forma")

        self.push_button_h2_v2_2 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_2.setObjectName(u"Weapon_2_Forma_2")
        self.push_button_h2_v2_2.setText(QCoreApplication.translate("MainWindow", u"Forma 2: None", None))  # move to re-translate
        self.push_button_h2_v2_2.setIcon(icon_slot_forma)
        self.push_button_h2_v2_2.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_2, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v2_2.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v2_2.set_button_type("Forma")

        self.push_button_h2_v2_3 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_3.setObjectName(u"Weapon_2_Forma_3")
        self.push_button_h2_v2_3.setText(QCoreApplication.translate("MainWindow", u"Forma 3: None", None))  # move to re-translate
        self.push_button_h2_v2_3.setIcon(icon_slot_forma)
        self.push_button_h2_v2_3.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_3, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v2_3.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v2_3.set_button_type("Forma")

        self.push_button_h2_v2_4 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_4.setObjectName(u"Weapon_2_Forma_4")
        self.push_button_h2_v2_4.setText(QCoreApplication.translate("MainWindow", u"Forma 4: None", None))  # move to re-translate
        self.push_button_h2_v2_4.setIcon(icon_slot_forma)
        self.push_button_h2_v2_4.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_4, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v2_4.clicked.connect(self.fill_side_menu_forma)
        self.push_button_h2_v2_4.set_button_type("Forma")

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout content
        self.tool_button_h2_v2_h1_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v2_h1_1.setObjectName(u"Weapon_2_Button")
        self.tool_button_h2_v2_h1_1.setText(QCoreApplication.translate("MainWindow", u"Weapon 2", None))  # move to re-translate
        self.tool_button_h2_v2_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v2_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v2_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v2_1.addWidget(self.tool_button_h2_v2_h1_1)
        self.tool_button_h2_v2_h1_1.clicked.connect(self.fill_side_menu_weapon)
        self.tool_button_h2_v2_h1_1.set_button_type("Weapon")

        self.tool_button_h2_v2_h1_1a = MyQToolButton(self.centralwidget)
        self.tool_button_h2_v2_h1_1a.setObjectName(u"Transform_Weapon_2_Button")
        self.tool_button_h2_v2_h1_1a.setIcon(icon_slot_item_addon)
        self.tool_button_h2_v2_h1_1a.setIconSize(icon_slot_item_addon_size)
        self.tool_button_h2_v2_h1_1a.clicked.connect(self.fill_side_menu_transform)
        # self.tool_button_h2_v2_h1_1.set_button_type("Transform")  # TODO

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout content - grid layout
        self.grid_layout_h2_v2_h1_1 = QGridLayout()
        self.grid_layout_h2_v2_h1_1.setObjectName(u"grid_layout_h2_v2_h1_1")
        self.grid_layout_h2_v2_h1_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.horizontal_layout_h2_v2_1.addLayout(self.grid_layout_h2_v2_h1_1)

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout content - grid layout content
        self.label_h2_v2_h1_g1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_1.setObjectName(u"label_h2_v2_h1_g1_1")
        self.label_h2_v2_h1_g1_1.setText(QCoreApplication.translate("MainWindow", u"Reliability ", None))  # move to re-translate

        self.label_h2_v2_h1_g1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_2.setObjectName(u"label_h2_v2_h1_g1_2")
        self.label_h2_v2_h1_g1_2.setText(QCoreApplication.translate("MainWindow", u"Handling ", None))  # move to re-translate

        self.label_h2_v2_h1_g1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_3.setObjectName(u"label_h2_v2_h1_g1_3")
        self.label_h2_v2_h1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Conversion ", None))  # move to re-translate

        self.label_h2_v2_h1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_4.setObjectName(u"label_h2_v2_h1_g1_4")
        self.label_h2_v2_h1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Conductivity ", None))  # move to re-translate

        self.label_h2_v2_h1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_5.setObjectName(u"label_h2_v2_h1_g1_5")
        self.label_h2_v2_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_6.setObjectName(u"label_h2_v2_h1_g1_6")
        self.label_h2_v2_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_7.setObjectName(u"label_h2_v2_h1_g1_7")
        self.label_h2_v2_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_8.setObjectName(u"label_h2_v2_h1_g1_8")
        self.label_h2_v2_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_9 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_9.setObjectName(u"label_h2_v2_h1_g1_9")
        self.label_h2_v2_h1_g1_9.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v2_h1_g1_10 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_10.setObjectName(u"label_h2_v2_h1_g1_10")
        self.label_h2_v2_h1_g1_10.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v2_h1_g1_11 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_11.setObjectName(u"label_h2_v2_h1_g1_11")
        self.label_h2_v2_h1_g1_11.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v2_h1_g1_12 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_12.setObjectName(u"label_h2_v2_h1_g1_12")
        self.label_h2_v2_h1_g1_12.setText(QCoreApplication.translate("MainWindow", u"/", None))  # move to re-translate

        self.label_h2_v2_h1_g1_13 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_13.setObjectName(u"label_h2_v2_h1_g1_13")
        self.label_h2_v2_h1_g1_13.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_14 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_14.setObjectName(u"label_h2_v2_h1_g1_14")
        self.label_h2_v2_h1_g1_14.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_15 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_15.setObjectName(u"label_h2_v2_h1_g1_15")
        self.label_h2_v2_h1_g1_15.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v2_h1_g1_16 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_16.setObjectName(u"label_h2_v2_h1_g1_16")
        self.label_h2_v2_h1_g1_16.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_1, 0, 0, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_2, 1, 0, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_3, 2, 0, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_4, 3, 0, 1, 1)

        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_5, 0, 1, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_6, 1, 1, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_7, 2, 1, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_8, 3, 1, 1, 1)

        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_9,  0, 2, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_10, 1, 2, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_11, 2, 2, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_12, 3, 2, 1, 1)

        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_13, 0, 3, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_14, 1, 3, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_15, 2, 3, 1, 1)
        self.grid_layout_h2_v2_h1_1.addWidget(self.label_h2_v2_h1_g1_16, 3, 3, 1, 1)

        # 2nd horizontal layout content - vertical layout 3
        self.vertical_layout_h2_3 = QVBoxLayout()
        self.vertical_layout_h2_3.setObjectName(u"vertical_layout_h2_1")
        self.vertical_layout_h2_3.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_3)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1
        self.horizontal_layout_h2_v3_1 = QHBoxLayout()
        self.horizontal_layout_h2_v3_1.setObjectName(u"vertical_layout_h2_v3_1")
        self.horizontal_layout_h2_v3_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_3.addLayout(self.horizontal_layout_h2_v3_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1 content
        self.tool_button_h2_v3_h1_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_1.setObjectName(u"Offensive_Button")
        self.tool_button_h2_v3_h1_1.setText(QCoreApplication.translate("MainWindow", u"Offensive", None)) # move to re-translate
        self.tool_button_h2_v3_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_1)
        self.tool_button_h2_v3_h1_1.clicked.connect(self.fill_side_menu_offensive)
        self.tool_button_h2_v3_h1_1.set_button_type("Offensive")

        self.tool_button_h2_v3_h1_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_2.setObjectName(u"Defensive_Button")
        self.tool_button_h2_v3_h1_2.setText(QCoreApplication.translate("MainWindow", u"Defensive", None)) # move to re-translate
        self.tool_button_h2_v3_h1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_2.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_2.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_2)
        self.tool_button_h2_v3_h1_2.clicked.connect(self.fill_side_menu_defensive)
        self.tool_button_h2_v3_h1_2.set_button_type("Defensive")

        self.tool_button_h2_v3_h1_2a = MyQToolButton(self.centralwidget)
        self.tool_button_h2_v3_h1_2a.setObjectName(u"Transform_Defensive_Button")
        self.tool_button_h2_v3_h1_2a.setIcon(icon_slot_item_addon)
        self.tool_button_h2_v3_h1_2a.setIconSize(icon_slot_item_addon_size)
        self.tool_button_h2_v3_h1_2a.clicked.connect(self.fill_side_menu_transform)
        # self.tool_button_h2_v3_h1_2a.set_button_type("Transform")  # TODO

        self.tool_button_h2_v3_h1_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_3.setObjectName(u"Jail_Button")
        self.tool_button_h2_v3_h1_3.setText(QCoreApplication.translate("MainWindow", u"Jail", None)) # move to re-translate
        self.tool_button_h2_v3_h1_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_3.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_3.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_3)
        self.tool_button_h2_v3_h1_3.clicked.connect(self.fill_side_menu_jail)
        self.tool_button_h2_v3_h1_3.set_button_type("Jail")

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1 content - grid layout
        self.grid_layout_h2_v3_h1_1 = QGridLayout()
        self.grid_layout_h2_v3_h1_1.setObjectName(u"grid_layout_h2_v3_h1_1")
        self.grid_layout_h2_v3_h1_1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.horizontal_layout_h2_v3_1.addLayout(self.grid_layout_h2_v3_h1_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1 content - grid layout content
        self.label_h2_v3_h1_g1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_1.setObjectName(u"label_h2_v3_h1_g1_1")
        self.label_h2_v3_h1_g1_1.setText(QCoreApplication.translate("MainWindow", u"Bleed W1", None))  # move to re-translate

        self.label_h2_v3_h1_g1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_2.setObjectName(u"label_h2_v3_h1_g1_2")
        self.label_h2_v3_h1_g1_2.setText(QCoreApplication.translate("MainWindow", u"Bleed W2", None))  # move to re-translate

        self.label_h2_v3_h1_g1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_3.setObjectName(u"label_h2_v3_h1_g1_3")
        self.label_h2_v3_h1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Bleed O", None))  # move to re-translate

        self.label_h2_v3_h1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_4.setObjectName(u"label_h2_v3_h1_g1_4")
        self.label_h2_v3_h1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Balance", None))  # move to re-translate

        self.label_h2_v3_h1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_5.setObjectName(u"label_h2_v3_h1_g1_5")
        self.label_h2_v3_h1_g1_5.setFont(self.font_numbers_bleed)
        self.label_h2_v3_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v3_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_6.setObjectName(u"label_h2_v3_h1_g1_6")
        self.label_h2_v3_h1_g1_6.setFont(self.font_numbers_bleed)
        self.label_h2_v3_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v3_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_7.setObjectName(u"label_h2_v3_h1_g1_7")
        self.label_h2_v3_h1_g1_7.setFont(self.font_numbers_bleed)
        self.label_h2_v3_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.label_h2_v3_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_8.setObjectName(u"label_h2_v3_h1_g1_8")
        self.label_h2_v3_h1_g1_8.setFont(self.font_numbers_bleed)
        self.label_h2_v3_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate

        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_1, 0, 0, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_2, 1, 0, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_3, 2, 0, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_4, 3, 0, 1, 1)

        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_5, 0, 1, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_6, 1, 1, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_7, 2, 1, 1, 1)
        self.grid_layout_h2_v3_h1_1.addWidget(self.label_h2_v3_h1_g1_8, 3, 1, 1, 1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2
        self.horizontal_layout_h2_v3_2 = QHBoxLayout()
        self.horizontal_layout_h2_v3_2.setObjectName(u"horizontal_layout_h2_v3_2")
        self.horizontal_layout_h2_v3_2.setContentsMargins(0, 0, 0, 0)
        # self.horizontal_layout_h2_v3_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.vertical_layout_h2_3.addLayout(self.horizontal_layout_h2_v3_2)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content
        self.tool_button_h2_v3_h2_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h2_1.setObjectName(u"Blood_Code_Button")
        self.tool_button_h2_v3_h2_1.setText(QCoreApplication.translate("MainWindow", u"Blood Code", None)) # move to re-translate
        self.tool_button_h2_v3_h2_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h2_1.setIcon(icon_slot_blood_code)
        self.tool_button_h2_v3_h2_1.setIconSize(icon_slot_blood_code_size)
        self.horizontal_layout_h2_v3_2.addWidget(self.tool_button_h2_v3_h2_1)
        self.tool_button_h2_v3_h2_1.clicked.connect(self.fill_side_menu_blood_code)
        self.tool_button_h2_v3_h2_1.set_button_type("BloodCode")

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content - vertical layout
        self.vertical_layout_h2_v3_h2_1 = QVBoxLayout()
        self.vertical_layout_h2_v3_h2_1.setObjectName(u"vertical_layout_h2_v3_h2_1")
        self.vertical_layout_h2_v3_h2_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_v3_h2_1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.horizontal_layout_h2_v3_2.addLayout(self.vertical_layout_h2_v3_h2_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content - vertical layout content
        self.push_button_h2_v3_h2_v1_1 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_1.setObjectName(u"Booster_1_Button")
        self.push_button_h2_v3_h2_v1_1.setText(QCoreApplication.translate("MainWindow", u"Booster 1: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_1.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_1.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_1.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_1, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_1.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_1.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_2 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_2.setObjectName(u"Booster_2_Button")
        self.push_button_h2_v3_h2_v1_2.setText(QCoreApplication.translate("MainWindow", u"Booster 2: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_2.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_2.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_2.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_2, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_2.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_2.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_3 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_3.setObjectName(u"Booster_3_Button")
        self.push_button_h2_v3_h2_v1_3.setText(QCoreApplication.translate("MainWindow", u"Booster 3: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_3.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_3.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_3.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_3, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_3.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_3.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_4 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_4.setObjectName(u"Booster_4_Button")
        self.push_button_h2_v3_h2_v1_4.setText(QCoreApplication.translate("MainWindow", u"Booster 4: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_4.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_4.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_4.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_4, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_4.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_4.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_5 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_5.setObjectName(u"Booster_5_Button")
        self.push_button_h2_v3_h2_v1_5.setText(QCoreApplication.translate("MainWindow", u"Booster 5: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_5.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_5.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_5.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_5, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_5.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_5.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_6 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_6.setObjectName(u"Booster_6_Button")
        self.push_button_h2_v3_h2_v1_6.setText(QCoreApplication.translate("MainWindow", u"Booster 6: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_6.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_6.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_6.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_6, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_6.clicked.connect(self.fill_side_menu_booster)
        self.push_button_h2_v3_h2_v1_6.set_button_type("Booster")

        self.push_button_h2_v3_h2_v1_7 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_7.setObjectName(u"Trait_1_Button")
        self.push_button_h2_v3_h2_v1_7.setText(QCoreApplication.translate("MainWindow", u"Trait 1: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_7.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_7.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_7.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_7, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_7.set_button_type("BloodCode")

        self.push_button_h2_v3_h2_v1_8 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_8.setObjectName(u"Trait_2_Button")
        self.push_button_h2_v3_h2_v1_8.setText(QCoreApplication.translate("MainWindow", u"Trait 2: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_8.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_8.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_8.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_8, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_8.set_button_type("BloodCode")

        self.push_button_h2_v3_h2_v1_9 = MyQPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_9.setObjectName(u"Trait_3_Button")
        self.push_button_h2_v3_h2_v1_9.setText(QCoreApplication.translate("MainWindow", u"Trait 3: None", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_9.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_9.setIconSize(icon_slot_forma_size)
        self.push_button_h2_v3_h2_v1_9.setMinimumHeight(icon_slot_forma_size.height())
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_9, 0, Qt.AlignmentFlag.AlignLeft)
        self.push_button_h2_v3_h2_v1_9.set_button_type("BloodCode")

        # 2nd horizontal layout content - spacer at the end (right)
        self.horizontal_spacer_h2_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_horizontal_layout_2.addItem(self.horizontal_spacer_h2_1)

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
        self.tool_button_h3_g1_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_1.setObjectName(u"tool_button_h3_g1_1")
        self.tool_button_h3_g1_1.setText(QCoreApplication.translate("MainWindow", u"Dodge Effectiveness", None)) # move to re-translate
        self.tool_button_h3_g1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_h3_g1_1.setIcon(icon_text_arrow)

        self.tool_button_h3_g1_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_2.setObjectName(u"tool_button_h3_g1_2")
        self.tool_button_h3_g1_2.setText(QCoreApplication.translate("MainWindow", u"Quick", None)) # move to re-translate
        self.tool_button_h3_g1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_button_h3_g1_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_3.setObjectName(u"tool_button_h3_g1_3")
        self.tool_button_h3_g1_3.setText(QCoreApplication.translate("MainWindow", u"Defensive Formae", None)) # move to re-translate
        self.tool_button_h3_g1_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_h3_g1_3.setIcon(icon_text_arrow)

        self.tool_button_h3_g1_4 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_4.setObjectName(u"tool_button_h3_g1_4")
        self.tool_button_h3_g1_4.setFont(self.font_defensive_formae)
        self.tool_button_h3_g1_4.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h3_g1_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.grid_layout_h3_1.addWidget(self.tool_button_h3_g1_1, 0, 0, 1, 1)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_g1_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_g1_3, 2, 0, 1, 1)
        self.grid_layout_h3_1.addWidget(self.tool_button_h3_g1_4, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        # 3rd horizontal layout content - vertical layout 1
        self.vertical_layout_h3_1 = QVBoxLayout()
        self.vertical_layout_h3_1.setObjectName(u"vertical_layout_h3_1")
        self.vertical_layout_h3_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h3_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_horizontal_layout_3.addLayout(self.vertical_layout_h3_1)

        # 3rd horizontal layout content - vertical layout 1 content
        self.label_h3_v1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_1.setObjectName(u"label_h3_v1_1")
        self.label_h3_v1_1.setText(QCoreApplication.translate("MainWindow", u"Attributes & Burden", None)) # move to re-translate
        self.label_h3_v1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout_h3_1.addWidget(self.label_h3_v1_1)

        # 3rd horizontal layout content - vertical layout 1 content - grid layout 1
        self.grid_layout_h3_v1_2 = QGridLayout()
        self.grid_layout_h3_v1_2.setObjectName(u"grid_layout_h3_v1_2")
        self.vertical_layout_h3_1.addLayout(self.grid_layout_h3_v1_2)

        # 3rd horizontal layout content - vertical layout 1 content - grid layout 1 content
        self.tool_button_h3_v1_g1_1 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_1.setObjectName(u"tool_button_h3_v1_g1_1")
        self.tool_button_h3_v1_g1_1.setText(QCoreApplication.translate("MainWindow", u"Strength", None)) # move to re-translate
        self.tool_button_h3_v1_g1_1.setIcon(icon_attribute_strength)
        self.tool_button_h3_v1_g1_1.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_2 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_2.setObjectName(u"tool_button_h3_v1_g1_2")
        self.tool_button_h3_v1_g1_2.setText(QCoreApplication.translate("MainWindow", u"Dexterity", None)) # move to re-translate
        self.tool_button_h3_v1_g1_2.setIcon(icon_attribute_dexterity)
        self.tool_button_h3_v1_g1_2.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_3 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_3.setObjectName(u"tool_button_h3_v1_g1_3")
        self.tool_button_h3_v1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Mind", None)) # move to re-translate
        self.tool_button_h3_v1_g1_3.setIcon(icon_attribute_mind)
        self.tool_button_h3_v1_g1_3.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_4 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_4.setObjectName(u"tool_button_h3_v1_g1_4")
        self.tool_button_h3_v1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Willpower", None)) # move to re-translate
        self.tool_button_h3_v1_g1_4.setIcon(icon_attribute_willpower)
        self.tool_button_h3_v1_g1_4.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_5 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_5.setObjectName(u"tool_button_h3_v1_g1_5")
        self.tool_button_h3_v1_g1_5.setText(QCoreApplication.translate("MainWindow", u"Vitality", None)) # move to re-translate
        self.tool_button_h3_v1_g1_5.setIcon(icon_attribute_vitality)
        self.tool_button_h3_v1_g1_5.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_6 = MyQPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_6.setObjectName(u"tool_button_h3_v1_g1_6")
        self.tool_button_h3_v1_g1_6.setText(QCoreApplication.translate("MainWindow", u"Fortitude", None)) # move to re-translate
        self.tool_button_h3_v1_g1_6.setIcon(icon_attribute_fortitude)
        self.tool_button_h3_v1_g1_6.setIconSize(icon_attribute_size)

        self.label_h3_v1_g1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_1.setObjectName(u"label_h3_v1_g1_1")
        self.label_h3_v1_g1_1.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_1.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_2.setObjectName(u"label_h3_v1_g1_2")
        self.label_h3_v1_g1_2.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_3.setObjectName(u"label_h3_v1_g1_3")
        self.label_h3_v1_g1_3.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_3.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_4.setObjectName(u"label_h3_v1_g1_4")
        self.label_h3_v1_g1_4.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_4.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_5.setObjectName(u"label_h3_v1_g1_5")
        self.label_h3_v1_g1_5.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_5.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_6.setObjectName(u"label_h3_v1_g1_6")
        self.label_h3_v1_g1_6.setFont(self.font_numbers_attribute)
        self.label_h3_v1_g1_6.setText(QCoreApplication.translate("MainWindow", u"0", None))  # move to re-translate
        self.label_h3_v1_g1_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_1 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_1.setObjectName(u"progress_bar_h3_v1_g1_1")
        self.progress_bar_h3_v1_g1_1.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_1.setFormat("%v")
        self.progress_bar_h3_v1_g1_1.setValue(0)
        self.progress_bar_h3_v1_g1_1.setMaximum(0)
        self.progress_bar_h3_v1_g1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_2 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_2.setObjectName(u"progress_bar_h3_v1_g1_2")
        self.progress_bar_h3_v1_g1_2.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_2.setFormat("%v")
        self.progress_bar_h3_v1_g1_2.setValue(0)
        self.progress_bar_h3_v1_g1_2.setMaximum(0)
        self.progress_bar_h3_v1_g1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_3 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_3.setObjectName(u"progress_bar_h3_v1_g1_3")
        self.progress_bar_h3_v1_g1_3.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_3.setFormat("%v")
        self.progress_bar_h3_v1_g1_3.setValue(0)
        self.progress_bar_h3_v1_g1_3.setMaximum(0)
        self.progress_bar_h3_v1_g1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_4 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_4.setObjectName(u"progress_bar_h3_v1_g1_4")
        self.progress_bar_h3_v1_g1_4.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_4.setFormat("%v")
        self.progress_bar_h3_v1_g1_4.setValue(0)
        self.progress_bar_h3_v1_g1_4.setMaximum(0)
        self.progress_bar_h3_v1_g1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_5 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_5.setObjectName(u"progress_bar_h3_v1_g1_5")
        self.progress_bar_h3_v1_g1_5.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_5.setFormat("%v")
        self.progress_bar_h3_v1_g1_5.setValue(0)
        self.progress_bar_h3_v1_g1_5.setMaximum(0)
        self.progress_bar_h3_v1_g1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_6 = AttributeProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_6.setObjectName(u"progress_bar_h3_v1_g1_6")
        self.progress_bar_h3_v1_g1_6.setFont(self.font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_6.setFormat("%v")
        self.progress_bar_h3_v1_g1_6.setValue(0)
        self.progress_bar_h3_v1_g1_6.setMaximum(0)
        self.progress_bar_h3_v1_g1_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_1, 0, 0, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_2, 0, 1, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_3, 0, 2, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_4, 0, 3, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_5, 0, 4, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.tool_button_h3_v1_g1_6, 0, 5, 1, 1)

        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_1, 1, 0, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_2, 1, 1, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_3, 1, 2, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_4, 1, 3, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_5, 1, 4, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.label_h3_v1_g1_6, 1, 5, 1, 1)

        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_1, 2, 0, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_2, 2, 1, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_3, 2, 2, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_4, 2, 3, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_5, 2, 4, 1, 1)
        self.grid_layout_h3_v1_2.addWidget(self.progress_bar_h3_v1_g1_6, 2, 5, 1, 1)

        # 4th horizontal layout
        self.tool_button_pre_h4 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_pre_h4.setObjectName(u"tool_button_pre_h4")
        self.tool_button_pre_h4.setText(QCoreApplication.translate("MainWindow", u"Defense", None)) # move to re-translate
        self.tool_button_pre_h4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_pre_h4.setIcon(icon_text_arrow)
        self.main_vertical_layout.addWidget(self.tool_button_pre_h4)

        self.main_horizontal_layout_4 = QHBoxLayout()
        self.main_horizontal_layout_4.setObjectName(u"main_horizontal_layout_4")
        self.main_horizontal_layout_4.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_4)

        # # 4th horizontal layout content
        self.tool_button_h4_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_1.setObjectName(u"tool_button_h4_1")
        self.tool_button_h4_1.setFont(self.font_numbers_defense)
        self.tool_button_h4_1.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_1.setIcon(icon_defense_slash)
        self.tool_button_h4_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_1)

        self.tool_button_h4_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_2.setObjectName(u"tool_button_h4_2")
        self.tool_button_h4_2.setFont(self.font_numbers_defense)
        self.tool_button_h4_2.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_2.setIcon(icon_defense_crush)
        self.tool_button_h4_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_2)

        self.tool_button_h4_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_3.setObjectName(u"tool_button_h4_3")
        self.tool_button_h4_3.setFont(self.font_numbers_defense)
        self.tool_button_h4_3.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_3.setIcon(icon_defense_pierce)
        self.tool_button_h4_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_3)

        self.tool_button_h4_4 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_4.setObjectName(u"tool_button_h4_4")
        self.tool_button_h4_4.setFont(self.font_numbers_defense)
        self.tool_button_h4_4.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_4.setIcon(icon_defense_blood)
        self.tool_button_h4_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_4)

        self.tool_button_h4_5 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_5.setObjectName(u"tool_button_h4_5")
        self.tool_button_h4_5.setFont(self.font_numbers_defense)
        self.tool_button_h4_5.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_5.setIcon(icon_defense_fire)
        self.tool_button_h4_5.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_5)

        self.tool_button_h4_6 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_6.setObjectName(u"tool_button_h4_6")
        self.tool_button_h4_6.setFont(self.font_numbers_defense)
        self.tool_button_h4_6.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_6.setIcon(icon_defense_ice)
        self.tool_button_h4_6.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_6)

        self.tool_button_h4_7 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_7.setObjectName(u"tool_button_h4_7")
        self.tool_button_h4_7.setFont(self.font_numbers_defense)
        self.tool_button_h4_7.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h4_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_7.setIcon(icon_defense_thunder)
        self.tool_button_h4_7.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_7)

        # 5th horizontal layout
        self.tool_button_pre_h5 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_pre_h5.setObjectName(u"tool_button_pre_h5")
        self.tool_button_pre_h5.setText(QCoreApplication.translate("MainWindow", u"Guarding Defense", None)) # move to re-translate
        self.tool_button_pre_h5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_pre_h5.setIcon(icon_text_arrow)
        self.main_vertical_layout.addWidget(self.tool_button_pre_h5)

        self.main_horizontal_layout_5 = QHBoxLayout()
        self.main_horizontal_layout_5.setObjectName(u"main_horizontal_layout_5")
        self.main_horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_5)

        # 5th horizontal layout content
        self.tool_button_h5_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_1.setObjectName(u"tool_button_h5_1")
        self.tool_button_h5_1.setFont(self.font_numbers_defense)
        self.tool_button_h5_1.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_1.setIcon(icon_defense_slash)
        self.tool_button_h5_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_1)

        self.tool_button_h5_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_2.setObjectName(u"tool_button_h5_2")
        self.tool_button_h5_2.setFont(self.font_numbers_defense)
        self.tool_button_h5_2.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_2.setIcon(icon_defense_crush)
        self.tool_button_h5_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_2)

        self.tool_button_h5_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_3.setObjectName(u"tool_button_h5_3")
        self.tool_button_h5_3.setFont(self.font_numbers_defense)
        self.tool_button_h5_3.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_3.setIcon(icon_defense_pierce)
        self.tool_button_h5_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_3)

        self.tool_button_h5_4 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_4.setObjectName(u"tool_button_h5_4")
        self.tool_button_h5_4.setFont(self.font_numbers_defense)
        self.tool_button_h5_4.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_4.setIcon(icon_defense_blood)
        self.tool_button_h5_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_4)

        self.tool_button_h5_5 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_5.setObjectName(u"tool_button_h5_5")
        self.tool_button_h5_5.setFont(self.font_numbers_defense)
        self.tool_button_h5_5.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_5.setIcon(icon_defense_fire)
        self.tool_button_h5_5.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_5)

        self.tool_button_h5_6 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_6.setObjectName(u"tool_button_h5_6")
        self.tool_button_h5_6.setFont(self.font_numbers_defense)
        self.tool_button_h5_6.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_6.setIcon(icon_defense_ice)
        self.tool_button_h5_6.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_6)

        self.tool_button_h5_7 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_7.setObjectName(u"tool_button_h5_7")
        self.tool_button_h5_7.setFont(self.font_numbers_defense)
        self.tool_button_h5_7.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h5_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_7.setIcon(icon_defense_thunder)
        self.tool_button_h5_7.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_7)

        # 6th horizontal layout
        self.tool_button_pre_h6 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_pre_h6.setObjectName(u"tool_button_pre_h6")
        self.tool_button_pre_h6.setText(QCoreApplication.translate("MainWindow", u"Resistances", None)) # move to re-translate
        self.tool_button_pre_h6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_pre_h6.setIcon(icon_text_arrow)
        self.main_vertical_layout.addWidget(self.tool_button_pre_h6)

        self.main_horizontal_layout_6 = QHBoxLayout()
        self.main_horizontal_layout_6.setObjectName(u"main_horizontal_layout_6")
        self.main_horizontal_layout_6.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_6)

        # 6th horizontal layout content
        self.tool_button_h6_1 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_1.setObjectName(u"tool_button_h6_1")
        self.tool_button_h6_1.setFont(self.font_numbers_defense)
        self.tool_button_h6_1.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_1.setIcon(icon_resistance_disease)
        self.tool_button_h6_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_1)

        self.tool_button_h6_2 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_2.setObjectName(u"tool_button_h6_2")
        self.tool_button_h6_2.setFont(self.font_numbers_defense)
        self.tool_button_h6_2.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_2.setIcon(icon_resistance_wound)
        self.tool_button_h6_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_2)

        self.tool_button_h6_3 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_3.setObjectName(u"tool_button_h6_3")
        self.tool_button_h6_3.setFont(self.font_numbers_defense)
        self.tool_button_h6_3.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_3.setIcon(icon_resistance_bleed)
        self.tool_button_h6_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_3)

        self.tool_button_h6_4 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_4.setObjectName(u"tool_button_h6_4")
        self.tool_button_h6_4.setFont(self.font_numbers_defense)
        self.tool_button_h6_4.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_4.setIcon(icon_resistance_curse)
        self.tool_button_h6_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_4)

        # dummy button
        self.tool_button_h6_5 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_5.setObjectName(u"tool_button_h6_5")
        self.tool_button_h6_5.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_5.setVisible(False)
        sp = self.tool_button_h6_5.sizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self.tool_button_h6_5.setSizePolicy(sp)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_5)

        # dummy button
        self.tool_button_h6_6 = MyQToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_6.setObjectName(u"tool_button_h6_6")
        self.tool_button_h6_6.setText(QCoreApplication.translate("MainWindow", u"0", None)) # move to re-translate
        self.tool_button_h6_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_6.setVisible(False)
        sp = self.tool_button_h6_6.sizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self.tool_button_h6_6.setSizePolicy(sp)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_6)

        # end of setupUi
        MainWindow.setCentralWidget(self.centralwidget)
        self.set_character_to_widget_mapping()
        self.add_menu_bar(MainWindow)
        self.retranslateUi(MainWindow)

    def disconnect_side_menu_signals(self):
        # warning will be thrown if signals are already disconnected, ignore it
        warnings.filterwarnings("ignore", category=RuntimeWarning, message=r".*Failed to disconnect.*")
        self.side_menu_buttons.itemClicked.disconnect()
        self.side_menu_buttons.itemEntered.disconnect()
        self.side_menu_content.itemClicked.disconnect()
        self.side_menu_content.itemEntered.disconnect()
        warnings.resetwarnings()

    def show_side_menu(self, menu):
        self.side_menu_buttons.setVisible(True)
        self.side_menu_content.setVisible(True)
        self.side_menu_text.setVisible(True)
        self.side_menu_content.set_menu_type(menu)

    def close_side_menu(self):
        self.side_menu_buttons.setVisible(False)
        self.side_menu_content.setVisible(False)
        self.side_menu_text.setVisible(False)
        self.side_menu_content.set_menu_type("")

    def close_side_menu_if_already_opened(self, sender):
        if self.selected_side_menu["Menu"] == sender:
            if self.selected_side_menu["Count"] == 0:
                self.selected_side_menu["Count"] = 1
            else:
                self.selected_side_menu["Count"] = 0
                self.close_side_menu()
                return True
        else:
            self.selected_side_menu["Menu"] = sender
            self.selected_side_menu["Count"] = 1

        return False

    def fill_side_menu_forma(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.filter_menu_forma)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)

        if "Weapon_1_Forma_1" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_1_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_1_weapon_1_hover)
        elif "Weapon_1_Forma_2" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_2_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_2_weapon_1_hover)
        elif "Weapon_1_Forma_3" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_3_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_3_weapon_1_hover)
        elif "Weapon_1_Forma_4" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_4_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_4_weapon_1_hover)
        elif "Weapon_2_Forma_1" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_1_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_1_weapon_2_hover)
        elif "Weapon_2_Forma_2" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_2_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_2_weapon_2_hover)
        elif "Weapon_2_Forma_3" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_3_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_3_weapon_2_hover)
        elif "Weapon_2_Forma_4" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_forma_4_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_forma_4_weapon_2_hover)

        self.show_side_menu("Forma")

        # buttons
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_All.png"), "")
        item.setStatusTip("All")
        self.side_menu_buttons.addItem(item)
        self.side_menu_buttons.setCurrentItem(item)
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_Favorite.png"), "")
        item.setStatusTip("Favorite")
        self.side_menu_buttons.addItem(item)

        button_names = ["SingleSword", "GreatSword", "DualSword", "Bayonet", "Halberd", "Hammer", "RuneBlade"]
        for name in button_names:
            item = QListWidgetItem(QIcon(u":/All/UI/Menu_Weapon_" + name + ".png"), "")
            item.setStatusTip(name)
            self.side_menu_buttons.addItem(item)

        # temporary, fix file names?
        mapping = {
            "Menu_Formae_Action.png": "WeaponAction",
            "Menu_Formae_Magic_Range_Long": "MagicLongRange",
            "Menu_Formae_Magic_Range_Close.png": "MagicMiddleRange",
            "Menu_Formae_Assistance_Attack.png": "SupportAttack",
            "Menu_Formae_Assistance_Defense.png": "SupportDefense",
            "Menu_Formae_Assistance_Other.png": "SupportOther",
        }
        for k, v in mapping.items():
            item = QListWidgetItem(QIcon(u":/All/UI/" + k), "")
            item.setStatusTip(v)
            self.side_menu_buttons.addItem(item)

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k, v in self.builder.formae.items():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Forma/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            if v.favorite:
                self.add_favorite_to_icon(item)
            self.side_menu_content.addItem(item)

    def fill_side_menu_booster(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.filter_menu_booster)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)

        if "Booster_1" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_1_hover)
        elif "Booster_2" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_2_hover)
        elif "Booster_3" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_3_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_3_hover)
        elif "Booster_4" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_4_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_4_hover)
        elif "Booster_5" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_5_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_5_hover)
        elif "Booster_6" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_booster_6_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_booster_6_hover)

        self.show_side_menu("Booster")

        # buttons
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_All.png"), "")
        item.setStatusTip("All")
        self.side_menu_buttons.addItem(item)
        self.side_menu_buttons.setCurrentItem(item)
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_Favorite.png"), "")
        item.setStatusTip("Favorite")
        self.side_menu_buttons.addItem(item)

        button_names = ["Basic", "Attack", "Defence", "Other"]
        for name in button_names:
            item = QListWidgetItem(QIcon(u":/All/UI/Menu_Booster_" + name + ".png"), "")
            item.setStatusTip(name)
            self.side_menu_buttons.addItem(item)

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k, v in self.builder.boosters.items():
            if v.equipped:
                # already equipped, do not show
                continue
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Booster/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            if v.favorite:
                self.add_favorite_to_icon(item)
            self.side_menu_content.addItem(item)

    def fill_side_menu_weapon(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.filter_menu_weapon)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)

        if "Weapon_1" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_weapon_1_hover)
        elif "Weapon_2" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_weapon_2_hover)

        self.show_side_menu("Weapon")

        # buttons
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_All.png"), "")
        item.setStatusTip("All")
        self.side_menu_buttons.addItem(item)
        self.side_menu_buttons.setCurrentItem(item)
        item = QListWidgetItem(QIcon(u":/All/UI/Menu_Favorite.png"), "")
        item.setStatusTip("Favorite")
        self.side_menu_buttons.addItem(item)

        button_names = ["SingleSword", "GreatSword", "DualSword", "Bayonet", "Halberd", "Hammer", "RuneBlade"]
        for name in button_names:
            item = QListWidgetItem(QIcon(u":/All/UI/Menu_Weapon_" + name + ".png"), "")
            item.setStatusTip(name)
            self.side_menu_buttons.addItem(item)

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k, v in self.builder.weapons.items():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Weapon/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            if v.favorite:
                self.add_favorite_to_icon(item)
            self.side_menu_content.addItem(item)

    def fill_side_menu_transform(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.handle_unimplemented_clicked)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)

        mode = "Weapon"
        if "Weapon_1" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_transform_weapon_1_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_transform_weapon_1_hover)
        elif "Weapon_2" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_transform_weapon_2_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_transform_weapon_2_hover)
        elif "Defensive" in self.sender().objectName():
            self.side_menu_content.itemClicked.connect(self.handle_transform_defensive_clicked)
            self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_transform_defensive_hover)
            mode = "Defensive"

        self.show_side_menu("Transform")

        # buttons - empty

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        if mode == "Weapon":
            # place Off button at the start for Weapon - looks better
            item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            item.setStatusTip("Off")
            self.side_menu_content.addItem(item)

            # some weapons do not have all transforms ! like ones with venom don't have sun or venom
            weapon_w_all_transform = self.builder.weapons["Stealth Blades"].transforms
            for k, v in weapon_w_all_transform.items():
                if "Weapon_Off" in k:
                    # already added
                    continue
                icon_name = k.replace("Weapon_", "Transform_")
                item = QListWidgetItem(QIcon(u":/All/Transform/" + icon_name + ".png"), "")
                item.setStatusTip(k)
                self.side_menu_content.addItem(item)

        if mode == "Defensive":
            defensive_w_all_transform = self.builder.defensive_formae["Clotted Shield"].transforms
            for k, v in defensive_w_all_transform.items():
                if "Defensive_Off" in k:
                    # will be added later
                    continue
                icon_name = k.replace("Defensive_", "Transform_")
                item = QListWidgetItem(QIcon(u":/All/Transform/" + icon_name + ".png"), "")
                item.setStatusTip(k)
                self.side_menu_content.addItem(item)

            # place Off button at the end for Defensive like in game - also looks better
            item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            item.setStatusTip("Off")
            self.side_menu_content.addItem(item)

    def fill_side_menu_blood_code(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.filter_menu_blood_code)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)
        self.side_menu_content.itemClicked.connect(self.handle_blood_code_clicked)
        self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_blood_code_hover)
        self.show_side_menu("BloodCode")

        # buttons - text
        # bloodlines = ["All", "Favorite", "Superbia", "Gula", "Luxuria", "Ira", "Acedia", "Avarita", "Invidia",
        #               "Humilitas", "Temperantia", "Castitas", "Patientia", "Diligentia", "Caritas", "Humanitas"]
        bloodlines = ["All", "Favorite", "Superbia", "Gula", "Luxuria", "Acedia", "Patientia", "Caritas"]
        for bloodline in bloodlines:
            item = QListWidgetItem(QIcon(), bloodline)
            item.setFont(self.font_numbers_bleed)
            self.side_menu_buttons.addItem(item)
            if bloodline == "All":
                self.side_menu_buttons.setCurrentItem(item)

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k, v in self.builder.blood_codes.items():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/BloodCode/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            if v.favorite:
                self.add_favorite_to_icon(item)
            self.side_menu_content.addItem(item)

    def fill_side_menu_offensive(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.handle_unimplemented_clicked)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)
        self.side_menu_content.itemClicked.connect(self.handle_offensive_clicked)
        self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_offensive_hover)
        self.show_side_menu("Offensive")

        # buttons - empty

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k in self.builder.offensive_formae.keys():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Offensive/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            self.side_menu_content.addItem(item)

    def fill_side_menu_defensive(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.filter_menu_defensive)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)
        self.side_menu_content.itemClicked.connect(self.handle_defensive_clicked)
        self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_defensive_hover)
        self.show_side_menu("Defensive")

        # buttons
        types = ["All", "Favorite", "Guard", "Parry", "Dodge"]
        for type in types:
            item = QListWidgetItem(QIcon(), type)
            item.setFont(self.font_numbers_bleed)
            self.side_menu_buttons.addItem(item)
            if type == "All":
                self.side_menu_buttons.setCurrentItem(item)

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k, v in self.builder.defensive_formae.items():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Defensive/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            if v.favorite:
                self.add_favorite_to_icon(item)
            self.side_menu_content.addItem(item)

    def fill_side_menu_jail(self):
        self.side_menu_buttons.clear()
        self.side_menu_content.clear()
        self.disconnect_side_menu_signals()

        if self.close_side_menu_if_already_opened(self.sender().objectName()):
            return

        self.side_menu_buttons.itemClicked.connect(self.handle_unimplemented_clicked)
        self.side_menu_buttons.itemEntered.connect(self.side_menu_buttons.foo)
        self.side_menu_content.itemClicked.connect(self.handle_jail_clicked)
        self.side_menu_content.itemEntered.connect(self.side_menu_content.handle_jail_hover)
        self.show_side_menu("Jail")

        # buttons - empty

        # content - reposition and resize layout so that content is placed right after visible buttons end
        buttons_end_y = self.calculate_buttons_end()
        self.side_vertical_layout_widget_2.setGeometry(QRect(1080, buttons_end_y, 360, 810 - buttons_end_y))

        # content
        for k in self.builder.jails.keys():
            if k == "Empty":
                item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
            else:
                item = QListWidgetItem(QIcon(u":/All/Jail/" + escape_filename(k) + ".png"), "")
            item.setStatusTip(k)
            self.side_menu_content.addItem(item)

    def filter_menu_forma(self, item):
        chosen = item.statusTip()
        self.side_menu_content.clear()
        self.side_menu_text.clear()
        self.display_favorite_tips_if_needed(chosen)

        for k, v in self.builder.formae.items():
            if chosen == "All" or chosen == v.type or v.matching_weapons.get(chosen) \
                    or (chosen == "Favorite" and v.favorite) or k == "Empty":
                if k == "Empty":
                    item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
                else:
                    item = QListWidgetItem(QIcon(u":/All/Forma/" + escape_filename(k) + ".png"), "")
                item.setStatusTip(k)
                if v.favorite:
                    self.add_favorite_to_icon(item)
                self.side_menu_content.addItem(item)

    def filter_menu_booster(self, item):
        chosen = item.statusTip()
        self.side_menu_content.clear()
        self.side_menu_text.clear()
        self.display_favorite_tips_if_needed(chosen)

        for k, v in self.builder.boosters.items():
            if v.equipped:
                # already equipped, do not show
                continue
            if chosen == "All" or chosen == v.type or (chosen == "Favorite" and v.favorite) or k == "Empty":
                if k == "Empty":
                    item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
                else:
                    item = QListWidgetItem(QIcon(u":/All/Booster/" + escape_filename(k) + ".png"), "")
                item.setStatusTip(k)
                if v.favorite:
                    self.add_favorite_to_icon(item)
                self.side_menu_content.addItem(item)

    def filter_menu_weapon(self, item):
        chosen = item.statusTip()
        self.side_menu_content.clear()
        self.side_menu_text.clear()
        self.display_favorite_tips_if_needed(chosen)

        for k, v in self.builder.weapons.items():
            if chosen == "All" or chosen == v.type or (chosen == "Favorite" and v.favorite) or k == "Empty":
                if k == "Empty":
                    item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
                else:
                    item = QListWidgetItem(QIcon(u":/All/Weapon/" + escape_filename(k) + ".png"), "")
                item.setStatusTip(k)
                if v.favorite:
                    self.add_favorite_to_icon(item)
                self.side_menu_content.addItem(item)

    def filter_menu_blood_code(self, item):
        chosen = item.text()
        self.side_menu_content.clear()
        self.side_menu_text.clear()
        self.display_favorite_tips_if_needed(chosen)

        for k, v in self.builder.blood_codes.items():
            if chosen == "All" or chosen == v.bloodline or (chosen == "Favorite" and v.favorite) or k == "Empty":
                if k == "Empty":
                    item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
                else:
                    item = QListWidgetItem(QIcon(u":/All/BloodCode/" + escape_filename(k) + ".png"), "")
                item.setStatusTip(k)
                if v.favorite:
                    self.add_favorite_to_icon(item)
                self.side_menu_content.addItem(item)

    def filter_menu_defensive(self, item):
        chosen = item.text()
        self.side_menu_content.clear()
        self.side_menu_text.clear()
        self.display_favorite_tips_if_needed(chosen)

        for k, v in self.builder.defensive_formae.items():
            if chosen == "All" or chosen == v.type or (chosen == "Favorite" and v.favorite) or k == "Empty":
                if k == "Empty":
                    item = QListWidgetItem(QIcon(u":/All/Transform/Transform_Off.png"), "")
                else:
                    item = QListWidgetItem(QIcon(u":/All/Defensive/" + escape_filename(k) + ".png"), "")
                item.setStatusTip(k)
                if v.favorite:
                    self.add_favorite_to_icon(item)
                self.side_menu_content.addItem(item)

    def display_favorite_tips_if_needed(self, selected):
        if selected == "Favorite":
            self.side_menu_text.insertHtml(f'<body><h2><p align="center">Favorites</p></h2><body>')
            self.side_menu_text.insertPlainText("Right click icon to add to favorites.\nRight click again to unfavorite.")

    def handle_unimplemented_clicked(self, item):
        print("clicked", item)

    def handle_dummy(self):
        pass

    def handle_transform_weapon_1_clicked(self, item):
        widget = self.tool_button_h2_v1_h1_1a
        self.handle_transform_weapon_clicked(widget, item, "Weapon_1")

    def handle_transform_weapon_2_clicked(self, item):
        widget = self.tool_button_h2_v2_h1_1a
        self.handle_transform_weapon_clicked(widget, item, "Weapon_2")

    def handle_transform_weapon_clicked(self, widget, item, slot):
        builder = self.builder
        weapon = builder.character.weapons[slot]
        transform = item.statusTip()
        if transform == "Off":
            transform = "Weapon_" + transform
        builder.commit_transaction(weapon, slot=slot, transform=transform)

    def handle_transform_defensive_clicked(self, item):
        builder = self.builder
        defensive = builder.character.defensive_forma
        transform = item.statusTip()
        if transform == "Off":
            transform = "Defensive_" + transform
        builder.commit_transaction(defensive, transform=transform)

    def handle_weapon_1_clicked(self, item):
        widget = self.tool_button_h2_v1_h1_1
        self.handle_weapon_clicked(widget, item, "Weapon_1")

    def handle_weapon_2_clicked(self, item):
        widget = self.tool_button_h2_v2_h1_1
        self.handle_weapon_clicked(widget, item, "Weapon_2")

    def handle_weapon_clicked(self, widget, item, slot):
        builder = self.builder
        weapon = builder.weapons[item.statusTip()]
        builder.commit_transaction(weapon, slot=slot, transform=builder.character.transform[slot])

    def update_weapon_icon_text(self, name, slot, transform):
        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        widget = self.builder.char_to_widget_mapping[slot]
        if name == "Weapon None":
            widget.setIcon(icon_1)
            widget.setText(slot.replace("_", " "))
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Weapon/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal,
                           QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 150)
            widget.setIcon(new_icon)
            widget.setText(name)

        widget = self.builder.char_to_widget_mapping[slot + "_Transform"]
        transform = transform.replace("Weapon_", "Transform_")
        icon_transform = QIcon()
        icon_transform.addFile(u":/All/Transform/" + escape_filename(transform) + ".png", QSize(),
                               QIcon.Mode.Normal,
                               QIcon.State.Off)
        widget.setIcon(icon_transform)

    def handle_blood_code_clicked(self, item):
        builder = self.builder
        blood_code = builder.blood_codes[item.statusTip()]
        builder.commit_transaction(blood_code)

    def update_blood_code_icon_text(self, name):
        widget = self.tool_button_h2_v3_h2_1
        if name == "Blood Code":
            new_icon = QIcon()
            new_icon.addFile(u":/All/UI/Slot_Blood_Code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            widget.setIcon(new_icon)
            widget.setText("Blood Code")
        else:
            new_icon = QIcon()
            new_icon.addFile(u":/All/BloodCode/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal,
                             QIcon.State.Off)
            widget.setIcon(new_icon)
            widget.setText(name)

    def handle_offensive_clicked(self, item):
        builder = self.builder
        offensive = builder.offensive_formae[item.statusTip()]
        builder.commit_transaction(offensive)

    def update_offensive_icon_text(self, name):
        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        widget = self.tool_button_h2_v3_h1_1
        if name == "Offensive":
            widget.setIcon(icon_1)
            widget.setText("Offensive")
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Offensive/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 150)
            widget.setIcon(new_icon)
            widget.setText(name)

    def handle_defensive_clicked(self, item):
        builder = self.builder
        defensive = builder.defensive_formae[item.statusTip()]
        builder.commit_transaction(defensive, transform=builder.character.transform["Defensive"])

    def update_defensive_icon_text(self, name, slot, transform):
        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        widget = self.tool_button_h2_v3_h1_2
        if name == "Defensive":
            widget.setIcon(icon_1)
            widget.setText("Defensive")
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Defensive/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal,
                           QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 150)
            widget.setIcon(new_icon)
            widget.setText(name)

        widget = self.tool_button_h2_v3_h1_2a
        transform = transform.replace("Defensive_", "Transform_")
        icon_transform = QIcon()
        icon_transform.addFile(u":/All/Transform/" + escape_filename(transform) + ".png", QSize(),
                               QIcon.Mode.Normal,
                               QIcon.State.Off)
        widget.setIcon(icon_transform)

    def handle_jail_clicked(self, item):
        builder = self.builder
        jail = builder.jails[item.statusTip()]
        builder.commit_transaction(jail)

    def update_jail_icon_text(self, name):
        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        widget = self.tool_button_h2_v3_h1_3
        if name == "Jail":
            widget.setIcon(icon_1)
            widget.setText("Jail")
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Jail/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 150)
            widget.setIcon(new_icon)
            widget.setText(name)

    def handle_booster_1_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_1
        self.handle_booster_clicked(widget, item, "Booster_1")

    def handle_booster_2_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_2
        self.handle_booster_clicked(widget, item, "Booster_2")

    def handle_booster_3_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_3
        self.handle_booster_clicked(widget, item, "Booster_3")

    def handle_booster_4_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_4
        self.handle_booster_clicked(widget, item, "Booster_4")

    def handle_booster_5_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_5
        self.handle_booster_clicked(widget, item, "Booster_5")

    def handle_booster_6_clicked(self, item):
        widget = self.push_button_h2_v3_h2_v1_6
        self.handle_booster_clicked(widget, item, "Booster_6")

    def handle_booster_clicked(self, widget, item, slot):
        builder = self.builder
        booster = builder.boosters[item.statusTip()]
        builder.commit_transaction(booster, slot=slot)

        # disable for easier troubleshooting
        # selected_filter = self.side_menu_buttons.selectedItems()
        # if selected_filter:
        #     # do a soft-refresh of booster side menu content
        #     # to remove currently selected booster from the list and to add previously selected booster (if any)
        #     # ensures previously selected booster can be selected again without re-opening the side menu
        #     #
        #     # removing item from the list will destroy it, so should be called after it's last usage
        #     self.filter_menu_booster(selected_filter[0])

    def update_boosters_icon_text(self, booster, slot):
        name = booster.name
        active = booster.active
        print("      handle_booster_clicked", active)
        print("      bloodline", self.builder.character.bloodline)

        widget = self.builder.char_to_widget_mapping[slot]
        self.set_booster_icon(widget, name, active)
        if name == "Booster None":
            widget.setText(slot.replace("_", " ") + ": None")
        else:
            widget.setText(name)

    def handle_forma_1_weapon_1_clicked(self, item):
        widget = self.push_button_h2_v1_1
        self.handle_forma_clicked(widget, item, "Weapon_1_Forma_1")

    def handle_forma_2_weapon_1_clicked(self, item):
        widget = self.push_button_h2_v1_2
        self.handle_forma_clicked(widget, item, "Weapon_1_Forma_2")

    def handle_forma_3_weapon_1_clicked(self, item):
        widget = self.push_button_h2_v1_3
        self.handle_forma_clicked(widget, item, "Weapon_1_Forma_3")

    def handle_forma_4_weapon_1_clicked(self, item):
        widget = self.push_button_h2_v1_4
        self.handle_forma_clicked(widget, item, "Weapon_1_Forma_4")

    def handle_forma_1_weapon_2_clicked(self, item):
        widget = self.push_button_h2_v2_1
        self.handle_forma_clicked(widget, item, "Weapon_2_Forma_1")

    def handle_forma_2_weapon_2_clicked(self, item):
        widget = self.push_button_h2_v2_2
        self.handle_forma_clicked(widget, item, "Weapon_2_Forma_2")

    def handle_forma_3_weapon_2_clicked(self, item):
        widget = self.push_button_h2_v2_3
        self.handle_forma_clicked(widget, item, "Weapon_2_Forma_3")

    def handle_forma_4_weapon_2_clicked(self, item):
        widget = self.push_button_h2_v2_4
        self.handle_forma_clicked(widget, item, "Weapon_2_Forma_4")

    def handle_forma_clicked(self, widget, item, slot):
        builder = self.builder
        forma = builder.formae[item.statusTip()]
        builder.commit_transaction(forma, slot=slot)

    def update_forma_icon_text(self, name, slot):
        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Forma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        widget = self.builder.char_to_widget_mapping[slot]
        if name == "Forma None":
            widget.setIcon(icon_1)
            idx = slot.find("Forma")
            default_text = slot[idx:].replace("_", " ") + ": None"
            widget.setText(default_text)
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Forma/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 30)
            widget.setIcon(new_icon)
            widget.setText(name)

    def handle_hover(self, data, detailed=False):
        data_hover_text = data.get_hover_text(detailed)
        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(data_hover_text)

    # TODO consider putting inverted state as alternate icon state, to make switching more efficient
    def set_booster_icon(self, widget, name, active):
        print("  set_booster_icon", widget, name, active)

        icon_1 = QIcon()
        icon_1.addFile(u":/All/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        if name == "Booster None":
            widget.setIcon(icon_1)
        else:
            icon_2 = QIcon()
            icon_2.addFile(u":/All/Booster/" + escape_filename(name) + ".png", QSize(), QIcon.Mode.Normal,
                           QIcon.State.Off)
            new_icon = self.merge_icons(icon_1, icon_2, 30, invert=not active)
            widget.setIcon(new_icon)

    # could not find a way to overlay weapon icon over button icon with PyQt stylesheets
    # (such that it looks good and button remains clickable)
    # merge icons instead to accomplish this
    def merge_icons(self, icon_1, icon_2, size_1, size_2=None, invert=False):
        if not size_2:
            size_2 = size_1

        pixmap_1 = icon_1.pixmap(size_1, QIcon.Mode.Normal, QIcon.State.Off)
        pixmap_2 = icon_2.pixmap(size_2, QIcon.Mode.Normal, QIcon.State.Off)
        image_1 = pixmap_1.toImage()
        image_2 = pixmap_2.toImage()

        # draw image 2 on top of image 1
        painter = QPainter(image_1)
        painter.drawImage(0, 0, image_2)
        painter.end()

        if invert:
            image_1.invertPixels()
        pixmap_3 = QPixmap.fromImage(image_1)
        icon_3 = QIcon()
        icon_3.addPixmap(pixmap_3, QIcon.Mode.Normal, QIcon.State.Off)
        return icon_3

    # merge original icon with favorite icon
    # save original icon pixmap as another pixmap (for mode, state which aren't used for anything)
    def add_favorite_to_icon(self, item):
        icon_1 = item.icon()
        size_1 = self.side_menu_content.iconSize()
        icon_2 = QIcon(u":/All/UI/Menu_Favorite.png")
        size_2 = size_1 / 3
        new_icon = self.merge_icons(icon_1, icon_2, size_1, size_2)

        pixmap_1 = icon_1.pixmap(size_1, QIcon.Mode.Normal, QIcon.State.Off)
        new_icon.addPixmap(pixmap_1, QIcon.Mode.Disabled, QIcon.State.On)
        item.setIcon(new_icon)

    # restore original icon pixmap (from mode, state which aren't used for anything)
    def remove_favorite_from_icon(self, item):
        icon_1 = item.icon()
        size_1 = self.side_menu_content.iconSize()

        pixmap_1 = icon_1.pixmap(size_1, QIcon.Mode.Disabled, QIcon.State.On)
        new_icon = QIcon(pixmap_1)
        item.setIcon(new_icon)

    def calculate_buttons_end(self):
        # calculate y position of end of visible content for side menu buttons

        # find y position of item placed in last row of buttons
        # find height of tallest item placed in last row of buttons
        last_row_y = 0
        last_row_height = 0
        for idx in range(self.side_menu_buttons.count()):
            item = self.side_menu_buttons.item(idx)
            item_rect = self.side_menu_buttons.visualItemRect(item)

            if item_rect.y() > last_row_y:
                last_row_y = item_rect.y()
                last_row_height = item_rect.height()

            elif item_rect.y() == last_row_y:
                last_row_y = item_rect.y()
                if last_row_height < item_rect.height():
                    last_row_height = item_rect.height()

        # last_row_y is position of top left corner of rectangle, change it to bottom left corner by adding height
        # also need to account for margins, only the top one because bottom one is 0
        return last_row_y + last_row_height + self.margin_size

    def set_character_to_widget_mapping(self):
        self.builder.widget_to_char_mapping = {
            # Blood Code
            self.tool_button_h2_v3_h2_1: "Blood_Code",
            self.push_button_h2_v3_h2_v1_7: "Trait_1",
            self.push_button_h2_v3_h2_v1_8: "Trait_2",
            self.push_button_h2_v3_h2_v1_9: "Trait_3",
            self.label_h3_v1_g1_1: "Attribute_Strength",
            self.label_h3_v1_g1_2: "Attribute_Dexterity",
            self.label_h3_v1_g1_3: "Attribute_Mind",
            self.label_h3_v1_g1_4: "Attribute_Willpower",
            self.label_h3_v1_g1_5: "Attribute_Fortitude",
            self.label_h3_v1_g1_6: "Attribute_Vitality",
            self.progress_bar_h3_v1_g1_1: "Burden_Strength",
            self.progress_bar_h3_v1_g1_2: "Burden_Dexterity",
            self.progress_bar_h3_v1_g1_3: "Burden_Mind",
            self.progress_bar_h3_v1_g1_4: "Burden_Willpower",
            self.progress_bar_h3_v1_g1_5: "Burden_Fortitude",
            self.progress_bar_h3_v1_g1_6: "Burden_Vitality",

            # Weapon 1
            self.tool_button_h2_v1_h1_1: "Weapon_1",
            self.tool_button_h2_v1_h1_1a: "Weapon_1_Transform",
            self.label_h2_v3_h1_g1_5: "Weapon_1_Bleed",
            self.label_h2_v1_h1_g1_5: "Weapon_1_Reliability",
            self.label_h2_v1_h1_g1_6: "Weapon_1_Handling",
            self.label_h2_v1_h1_g1_7: "Weapon_1_Conversion",
            self.label_h2_v1_h1_g1_8: "Weapon_1_Conductivity",
            self.label_h2_v1_h1_g1_13: "Weapon_1_Reliability_Max",
            self.label_h2_v1_h1_g1_14: "Weapon_1_Handling_Max",
            self.label_h2_v1_h1_g1_15: "Weapon_1_Conversion_Max",
            self.label_h2_v1_h1_g1_16: "Weapon_1_Conductivity_Max",
            self.push_button_h2_v1_1: "Weapon_1_Forma_1",
            self.push_button_h2_v1_2: "Weapon_1_Forma_2",
            self.push_button_h2_v1_3: "Weapon_1_Forma_3",
            self.push_button_h2_v1_4: "Weapon_1_Forma_4",

            # Weapon 2
            self.tool_button_h2_v2_h1_1: "Weapon_2",
            self.tool_button_h2_v2_h1_1a: "Weapon_2_Transform",
            self.label_h2_v3_h1_g1_6: "Weapon_2_Bleed",
            self.label_h2_v2_h1_g1_5: "Weapon_2_Reliability",
            self.label_h2_v2_h1_g1_6: "Weapon_2_Handling",
            self.label_h2_v2_h1_g1_7: "Weapon_2_Conversion",
            self.label_h2_v2_h1_g1_8: "Weapon_2_Conductivity",
            self.label_h2_v2_h1_g1_13: "Weapon_2_Reliability_Max",
            self.label_h2_v2_h1_g1_14: "Weapon_2_Handling_Max",
            self.label_h2_v2_h1_g1_15: "Weapon_2_Conversion_Max",
            self.label_h2_v2_h1_g1_16: "Weapon_2_Conductivity_Max",
            self.push_button_h2_v2_1: "Weapon_2_Forma_1",
            self.push_button_h2_v2_2: "Weapon_2_Forma_2",
            self.push_button_h2_v2_3: "Weapon_2_Forma_3",
            self.push_button_h2_v2_4: "Weapon_2_Forma_4",

            # Offensive
            self.tool_button_h2_v3_h1_1: "Offensive",
            self.label_h2_v3_h1_g1_7: "Offensive_Bleed",

            # Defensive
            self.tool_button_h2_v3_h1_2: "Defensive",
            self.tool_button_h2_v3_h1_2a: "Defensive_Transform",

            # Jail
            self.tool_button_h2_v3_h1_3: "Jail",

            # Booster
            self.push_button_h2_v3_h2_v1_1: "Booster_1",
            self.push_button_h2_v3_h2_v1_2: "Booster_2",
            self.push_button_h2_v3_h2_v1_3: "Booster_3",
            self.push_button_h2_v3_h2_v1_4: "Booster_4",
            self.push_button_h2_v3_h2_v1_5: "Booster_5",
            self.push_button_h2_v3_h2_v1_6: "Booster_6",

            # Defense
            self.tool_button_h4_1: "Defense_Slash",
            self.tool_button_h4_2: "Defense_Crush",
            self.tool_button_h4_3: "Defense_Pierce",
            self.tool_button_h4_4: "Defense_Blood",
            self.tool_button_h4_5: "Defense_Fire",
            self.tool_button_h4_6: "Defense_Ice",
            self.tool_button_h4_7: "Defense_Lightning",

            # Guarding Defense
            self.tool_button_h5_1: "GuardingDefense_Slash",
            self.tool_button_h5_2: "GuardingDefense_Crush",
            self.tool_button_h5_3: "GuardingDefense_Pierce",
            self.tool_button_h5_4: "GuardingDefense_Blood",
            self.tool_button_h5_5: "GuardingDefense_Fire",
            self.tool_button_h5_6: "GuardingDefense_Ice",
            self.tool_button_h5_7: "GuardingDefense_Lightning",

            # Resistances
            self.tool_button_h6_1: "Resistance_Disease",
            self.tool_button_h6_2: "Resistance_Wound",
            self.tool_button_h6_3: "Resistance_Bleed",
            self.tool_button_h6_4: "Resistance_Curse",

            # Misc
            self.label_h2_v3_h1_g1_8: "Balance",
            self.tool_button_h3_g1_2: "Dodge_Effectiveness",
            self.tool_button_h3_g1_4: "StaminaGuardCost",
            self.tool_button_h1_2: "Ichor",
        }
        self.builder.char_to_widget_mapping = dict((v, k) for k, v in self.builder.widget_to_char_mapping.items())

    def add_menu_bar(self, MainWindow):
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1440, 21))
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)

        # build submenu
        self.menuBuild = QMenu(self.menubar)
        self.menuBuild.setObjectName(u"menuBuild")
        self.menubar.addAction(self.menuBuild.menuAction())

        self.action_load_build_file = QAction(MainWindow)
        self.action_load_build_file.setObjectName(u"action_load_build_file")
        self.action_load_build_code = QAction(MainWindow)
        self.action_load_build_code.setObjectName(u"action_load_build_code")
        self.action_load_favorites_file = QAction(MainWindow)
        self.action_load_favorites_file.setObjectName(u"action_load_favorites_file")
        self.action_save_build_file = QAction(MainWindow)
        self.action_save_build_file.setObjectName(u"action_save_build_file")
        self.action_save_build_code = QAction(MainWindow)
        self.action_save_build_code.setObjectName(u"action_save_build_code")
        self.action_save_favorites_file = QAction(MainWindow)
        self.action_save_favorites_file.setObjectName(u"action_save_favorites_file")

        self.action_load_build_file.triggered.connect(self.load_build_file)
        self.action_load_build_code.triggered.connect(self.load_build_code)
        self.action_load_favorites_file.triggered.connect(self.load_favorites_file)
        self.action_save_build_file.triggered.connect(self.save_build_file)
        self.action_save_build_code.triggered.connect(self.save_build_code)
        self.action_save_favorites_file.triggered.connect(self.save_favorites_file)

        self.menuBuild.addAction(self.action_load_build_file)
        self.menuBuild.addAction(self.action_load_build_code)
        self.menuBuild.addAction(self.action_load_favorites_file)
        self.menuBuild.addAction(self.action_save_build_file)
        self.menuBuild.addAction(self.action_save_build_code)
        self.menuBuild.addAction(self.action_save_favorites_file)

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

    def load_build_file(self):
        filepath, extension = QFileDialog.getOpenFileName(self, 'Open file', "", "*.txt")
        if not filepath:
            self.show_message("Cannot open file.")
            return

        with open(filepath, "r") as _file:
            code = _file.read()
            self.handle_build_load(code)

    def load_build_code(self):
        widget = QInputDialog()
        widget.resize(600, 600)
        widget.setWindowTitle(VERSION)
        widget.setInputMode(QInputDialog.TextInput)
        widget.setLabelText("Enter build code")

        ok = widget.exec_()
        if ok:
            code = widget.textValue()
            self.handle_build_load(code)

    def save_build_file(self):
        code = self.generate_build_code()

    def save_build_code(self):
        code = self.generate_build_code()

        widget = QInputDialog()
        widget.resize(600, 600)
        widget.setWindowTitle(VERSION)
        widget.setInputMode(QInputDialog.TextInput)
        widget.setLabelText("Code generated successfully.")
        line_edit = widget.findChild(QLineEdit)
        if line_edit:
            line_edit.setText(code)

        widget.exec_()

    def load_favorites_file(self):
        pass

    def save_favorites_file(self):
        pass

    def handle_build_load(self, code):
        print(code)

        # check length
        if len(code) != 80:
            self.show_message("Build loading aborted, invalid code length (%d). Should be 80." % len(code))
            return

        # check allowed characters
        allowed_regex = "[0-9a-fA-F]+"
        match = re.match(allowed_regex, code)
        if match:
            if len(match.group(0)) != len(code):
                self.show_message("Build loading aborted, code contains forbidden characters.")
                return

        # check checksum, that every separate element summed adds up to 80000
        # TODO

        # proper handling
        # legal = code[0:2]
        blood_code = code[2:4]
        weapon_1 = code[4:7]
        weapon_2 = code[7:10]
        weapon_1_transform = code[10:12]
        weapon_2_transform = code[12:14]
        weapon_1_forma_1 = code[14:17]
        weapon_1_forma_2 = code[17:20]
        weapon_1_forma_3 = code[20:23]
        weapon_1_forma_4 = code[23:26]
        weapon_2_forma_1 = code[26:29]
        weapon_2_forma_2 = code[29:32]
        weapon_2_forma_3 = code[32:35]
        weapon_2_forma_4 = code[35:38]
        offensive = code[38:40]
        defensive = code[40:42]
        defensive_transform = code[42:44]
        jail = code[44:46]
        booster_1 = code[46:49]
        booster_2 = code[49:52]
        booster_3 = code[52:55]
        booster_4 = code[55:58]
        booster_5 = code[58:61]
        booster_6 = code[61:64]
        partner = code[64:66]
        # food_1 = code[66:68]
        # food_2 = code[68:70]
        # placeholder_1 = code[70:72]
        # placeholder_1 = code[72:75]
        checksum = code[75:80]

        # print(checksum)

        build_save_order = self.builder.build_save_order

        # if anything is "00" say there's a problem? and empty will be loaded instead
        builder = self.builder

        blood_code = build_save_order["BloodCode"].get(blood_code)
        if blood_code:
            blood_code = builder.blood_codes[blood_code]
            print(blood_code)
            builder.start_transaction(blood_code)
            builder.commit_transaction(blood_code)
        else:
            blood_code = BloodCode()
            print(blood_code)

        weapon_1_transform = build_save_order["Transform_Weapon"].get(weapon_1_transform)
        if not weapon_1_transform:
            weapon_1_transform = "Weapon_Off"
            print(weapon_1_transform)

        weapon_2_transform = build_save_order["Transform_Weapon"].get(weapon_2_transform)
        if not weapon_2_transform:
            weapon_2_transform = "Weapon_Off"
            print(weapon_2_transform)

        defensive_transform = build_save_order["Transform_Defensive"].get(defensive_transform)
        if not defensive_transform:
            defensive_transform = "Defensive_Off"
            print(defensive_transform)

        weapon_1 = build_save_order["Weapon"].get(weapon_1)
        if weapon_1:
            weapon_1 = builder.weapons[weapon_1]
            print(weapon_1)
            builder.start_transaction(weapon_1, "Weapon_1", weapon_1_transform)
            builder.commit_transaction(weapon_1, "Weapon_1", weapon_1_transform)
        else:
            weapon_1 = Weapon()
            print(weapon_1)

        weapon_2 = build_save_order["Weapon"].get(weapon_2)
        if weapon_2:
            weapon_2 = builder.weapons[weapon_2]
            print(weapon_2)
            builder.start_transaction(weapon_2, "Weapon_2", weapon_2_transform)
            builder.commit_transaction(weapon_2, "Weapon_2", weapon_2_transform)
        else:
            weapon_2 = Weapon()
            print(weapon_2)

        formae = [
            (weapon_1_forma_1, "Weapon_1_Forma_1"),
            (weapon_1_forma_2, "Weapon_1_Forma_2"),
            (weapon_1_forma_3, "Weapon_1_Forma_3"),
            (weapon_1_forma_4, "Weapon_1_Forma_4"),
            (weapon_2_forma_1, "Weapon_2_Forma_1"),
            (weapon_2_forma_2, "Weapon_2_Forma_2"),
            (weapon_2_forma_3, "Weapon_2_Forma_3"),
            (weapon_2_forma_4, "Weapon_2_Forma_4"),
        ]
        for forma, slot in formae:
            forma = build_save_order["Forma"].get(forma)
            if forma:
                forma = builder.formae[forma]
                print(forma)
                builder.start_transaction(forma, slot)
                builder.commit_transaction(forma, slot)
            else:
                forma = Forma()
                print(forma)

        offensive = build_save_order["Offensive"].get(offensive)
        if offensive:
            offensive = builder.offensive_formae[offensive]
            print(offensive)
            builder.start_transaction(offensive)
            builder.commit_transaction(offensive)
        else:
            offensive = Offensive()
            print(offensive)

        defensive = build_save_order["Defensive"].get(defensive)
        if defensive:
            defensive = builder.defensive_formae[defensive]
            print(defensive)
            builder.start_transaction(defensive, "", defensive_transform)
            builder.commit_transaction(defensive, "", defensive_transform)
        else:
            defensive = Defensive()
            print(defensive)

        jail = build_save_order["Jail"].get(jail)
        if jail:
            jail = builder.jails[jail]
            print(jail)
            builder.start_transaction(jail)
            builder.commit_transaction(jail)
        else:
            jail = Jail()
            print(jail)

        # todo
        #     booster active status seems to have issues on loading
        #     some issues could be expected since resolving booster effects
        #     is not implemented for non-booster item selection (and it should be)
        #
        #     however on loading boosters are loaded last, so it shouldn't matter here
        boosters = [
            (booster_1, "Booster_1"),
            (booster_2, "Booster_2"),
            (booster_3, "Booster_3"),
            (booster_4, "Booster_4"),
            (booster_5, "Booster_5"),
            (booster_6, "Booster_6"),
        ]
        for booster, slot in boosters:
            booster = build_save_order["Booster"].get(booster)
            if booster:
                booster = builder.boosters[booster]
                print(booster)
                builder.start_transaction(booster, slot)
                builder.commit_transaction(booster, slot)
            else:
                booster = Booster()
                print(booster)

        self.show_message("Build loaded successfully.")

    def generate_build_code(self):
        items = [
            "00",  # todo legal / illegal
            self.builder.character.blood_code,
            self.builder.character.weapons["Weapon_1"],
            self.builder.character.weapons["Weapon_2"],
            "Transform_Weapon_1",
            "Transform_Weapon_2",
            self.builder.character.formae["Weapon_1_Forma_1"],
            self.builder.character.formae["Weapon_1_Forma_2"],
            self.builder.character.formae["Weapon_1_Forma_3"],
            self.builder.character.formae["Weapon_1_Forma_4"],
            self.builder.character.formae["Weapon_2_Forma_1"],
            self.builder.character.formae["Weapon_2_Forma_2"],
            self.builder.character.formae["Weapon_2_Forma_3"],
            self.builder.character.formae["Weapon_2_Forma_4"],
            self.builder.character.offensive_forma,
            self.builder.character.defensive_forma,
            "Transform_Defensive",
            self.builder.character.jail,
            self.builder.character.boosters["Booster_1"],
            self.builder.character.boosters["Booster_2"],
            self.builder.character.boosters["Booster_3"],
            self.builder.character.boosters["Booster_4"],
            self.builder.character.boosters["Booster_5"],
            self.builder.character.boosters["Booster_6"],
            "00", # partner
            "00", # food 1
            "00", # food 2
            "00", # placeholder 1
            "000", # place holder 1
            "00000"  # todo checksum
        ]

        build_save_order = self.builder.build_save_order
        code = ""

        for item in items:
            if isinstance(item, str):
                if "Weapon" in item:
                    type_data = build_save_order["Transform_Weapon"]
                elif "Defensive" in item:
                    type_data = build_save_order["Transform_Defensive"]
                else:
                    type_data = dict()

                if type_data:
                    # transform
                    slot = item.replace("Transform_", "")
                    transform = self.builder.character.transform[slot]
                    matching_item_id = next((k for k, v in type_data.items() if v == transform), None)
                    if matching_item_id:
                        code += matching_item_id
                    else:
                        code += "00"
                else:
                    # any other string
                    code += item
            else:
                type_key = type(item).__name__
                if type_key == "OffensiveForma" or type_key == "DefensiveForma":
                    type_key = type_key.replace("Forma", "")

                type_data = build_save_order[type_key]
                if item.description == "":
                    # empty, TODO add "empty" variable to each game data class ?
                    matching_item_id = next((k for k, v in type_data.items() if v == "Empty"), None)
                else:
                    matching_item_id = next((k for k, v in type_data.items() if v == item.name), None)

                if matching_item_id:
                    code += matching_item_id
                else:
                    if type(item) in ["Weapon", "Forma", "Booster"]:
                        desired_length = 3
                    else:
                        desired_length = 2
                    code += "".join(["0" for x in range(desired_length)])

            # code += " "  # for easier troubleshooting

        return code

    def show_message(self, text, informative_text=None, title=" "):
        msg = QMessageBox()
        msg.setText(text)
        if informative_text:
            msg.setInformativeText(informative_text)
        msg.setWindowTitle(title)
        msg.exec_()

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

        # menu build
        self.menuBuild.setTitle(QCoreApplication.translate("MainWindow", u"Build", None))
        self.action_load_build_file.setText(QCoreApplication.translate("MainWindow", u"Load build from file", None))
        self.action_load_build_code.setText(QCoreApplication.translate("MainWindow", u"Load build from code", None))
        self.action_load_favorites_file.setText(QCoreApplication.translate("MainWindow", u"Load favorites from file", None))
        self.action_save_build_file.setText(QCoreApplication.translate("MainWindow", u"Save build to file", None))
        self.action_save_build_code.setText(QCoreApplication.translate("MainWindow", u"Save build to code", None))
        self.action_save_favorites_file.setText(QCoreApplication.translate("MainWindow", u"Save fovorites to file", None))

        # menu window
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuSize.setTitle(QCoreApplication.translate("MainWindow", u"Size", None))
        self.action960x540.setText(QCoreApplication.translate("MainWindow", u"960x540", None))
        self.action1440x810.setText(QCoreApplication.translate("MainWindow", u"1440x810", None))
        self.action1920x1080.setText(QCoreApplication.translate("MainWindow", u"1920x1080", None))
        self.action2880x1620.setText(QCoreApplication.translate("MainWindow", u"2880x1620", None))
        self.action3840x2160.setText(QCoreApplication.translate("MainWindow", u"3840x2160", None))


class AttributeProgressBar(QProgressBar):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        r = self.rect().adjusted(2, 2, -2, -2)
        skew = 10

        # Base shape
        border = QPolygonF([
            QPointF(r.left() + skew, r.top()),
            QPointF(r.right(), r.top()),
            QPointF(r.right() - skew, r.bottom()),
            QPointF(r.left(), r.bottom())
        ])

        # Progress shape
        if self.maximum() == 0:
            progress = 1
        else:
            progress = self.value() / self.maximum()
        skewed_width = border[2].x() - border[3].x()
        fill_width = skewed_width * progress + skew
        fill = QPolygonF([
            QPointF(r.left() + skew, r.top()),
            QPointF(r.left() + fill_width, r.top()),
            QPointF(r.left() + fill_width - skew, r.bottom()),
            QPointF(r.left(), r.bottom())
        ])
        painter.setPen(QColor("#95abbc"))
        painter.setBrush(QColor("#95abbc"))
        # painter.setPen(Qt.GlobalColor.red)  # debug
        # painter.setBrush(Qt.GlobalColor.red)  # debug
        painter.drawPolygon(fill)

        # Color border and background colored border (color on top of background)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(QColor("#171717"), 8))
        painter.drawPolygon(border)
        painter.setPen(QPen(QColor("#6d7981"), 2))
        painter.drawPolygon(border)

        # Progress text
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(r, Qt.AlignmentFlag.AlignCenter, f"{self.value()}")


class MyQPushButton(QPushButton):
    button_type = ""
    data_mapping = None
    data = None

    def __init__(self, parent):
        super(MyQPushButton, self).__init__(parent)
        self.data_mapping = {
            "Forma": parent.window().builder.formae,
            "Booster": parent.window().builder.boosters,
            "BloodCode": parent.window().builder.blood_codes,  # traits
        }

    def set_button_type(self, type):
        self.button_type = type

        data = self.data_mapping.get(type)
        if data:
            self.data = data
        else:
            self.data = None

    # triggers on mouseover, like itemEntered
    def enterEvent(self, QEvent):
        if self.data:
            item = self.data.get(self.text())
            if item:
                self.window().side_menu_buttons.setVisible(True)
                self.window().side_menu_content.setVisible(True)
                self.window().side_menu_text.setVisible(True)
                self.window().handle_hover(item, detailed=True)


class MyQToolButton(QToolButton):
    button_type = ""
    data_mapping = None
    data = None

    def __init__(self, parent):
        super(MyQToolButton, self).__init__(parent)
        self.data_mapping = {
            "Weapon": parent.window().builder.weapons,
            "BloodCode": parent.window().builder.blood_codes,
            "Defensive": parent.window().builder.defensive_formae,
            "Offensive": parent.window().builder.offensive_formae,
            "Jail": parent.window().builder.jails,
        }

    def set_button_type(self, type):
        self.button_type = type

        data = self.data_mapping.get(type)
        if data:
            self.data = data
        else:
            self.data = None

    # triggers on mouseover, like itemEntered
    def enterEvent(self, QEvent):
        if self.data:
            item = self.data.get(self.text())
            if item:
                self.window().side_menu_buttons.setVisible(True)
                self.window().side_menu_content.setVisible(True)
                self.window().side_menu_text.setVisible(True)
                self.window().handle_hover(item, detailed=True)


class MyQListWidget(QListWidget):
    menu_type = ""
    menu_data = None
    menu_data_mapping = None
    hovered_item = None

    def __init__(self, parent):
        super(MyQListWidget, self).__init__()
        self.menu_data_mapping = {
            "Forma": parent.window().builder.formae,
            "Booster": parent.window().builder.boosters,
            "Weapon": parent.window().builder.weapons,
            "BloodCode": parent.window().builder.blood_codes,
            "Defensive": parent.window().builder.defensive_formae,
            "Offensive": parent.window().builder.offensive_formae,
            "Jail": parent.window().builder.jails,
        }

    def set_menu_type(self, menu):
        self.menu_type = menu

        menu_data = self.menu_data_mapping.get(menu)
        if menu_data:
            self.menu_data = menu_data
        else:
            self.menu_data = None

    def handle_forma_1_weapon_1_hover(self, item):
        self.handle_forma_hover(item, "Weapon_1_Forma_1")

    def handle_forma_2_weapon_1_hover(self, item):
        self.handle_forma_hover(item, "Weapon_1_Forma_2")

    def handle_forma_3_weapon_1_hover(self, item):
        self.handle_forma_hover(item, "Weapon_1_Forma_3")

    def handle_forma_4_weapon_1_hover(self, item):
        self.handle_forma_hover(item, "Weapon_1_Forma_4")

    def handle_forma_1_weapon_2_hover(self, item):
        self.handle_forma_hover(item, "Weapon_2_Forma_1")

    def handle_forma_2_weapon_2_hover(self, item):
        self.handle_forma_hover(item, "Weapon_2_Forma_2")

    def handle_forma_3_weapon_2_hover(self, item):
        self.handle_forma_hover(item, "Weapon_2_Forma_3")

    def handle_forma_4_weapon_2_hover(self, item):
        self.handle_forma_hover(item, "Weapon_2_Forma_4")

    def handle_forma_hover(self, item, slot):
        builder = self.window().builder
        forma = builder.formae[item.statusTip()]
        self.handle_hover(forma)

        builder.rollback_transaction()
        builder.start_transaction(forma, slot=slot)

    def handle_booster_1_hover(self, item):
        self.handle_booster_hover(item, "Booster_1")

    def handle_booster_2_hover(self, item):
        self.handle_booster_hover(item, "Booster_2")

    def handle_booster_3_hover(self, item):
        self.handle_booster_hover(item, "Booster_3")

    def handle_booster_4_hover(self, item):
        self.handle_booster_hover(item, "Booster_4")

    def handle_booster_5_hover(self, item):
        self.handle_booster_hover(item, "Booster_5")

    def handle_booster_6_hover(self, item):
        self.handle_booster_hover(item, "Booster_6")

    def handle_booster_hover(self, item, slot):
        builder = self.window().builder
        booster = builder.boosters[item.statusTip()]
        self.handle_hover(booster)

        builder.rollback_transaction()
        builder.start_transaction(booster, slot=slot)

    def handle_weapon_1_hover(self, item):
        self.handle_weapon_hover(item, "Weapon_1")

    def handle_weapon_2_hover(self, item):
        self.handle_weapon_hover(item, "Weapon_2")

    def handle_weapon_hover(self, item, slot):
        builder = self.window().builder
        weapon = builder.weapons[item.statusTip()]
        self.handle_hover(weapon)

        builder.rollback_transaction()
        builder.start_transaction(weapon, slot=slot, transform=builder.character.transform[slot])

    def handle_transform_weapon_1_hover(self, item):
        self.handle_transform_weapon_hover(item, "Weapon_1")

    def handle_transform_weapon_2_hover(self, item):
        self.handle_transform_weapon_hover(item, "Weapon_2")

    # TODO change to new hover format?
    def handle_transform_weapon_hover(self, item, slot):
        builder = self.window().builder
        weapon = builder.character.weapons[slot]
        transform = item.statusTip()
        if transform == "Off":
            transform = "Weapon_" + transform
        builder.rollback_transaction()
        builder.start_transaction(weapon, slot=slot, transform=transform)

        name = self.window().builder.translation[item.statusTip() + "_Name"]
        description = self.window().builder.translation[item.statusTip() + "_Description"]

        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(f'<body><h2><p align="center">{name}</p></h2><body>')
        self.window().side_menu_text.insertPlainText(description)

    # TODO change to new hover format?
    def handle_transform_defensive_hover(self, item):
        builder = self.window().builder
        defensive = builder.character.defensive_forma
        transform = item.statusTip()
        if transform == "Off":
            transform = "Defensive_" + transform
        builder.rollback_transaction()
        builder.start_transaction(defensive, transform=transform)

        name = self.window().builder.translation[item.statusTip() + "_Name"]
        description = self.window().builder.translation[item.statusTip() + "_Description"]

        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(f'<body><h2><p align="center">{name}</p></h2><body>')
        self.window().side_menu_text.insertPlainText(description)

    # this is only used to leaveEvent, and only updates the side text menu
    def handle_transform_hover(self, item):
        name = self.window().builder.translation[item.statusTip() + "_Name"]
        description = self.window().builder.translation[item.statusTip() + "_Description"]

        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(f'<body><h2><p align="center">{name}</p></h2><body>')
        self.window().side_menu_text.insertPlainText(description)

    def handle_blood_code_hover(self, item):
        builder = self.window().builder
        blood_code = builder.blood_codes[item.statusTip()]
        self.handle_hover(blood_code)

        builder.rollback_transaction()
        builder.start_transaction(blood_code)

    def handle_offensive_hover(self, item):
        builder = self.window().builder
        offensive = builder.offensive_formae[item.statusTip()]
        self.handle_hover(offensive)

        builder.rollback_transaction()
        builder.start_transaction(offensive)

    def handle_defensive_hover(self, item):
        builder = self.window().builder
        defensive = builder.defensive_formae[item.statusTip()]
        self.handle_hover(defensive)

        builder.rollback_transaction()
        builder.start_transaction(defensive, transform=builder.character.transform["Defensive"])

    def handle_jail_hover(self, item):
        builder = self.window().builder
        jail = builder.jails[item.statusTip()]
        self.handle_hover(jail)

        builder.rollback_transaction()
        builder.start_transaction(jail)

    def handle_hover(self, data):
        data_hover_text = data.get_hover_text()
        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(data_hover_text)

    def handle_hover_item(self, item):
        item_data = self.menu_data.get(item.statusTip())
        if not item_data:
            return

        # simplified hover text displayed after cursor leaves the menu
        self.window().side_menu_text.clear()
        self.window().side_menu_text.insertHtml(f'<body><h2><p align="center">{item_data.name}</p></h2><body>')
        self.window().side_menu_text.insertPlainText(item_data.description)

    def leaveEvent(self, QEvent):
        if not self.menu_type:
            return

        # ensure the text for selected item is displayed after cursor leaves the menu
        items = self.selectedItems()
        if items and items[0]:
            if self.menu_type == "Transform":
                self.handle_transform_hover(items[0])
            else:
                self.handle_hover_item(items[0])

        self.window().builder.rollback_transaction()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            super().mousePressEvent(QMouseEvent)

        elif QMouseEvent.button() == Qt.RightButton:
            if self.menu_type in ["Transform", "Offensive", "Jail"]:
                # no favorites
                return

            index = self.indexAt(QMouseEvent.position().toPoint())
            if index.isValid():
                item = self.itemFromIndex(index)
                item_data = self.menu_data.get(item.statusTip())
                if not item_data:
                    return

                if item_data.favorite:
                    item_data.favorite = False
                    self.window().remove_favorite_from_icon(item)
                else:
                    item_data.favorite = True
                    self.window().add_favorite_to_icon(item)

    def foo(self, item):
        pass
