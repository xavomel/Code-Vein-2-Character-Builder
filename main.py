from PySide6.QtWidgets import QApplication, QMainWindow
import builder_ui
from game_data_classes import *


class Character:
    name = ""
    bloodline = ""
    blood_code = BloodCode()
    weapon_1 = Weapon(1)
    weapon_2 = Weapon(2)
    offensive_forma = OffensiveForma()
    defensive_forma = DefensiveForma()
    jail = Jail()

    formae_1 = [Forma(x) for x in range(4)]
    formae_2 = [Forma(x) for x in range(4)]
    boosters = [Booster(x) for x in range(6)]

    traits = []

    overburden = False
    balance = 0
    guard = 0
    ichor = 0

    attributes = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    burden = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    margin = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    defense = {
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Fire": 		0,
        "Ice":			0,
        "Lightning":	0,
        "Blood":	 	0,
    }

    guarding_defense = {
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Fire": 		0,
        "Ice":			0,
        "Lightning":	0,
        "Blood":	 	0,
    }

    resistances = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }

    def __init__(self):
        pass

    def add_burden(self, d):
        for attribute, value in d:
            burden[attribute] += value
            margin[attribute] -= value  # can be negative

    def remove_burden(self, d):
        for attribute, value in d:
            burden[attribute] -= value
            margin[attribute] += value  # can be negative

    # def update_weapon(self, Weapon, slot):
    #     if slot == 1:
    #         weapon_prev = self.weapon_1
    #     else:
    #         weapon_prev = self.weapon_2


class MainWindow(QMainWindow, builder_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.character = Character()


def main():
    app = QApplication([])
    form = MainWindow()
    form.show()
    form.placeDynamicUIElements()

    app.exec()
    

main()
