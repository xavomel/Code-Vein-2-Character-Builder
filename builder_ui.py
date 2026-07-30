from PySide6.QtCore import QCoreApplication, QRect, Qt, QSize, QDir
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QWidget, QMenu, QMenuBar, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSpacerItem, \
    QSizePolicy, QToolButton, QPushButton, QProgressBar, QApplication
import resource


VERSION = u"Code Vein II Character Builder v0.0.1"


class Ui_MainWindow(object):
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
        QApplication.setFont(font_default, "QPushButton")
        QApplication.setFont(font_default, "QToolButton")

        # fonts - specific uses
        font_numbers_bleed = db.font("Pirata One", "Regular", 9)
        font_numbers_attribute = db.font("Science Gothic", "ExtraLight", 20)
        font_numbers_progress_bar = db.font("Science Gothic", "ExtraLight", 10)
        font_numbers_defense = db.font("Science Gothic", "Regular", 10)
        font_defensive_formae = db.font("Pirata One", "Regular", 28)

        # icons
        icon_slot_blood_code_size = QSize(150, 150)
        icon_slot_item_size = QSize(75, 75)
        icon_slot_forma_size = QSize(30, 30)
        icon_attribute_size = QSize(24, 24)
        icon_defense_size = QSize(24, 24)

        icon_slot_blood_code = QIcon()
        icon_slot_blood_code.addFile(u":/UI/Slot_Blood_Code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_slot_item = QIcon()
        icon_slot_item.addFile(u":/UI/Slot_Item.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_slot_forma = QIcon()
        icon_slot_forma.addFile(u":/UI/Slot_Forma", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_attribute_strength = QIcon()
        icon_attribute_strength.addFile(u":/UI/Attribute_Strength.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_dexterity = QIcon()
        icon_attribute_dexterity.addFile(u":/UI/Attribute_Dexterity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_mind = QIcon()
        icon_attribute_mind.addFile(u":/UI/Attribute_Mind", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_willpower = QIcon()
        icon_attribute_willpower.addFile(u":/UI/Attribute_Willpower.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_vitality = QIcon()
        icon_attribute_vitality.addFile(u":/UI/Attribute_Vitality.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_attribute_fortitude = QIcon()
        icon_attribute_fortitude.addFile(u":/UI/Attribute_Fortitude.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_defense_slash = QIcon()
        icon_defense_slash.addFile(u":/UI/Defense_Slash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_crush = QIcon()
        icon_defense_crush.addFile(u":/UI/Defense_Crush.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_pierce = QIcon()
        icon_defense_pierce.addFile(u":/UI/Defense_Pierce", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_blood = QIcon()
        icon_defense_blood.addFile(u":/UI/Defense_Blood.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_fire = QIcon()
        icon_defense_fire.addFile(u":/UI/Defense_Fire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_ice = QIcon()
        icon_defense_ice.addFile(u":/UI/Defense_Ice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_defense_thunder = QIcon()
        icon_defense_thunder.addFile(u":/UI/Defense_Thunder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_resistance_disease = QIcon()
        icon_resistance_disease.addFile(u":/UI/Resistance_Disease.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_wound = QIcon()
        icon_resistance_wound.addFile(u":/UI/Resistance_Wound.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_bleed = QIcon()
        icon_resistance_bleed.addFile(u":/UI/Resistance_Bleed", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon_resistance_curse = QIcon()
        icon_resistance_curse.addFile(u":/UI/Resistance_Curse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon_text_arrow = QIcon()
        icon_text_arrow.addFile(u":/UI/Text_Arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"""
                #centralwidget {
                    border-image: url(:/UI/Background1440.png) 0 0 0 0 stretch stretch;
                    background: black;
                }

                QLabel {
                    color: #c2c2c2; /*light grey*/
                }

                QToolButton {
                    color: #c2c2c2; /*light grey*/
                    border: none;
                    background: transparent;
                }

                QPushButton {
                    color: #c2c2c2; /*light grey*/
                    border: none;
                    background: transparent;
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

                #tool_button_h2_v1_h1_1, #tool_button_h2_v2_h1_1,
                #tool_button_h2_v3_h1_1, #tool_button_h2_v3_h1_2, #tool_button_h2_v3_h1_3 {
                    color: #abddea; /*cyan*/
                }

                #label_h1_2, #tool_button_h1_2 {
                    color: #afcbde; /*pale cyan*/
                }

                #label_h1_3, #tool_button_h1_3{
                    color: #00adf1; /*blue*/
                }

                #tool_button_h2_v3_h2_1,
                #label_h3_v1_g1_1, #label_h3_v1_g1_2, #label_h3_v1_g1_3, #label_h3_v1_g1_4, #label_h3_v1_g1_6,
                #label_h3_v1_g1_5,
                #tool_button_h4_1, #tool_button_h4_2, #tool_button_h4_3, #tool_button_h4_4, #tool_button_h4_5,
                #tool_button_h4_6, #tool_button_h4_7,
                #tool_button_h5_1, #tool_button_h5_2, #tool_button_h5_3, #tool_button_h5_4, #tool_button_h5_5,
                #tool_button_h5_6, #tool_button_h5_7 {
                    color: white
                }
            """)

        # main vertical layout
        self.main_vertical_layout_widget = QWidget(self.centralwidget)
        self.main_vertical_layout_widget.setObjectName(u"main_vertical_layout_widget")
        self.main_vertical_layout_widget.setGeometry(QRect(0, 0, 940, 810))
        self.main_vertical_layout = QVBoxLayout(self.main_vertical_layout_widget)
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.main_vertical_layout.setContentsMargins(0, 0, 0, 0)

        # 1st horizontal layout
        self.main_horizontal_layout_1 = QHBoxLayout()
        self.main_horizontal_layout_1.setObjectName(u"main_horizontal_layout_1")
        self.main_horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_1)

        # 1st horizontal layout content
        self.tool_button_h1_1 = QToolButton(self.main_vertical_layout_widget)
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

        self.tool_button_h1_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h1_2.setObjectName(u"tool_button_h1_2")
        self.tool_button_h1_2.setText(QCoreApplication.translate("MainWindow", u"29", None)) # move to re-translate
        self.tool_button_h1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.main_horizontal_layout_1.addWidget(self.tool_button_h1_2)

        self.horizontal_spacer_h1_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_horizontal_layout_1.addItem(self.horizontal_spacer_h1_2)

        self.label_h1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h1_3.setObjectName(u"label_h1_3")
        self.label_h1_3.setText(QCoreApplication.translate("MainWindow", u"Partner", None)) # move to re-translate
        self.main_horizontal_layout_1.addWidget(self.label_h1_3)

        self.tool_button_h1_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h1_3.setObjectName(u"tool_button_h1_3")
        self.tool_button_h1_3.setText(QCoreApplication.translate("MainWindow", u"Holly", None)) # move to re-translate
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
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_1)

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout
        self.horizontal_layout_h2_v1_1 = QHBoxLayout()
        self.horizontal_layout_h2_v1_1.setObjectName(u"horizontal_layout_h2_v1_1")
        self.horizontal_layout_h2_v1_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_1.addLayout(self.horizontal_layout_h2_v1_1)

        # 2nd horizontal layout content - vertical layout 1 content - buttons
        self.push_button_h2_v1_1 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_1.setObjectName(u"push_button_h2_v1_1")
        self.push_button_h2_v1_1.setText(QCoreApplication.translate("MainWindow", u"Forma 1", None)) # move to re-translate
        self.push_button_h2_v1_1.setIcon(icon_slot_forma)
        self.push_button_h2_v1_1.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v1_2 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_2.setObjectName(u"push_button_h2_v1_2")
        self.push_button_h2_v1_2.setText(QCoreApplication.translate("MainWindow", u"Forma 2", None)) # move to re-translate
        self.push_button_h2_v1_2.setIcon(icon_slot_forma)
        self.push_button_h2_v1_2.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v1_3 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_3.setObjectName(u"push_button_h2_v1_3")
        self.push_button_h2_v1_3.setText(QCoreApplication.translate("MainWindow", u"Forma 3", None)) # move to re-translate
        self.push_button_h2_v1_3.setIcon(icon_slot_forma)
        self.push_button_h2_v1_3.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v1_4 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v1_4.setObjectName(u"push_button_h2_v1_4")
        self.push_button_h2_v1_4.setText(QCoreApplication.translate("MainWindow", u"Forma 4", None)) # move to re-translate
        self.push_button_h2_v1_4.setIcon(icon_slot_forma)
        self.push_button_h2_v1_4.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_1.addWidget(self.push_button_h2_v1_4, 0, Qt.AlignmentFlag.AlignLeft)

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout content
        self.tool_button_h2_v1_h1_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v1_h1_1.setObjectName(u"tool_button_h2_v1_h1_1")
        self.tool_button_h2_v1_h1_1.setText(QCoreApplication.translate("MainWindow", u"Weapon 1", None)) # move to re-translate
        self.tool_button_h2_v1_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v1_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v1_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v1_1.addWidget(self.tool_button_h2_v1_h1_1)

        # 2nd horizontal layout content - vertical layout 1 content - horizontal layout content - grid layout
        self.grid_layout_h2_v1_h1_1 = QGridLayout()
        self.grid_layout_h2_v1_h1_1.setObjectName(u"grid_layout_h2_v1_h1_1")
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
        self.label_h2_v1_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_6.setObjectName(u"label_h2_v1_h1_g1_6")
        self.label_h2_v1_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_7.setObjectName(u"label_h2_v1_h1_g1_7")
        self.label_h2_v1_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_8.setObjectName(u"label_h2_v1_h1_g1_8")
        self.label_h2_v1_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

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
        self.label_h2_v1_h1_g1_13.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_14 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_14.setObjectName(u"label_h2_v1_h1_g1_14")
        self.label_h2_v1_h1_g1_14.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_15 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_15.setObjectName(u"label_h2_v1_h1_g1_15")
        self.label_h2_v1_h1_g1_15.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v1_h1_g1_16 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v1_h1_g1_16.setObjectName(u"label_h2_v1_h1_g1_16")
        self.label_h2_v1_h1_g1_16.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

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
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_2)

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout
        self.horizontal_layout_h2_v2_1 = QHBoxLayout()
        self.horizontal_layout_h2_v2_1.setObjectName(u"horizontal_layout_h2_v2_1")
        self.horizontal_layout_h2_v2_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_2.addLayout(self.horizontal_layout_h2_v2_1)

        # 2nd horizontal layout content - vertical layout 2 content - buttons
        self.push_button_h2_v2_1 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_1.setObjectName(u"push_button_h2_v2_1")
        self.push_button_h2_v2_1.setText(QCoreApplication.translate("MainWindow", u"Forma 1", None))  # move to re-translate
        self.push_button_h2_v2_1.setIcon(icon_slot_forma)
        self.push_button_h2_v2_1.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v2_2 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_2.setObjectName(u"push_button_h2_v2_2")
        self.push_button_h2_v2_2.setText(QCoreApplication.translate("MainWindow", u"Forma 2", None))  # move to re-translate
        self.push_button_h2_v2_2.setIcon(icon_slot_forma)
        self.push_button_h2_v2_2.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v2_3 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_3.setObjectName(u"push_button_h2_v2_3")
        self.push_button_h2_v2_3.setText(QCoreApplication.translate("MainWindow", u"Forma 3", None))  # move to re-translate
        self.push_button_h2_v2_3.setIcon(icon_slot_forma)
        self.push_button_h2_v2_3.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.push_button_h2_v2_4 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v2_4.setObjectName(u"push_button_h2_v2_4")
        self.push_button_h2_v2_4.setText(QCoreApplication.translate("MainWindow", u"Forma 4", None))  # move to re-translate
        self.push_button_h2_v2_4.setIcon(icon_slot_forma)
        self.push_button_h2_v2_4.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_2.addWidget(self.push_button_h2_v2_4, 0, Qt.AlignmentFlag.AlignLeft)

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout content
        self.tool_button_h2_v2_h1_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v2_h1_1.setObjectName(u"tool_button_h2_v2_h1_1")
        self.tool_button_h2_v2_h1_1.setText(QCoreApplication.translate("MainWindow", u"Weapon 2", None))  # move to re-translate
        self.tool_button_h2_v2_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v2_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v2_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v2_1.addWidget(self.tool_button_h2_v2_h1_1)

        # 2nd horizontal layout content - vertical layout 2 content - horizontal layout content - grid layout
        self.grid_layout_h2_v2_h1_1 = QGridLayout()
        self.grid_layout_h2_v2_h1_1.setObjectName(u"grid_layout_h2_v2_h1_1")
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
        self.label_h2_v2_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_6.setObjectName(u"label_h2_v2_h1_g1_6")
        self.label_h2_v2_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_7.setObjectName(u"label_h2_v2_h1_g1_7")
        self.label_h2_v2_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_8.setObjectName(u"label_h2_v2_h1_g1_8")
        self.label_h2_v2_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

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
        self.label_h2_v2_h1_g1_13.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_14 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_14.setObjectName(u"label_h2_v2_h1_g1_14")
        self.label_h2_v2_h1_g1_14.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_15 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_15.setObjectName(u"label_h2_v2_h1_g1_15")
        self.label_h2_v2_h1_g1_15.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

        self.label_h2_v2_h1_g1_16 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v2_h1_g1_16.setObjectName(u"label_h2_v2_h1_g1_16")
        self.label_h2_v2_h1_g1_16.setText(QCoreApplication.translate("MainWindow", u"10(+10)", None))  # move to re-translate

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
        self.main_horizontal_layout_2.addLayout(self.vertical_layout_h2_3)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1
        self.horizontal_layout_h2_v3_1 = QHBoxLayout()
        self.horizontal_layout_h2_v3_1.setObjectName(u"vertical_layout_h2_v3_1")
        self.horizontal_layout_h2_v3_1.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_h2_3.addLayout(self.horizontal_layout_h2_v3_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1 content
        self.tool_button_h2_v3_h1_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_1.setObjectName(u"tool_button_h2_v3_h1_1")
        self.tool_button_h2_v3_h1_1.setText(QCoreApplication.translate("MainWindow", u"Offensive", None)) # move to re-translate
        self.tool_button_h2_v3_h1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_1.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_1.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_1)

        self.tool_button_h2_v3_h1_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_2.setObjectName(u"tool_button_h2_v3_h1_2")
        self.tool_button_h2_v3_h1_2.setText(QCoreApplication.translate("MainWindow", u"Defensive", None)) # move to re-translate
        self.tool_button_h2_v3_h1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_2.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_2.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_2)

        self.tool_button_h2_v3_h1_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h1_3.setObjectName(u"tool_button_h2_v3_h1_3")
        self.tool_button_h2_v3_h1_3.setText(QCoreApplication.translate("MainWindow", u"Jail", None)) # move to re-translate
        self.tool_button_h2_v3_h1_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h1_3.setIcon(icon_slot_item)
        self.tool_button_h2_v3_h1_3.setIconSize(icon_slot_item_size)
        self.horizontal_layout_h2_v3_1.addWidget(self.tool_button_h2_v3_h1_3)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 1 content - grid layout
        self.grid_layout_h2_v3_h1_1 = QGridLayout()
        self.grid_layout_h2_v3_h1_1.setObjectName(u"grid_layout_h2_v3_h1_1")
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
        self.label_h2_v3_h1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Bleed Jail", None))  # move to re-translate

        self.label_h2_v3_h1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_4.setObjectName(u"label_h2_v3_h1_g1_4")
        self.label_h2_v3_h1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Balance", None))  # move to re-translate

        self.label_h2_v3_h1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_5.setObjectName(u"label_h2_v3_h1_g1_5")
        self.label_h2_v3_h1_g1_5.setFont(font_numbers_bleed)
        self.label_h2_v3_h1_g1_5.setText(QCoreApplication.translate("MainWindow", u"134", None))  # move to re-translate

        self.label_h2_v3_h1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_6.setObjectName(u"label_h2_v3_h1_g1_6")
        self.label_h2_v3_h1_g1_6.setFont(font_numbers_bleed)
        self.label_h2_v3_h1_g1_6.setText(QCoreApplication.translate("MainWindow", u"126", None))  # move to re-translate

        self.label_h2_v3_h1_g1_7 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_7.setObjectName(u"label_h2_v3_h1_g1_7")
        self.label_h2_v3_h1_g1_7.setFont(font_numbers_bleed)
        self.label_h2_v3_h1_g1_7.setText(QCoreApplication.translate("MainWindow", u"101", None))  # move to re-translate

        self.label_h2_v3_h1_g1_8 = QLabel(self.main_vertical_layout_widget)
        self.label_h2_v3_h1_g1_8.setObjectName(u"label_h2_v3_h1_g1_8")
        self.label_h2_v3_h1_g1_8.setFont(font_numbers_bleed)
        self.label_h2_v3_h1_g1_8.setText(QCoreApplication.translate("MainWindow", u"96", None))  # move to re-translate

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
        self.vertical_layout_h2_3.addLayout(self.horizontal_layout_h2_v3_2)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content
        self.tool_button_h2_v3_h2_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h2_v3_h2_1.setObjectName(u"tool_button_h2_v3_h2_1")
        self.tool_button_h2_v3_h2_1.setText(QCoreApplication.translate("MainWindow", u"Blood Code", None)) # move to re-translate
        self.tool_button_h2_v3_h2_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h2_v3_h2_1.setIcon(icon_slot_blood_code)
        self.tool_button_h2_v3_h2_1.setIconSize(icon_slot_blood_code_size)
        self.horizontal_layout_h2_v3_2.addWidget(self.tool_button_h2_v3_h2_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content - vertical layout
        self.vertical_layout_h2_v3_h2_1 = QVBoxLayout()
        self.vertical_layout_h2_v3_h2_1.setObjectName(u"vertical_layout_h2_v3_h2_1")
        self.vertical_layout_h2_v3_h2_1.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_h2_v3_2.addLayout(self.vertical_layout_h2_v3_h2_1)

        # 2nd horizontal layout content - vertical layout 3 content - horizontal layout 2 content - vertical layout content
        self.push_button_h2_v3_h2_v1_1 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_1.setObjectName(u"push_button_h2_v3_h2_v1_1")
        self.push_button_h2_v3_h2_v1_1.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_1.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_1.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_1)

        self.push_button_h2_v3_h2_v1_2 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_2.setObjectName(u"push_button_h2_v3_h2_v1_2")
        self.push_button_h2_v3_h2_v1_2.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_2.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_2.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_2)

        self.push_button_h2_v3_h2_v1_3 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_3.setObjectName(u"push_button_h2_v3_h2_v1_3")
        self.push_button_h2_v3_h2_v1_3.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_3.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_3.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_3)

        self.push_button_h2_v3_h2_v1_4 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_4.setObjectName(u"push_button_h2_v3_h2_v1_4")
        self.push_button_h2_v3_h2_v1_4.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_4.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_4.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_4)

        self.push_button_h2_v3_h2_v1_5 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_5.setObjectName(u"push_button_h2_v3_h2_v1_5")
        self.push_button_h2_v3_h2_v1_5.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_5.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_5.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_5)

        self.push_button_h2_v3_h2_v1_6 = QPushButton(self.main_vertical_layout_widget)
        self.push_button_h2_v3_h2_v1_6.setObjectName(u"push_button_h2_v3_h2_v1_6")
        self.push_button_h2_v3_h2_v1_6.setText(QCoreApplication.translate("MainWindow", u"Willpower Booster - Overload", None)) # move to re-translate
        self.push_button_h2_v3_h2_v1_6.setIcon(icon_slot_item)
        self.push_button_h2_v3_h2_v1_6.setIconSize(icon_slot_forma_size)
        self.vertical_layout_h2_v3_h2_1.addWidget(self.push_button_h2_v3_h2_v1_6)

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
        self.tool_button_h3_g1_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_1.setObjectName(u"tool_button_h3_g1_1")
        self.tool_button_h3_g1_1.setText(QCoreApplication.translate("MainWindow", u"Dodge Effectiveness", None)) # move to re-translate
        self.tool_button_h3_g1_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_h3_g1_1.setIcon(icon_text_arrow)

        self.tool_button_h3_g1_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_2.setObjectName(u"tool_button_h3_g1_2")
        self.tool_button_h3_g1_2.setText(QCoreApplication.translate("MainWindow", u"Quick", None)) # move to re-translate
        self.tool_button_h3_g1_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_button_h3_g1_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_3.setObjectName(u"tool_button_h3_g1_3")
        self.tool_button_h3_g1_3.setText(QCoreApplication.translate("MainWindow", u"Defensive Formae", None)) # move to re-translate
        self.tool_button_h3_g1_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_h3_g1_3.setIcon(icon_text_arrow)

        self.tool_button_h3_g1_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h3_g1_4.setObjectName(u"tool_button_h3_g1_4")
        self.tool_button_h3_g1_4.setFont(font_defensive_formae)
        self.tool_button_h3_g1_4.setText(QCoreApplication.translate("MainWindow", u"30", None)) # move to re-translate
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

        # worse than setAlignment
        # self.vertical_spacer_h3_v1_1 = QSpacerItem(20, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.vertical_layout_h3_1.addItem(self.vertical_spacer_h3_v1_1)

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
        self.tool_button_h3_v1_g1_1 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_1.setObjectName(u"tool_button_h3_v1_g1_1")
        self.tool_button_h3_v1_g1_1.setText(QCoreApplication.translate("MainWindow", u"Strength", None)) # move to re-translate
        self.tool_button_h3_v1_g1_1.setIcon(icon_attribute_strength)
        self.tool_button_h3_v1_g1_1.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_2 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_2.setObjectName(u"tool_button_h3_v1_g1_2")
        self.tool_button_h3_v1_g1_2.setText(QCoreApplication.translate("MainWindow", u"Dexterity", None)) # move to re-translate
        self.tool_button_h3_v1_g1_2.setIcon(icon_attribute_dexterity)
        self.tool_button_h3_v1_g1_2.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_3 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_3.setObjectName(u"tool_button_h3_v1_g1_3")
        self.tool_button_h3_v1_g1_3.setText(QCoreApplication.translate("MainWindow", u"Mind", None)) # move to re-translate
        self.tool_button_h3_v1_g1_3.setIcon(icon_attribute_mind)
        self.tool_button_h3_v1_g1_3.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_4 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_4.setObjectName(u"tool_button_h3_v1_g1_4")
        self.tool_button_h3_v1_g1_4.setText(QCoreApplication.translate("MainWindow", u"Willpower", None)) # move to re-translate
        self.tool_button_h3_v1_g1_4.setIcon(icon_attribute_willpower)
        self.tool_button_h3_v1_g1_4.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_5 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_5.setObjectName(u"tool_button_h3_v1_g1_5")
        self.tool_button_h3_v1_g1_5.setText(QCoreApplication.translate("MainWindow", u"Vitality", None)) # move to re-translate
        self.tool_button_h3_v1_g1_5.setIcon(icon_attribute_vitality)
        self.tool_button_h3_v1_g1_5.setIconSize(icon_attribute_size)

        self.tool_button_h3_v1_g1_6 = QPushButton(self.main_vertical_layout_widget)
        self.tool_button_h3_v1_g1_6.setObjectName(u"tool_button_h3_v1_g1_6")
        self.tool_button_h3_v1_g1_6.setText(QCoreApplication.translate("MainWindow", u"Fortitude", None)) # move to re-translate
        self.tool_button_h3_v1_g1_6.setIcon(icon_attribute_fortitude)
        self.tool_button_h3_v1_g1_6.setIconSize(icon_attribute_size)

        self.label_h3_v1_g1_1 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_1.setObjectName(u"label_h3_v1_g1_1")
        self.label_h3_v1_g1_1.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_1.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_2 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_2.setObjectName(u"label_h3_v1_g1_2")
        self.label_h3_v1_g1_2.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_2.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_3 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_3.setObjectName(u"label_h3_v1_g1_3")
        self.label_h3_v1_g1_3.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_3.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_4 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_4.setObjectName(u"label_h3_v1_g1_4")
        self.label_h3_v1_g1_4.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_4.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_5 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_5.setObjectName(u"label_h3_v1_g1_5")
        self.label_h3_v1_g1_5.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_5.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_h3_v1_g1_6 = QLabel(self.main_vertical_layout_widget)
        self.label_h3_v1_g1_6.setObjectName(u"label_h3_v1_g1_6")
        self.label_h3_v1_g1_6.setFont(font_numbers_attribute)
        self.label_h3_v1_g1_6.setText(QCoreApplication.translate("MainWindow", u"12", None))  # move to re-translate
        self.label_h3_v1_g1_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_1 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_1.setObjectName(u"progress_bar_h3_v1_g1_1")
        self.progress_bar_h3_v1_g1_1.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_1.setFormat("%v")
        self.progress_bar_h3_v1_g1_1.setValue(24)
        self.progress_bar_h3_v1_g1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_2 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_2.setObjectName(u"progress_bar_h3_v1_g1_2")
        self.progress_bar_h3_v1_g1_2.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_2.setFormat("%v")
        self.progress_bar_h3_v1_g1_2.setValue(24)
        self.progress_bar_h3_v1_g1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_3 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_3.setObjectName(u"progress_bar_h3_v1_g1_3")
        self.progress_bar_h3_v1_g1_3.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_3.setFormat("%v")
        self.progress_bar_h3_v1_g1_3.setValue(24)
        self.progress_bar_h3_v1_g1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_4 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_4.setObjectName(u"progress_bar_h3_v1_g1_4")
        self.progress_bar_h3_v1_g1_4.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_4.setFormat("%v")
        self.progress_bar_h3_v1_g1_4.setValue(24)
        self.progress_bar_h3_v1_g1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_5 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_5.setObjectName(u"progress_bar_h3_v1_g1_5")
        self.progress_bar_h3_v1_g1_5.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_5.setFormat("%v")
        self.progress_bar_h3_v1_g1_5.setValue(24)
        self.progress_bar_h3_v1_g1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar_h3_v1_g1_6 = QProgressBar(self.main_vertical_layout_widget)
        self.progress_bar_h3_v1_g1_6.setObjectName(u"progress_bar_h3_v1_g1_6")
        self.progress_bar_h3_v1_g1_6.setFont(font_numbers_progress_bar)
        self.progress_bar_h3_v1_g1_6.setFormat("%v")
        self.progress_bar_h3_v1_g1_6.setValue(24)
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

        # 3rd horizontal layout content - vertical layout 1 content - spacer at the bottom
        # worse than setAlignment
        # self.vertical_spacer_h3_v1_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.vertical_layout_h3_1.addItem(self.vertical_spacer_h3_v1_2)

        # 4th horizontal layout
        self.tool_button_pre_h4 = QToolButton(self.main_vertical_layout_widget)
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
        self.tool_button_h4_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_1.setObjectName(u"tool_button_h4_1")
        self.tool_button_h4_1.setFont(font_numbers_defense)
        self.tool_button_h4_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_1.setIcon(icon_defense_slash)
        self.tool_button_h4_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_1)

        self.tool_button_h4_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_2.setObjectName(u"tool_button_h4_2")
        self.tool_button_h4_2.setFont(font_numbers_defense)
        self.tool_button_h4_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_2.setIcon(icon_defense_crush)
        self.tool_button_h4_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_2)

        self.tool_button_h4_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_3.setObjectName(u"tool_button_h4_3")
        self.tool_button_h4_3.setFont(font_numbers_defense)
        self.tool_button_h4_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_3.setIcon(icon_defense_pierce)
        self.tool_button_h4_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_3)

        self.tool_button_h4_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_4.setObjectName(u"tool_button_h4_4")
        self.tool_button_h4_4.setFont(font_numbers_defense)
        self.tool_button_h4_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_4.setIcon(icon_defense_blood)
        self.tool_button_h4_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_4)

        self.tool_button_h4_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_5.setObjectName(u"tool_button_h4_5")
        self.tool_button_h4_5.setFont(font_numbers_defense)
        self.tool_button_h4_5.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_5.setIcon(icon_defense_fire)
        self.tool_button_h4_5.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_5)

        self.tool_button_h4_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_6.setObjectName(u"tool_button_h4_6")
        self.tool_button_h4_6.setFont(font_numbers_defense)
        self.tool_button_h4_6.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_6.setIcon(icon_defense_ice)
        self.tool_button_h4_6.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_6)

        self.tool_button_h4_7 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h4_7.setObjectName(u"tool_button_h4_7")
        self.tool_button_h4_7.setFont(font_numbers_defense)
        self.tool_button_h4_7.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h4_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h4_7.setIcon(icon_defense_thunder)
        self.tool_button_h4_7.setIconSize(icon_defense_size)
        self.main_horizontal_layout_4.addWidget(self.tool_button_h4_7)

        # 5th horizontal layout
        self.tool_button_pre_h5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_pre_h5.setObjectName(u"tool_button_pre_h5")
        self.tool_button_pre_h5.setText(QCoreApplication.translate("MainWindow", u"Guardian Defense", None)) # move to re-translate
        self.tool_button_pre_h5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_button_pre_h5.setIcon(icon_text_arrow)
        self.main_vertical_layout.addWidget(self.tool_button_pre_h5)

        self.main_horizontal_layout_5 = QHBoxLayout()
        self.main_horizontal_layout_5.setObjectName(u"main_horizontal_layout_5")
        self.main_horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        self.main_vertical_layout.addLayout(self.main_horizontal_layout_5)

        # 5th horizontal layout content
        self.tool_button_h5_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_1.setObjectName(u"tool_button_h5_1")
        self.tool_button_h5_1.setFont(font_numbers_defense)
        self.tool_button_h5_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_1.setIcon(icon_defense_slash)
        self.tool_button_h5_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_1)

        self.tool_button_h5_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_2.setObjectName(u"tool_button_h5_2")
        self.tool_button_h5_2.setFont(font_numbers_defense)
        self.tool_button_h5_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_2.setIcon(icon_defense_crush)
        self.tool_button_h5_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_2)

        self.tool_button_h5_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_3.setObjectName(u"tool_button_h5_3")
        self.tool_button_h5_3.setFont(font_numbers_defense)
        self.tool_button_h5_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_3.setIcon(icon_defense_pierce)
        self.tool_button_h5_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_3)

        self.tool_button_h5_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_4.setObjectName(u"tool_button_h5_4")
        self.tool_button_h5_4.setFont(font_numbers_defense)
        self.tool_button_h5_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_4.setIcon(icon_defense_blood)
        self.tool_button_h5_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_4)

        self.tool_button_h5_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_5.setObjectName(u"tool_button_h5_5")
        self.tool_button_h5_5.setFont(font_numbers_defense)
        self.tool_button_h5_5.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_5.setIcon(icon_defense_fire)
        self.tool_button_h5_5.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_5)

        self.tool_button_h5_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_6.setObjectName(u"tool_button_h5_6")
        self.tool_button_h5_6.setFont(font_numbers_defense)
        self.tool_button_h5_6.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_6.setIcon(icon_defense_ice)
        self.tool_button_h5_6.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_6)

        self.tool_button_h5_7 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h5_7.setObjectName(u"tool_button_h5_7")
        self.tool_button_h5_7.setFont(font_numbers_defense)
        self.tool_button_h5_7.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h5_7.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h5_7.setIcon(icon_defense_thunder)
        self.tool_button_h5_7.setIconSize(icon_defense_size)
        self.main_horizontal_layout_5.addWidget(self.tool_button_h5_7)

        # 6th horizontal layout
        self.tool_button_pre_h6 = QToolButton(self.main_vertical_layout_widget)
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
        self.tool_button_h6_1 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_1.setObjectName(u"tool_button_h6_1")
        self.tool_button_h6_1.setFont(font_numbers_defense)
        self.tool_button_h6_1.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_1.setIcon(icon_resistance_disease)
        self.tool_button_h6_1.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_1)

        self.tool_button_h6_2 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_2.setObjectName(u"tool_button_h6_2")
        self.tool_button_h6_2.setFont(font_numbers_defense)
        self.tool_button_h6_2.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_2.setIcon(icon_resistance_wound)
        self.tool_button_h6_2.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_2)

        self.tool_button_h6_3 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_3.setObjectName(u"tool_button_h6_3")
        self.tool_button_h6_3.setFont(font_numbers_defense)
        self.tool_button_h6_3.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_3.setIcon(icon_resistance_bleed)
        self.tool_button_h6_3.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_3)

        self.tool_button_h6_4 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_4.setObjectName(u"tool_button_h6_4")
        self.tool_button_h6_4.setFont(font_numbers_defense)
        self.tool_button_h6_4.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_4.setIcon(icon_resistance_curse)
        self.tool_button_h6_4.setIconSize(icon_defense_size)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_4)

        # dummy button
        self.tool_button_h6_5 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_5.setObjectName(u"tool_button_h6_5")
        self.tool_button_h6_5.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_5.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_5.setVisible(False)
        sp = self.tool_button_h6_5.sizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self.tool_button_h6_5.setSizePolicy(sp)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_5)

        # dummy button
        self.tool_button_h6_6 = QToolButton(self.main_vertical_layout_widget)
        self.tool_button_h6_6.setObjectName(u"tool_button_h6_6")
        self.tool_button_h6_6.setText(QCoreApplication.translate("MainWindow", u"123", None)) # move to re-translate
        self.tool_button_h6_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tool_button_h6_6.setVisible(False)
        sp = self.tool_button_h6_6.sizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self.tool_button_h6_6.setSizePolicy(sp)
        self.main_horizontal_layout_6.addWidget(self.tool_button_h6_6)

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
