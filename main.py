from PySide6.QtWidgets import QApplication, QMainWindow
import builder_ui
from game_data_classes import *
from utility import open_json


class Character:
    def __init__(self):
        self.name = ""
        self.bloodline = ""
        self.blood_code = BloodCode()
        # need a separate variable for capacity weapon 1 and 2 ?
        # so that we can have max capacity 0 even without weapon
        # unless we use Weapon with default values for that
        self.weapon_1 = Weapon(dummy_number=1)
        self.weapon_2 = Weapon(dummy_number=2)
        self.offensive_forma = OffensiveForma()
        self.defensive_forma = DefensiveForma()
        self.jail = Jail()

        self.formae_1 = [Forma(dummy_number=x + 1) for x in range(4)]
        self.formae_2 = [Forma(dummy_number=x + 1) for x in range(4)]
        self.boosters = [Booster(dummy_number=x + 1) for x in range(6)]

        self.traits = []

        self.overburden = False
        self.balance = 0
        self.ichor = 0
        self.stamina_guard_cost = 0
        self.bleed = 0

        self.attributes = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        self.burden = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        self.margin = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        self.defense = {
            "Slash": 0.0,
            "Crush": 0.0,
            "Pierce": 0.0,
            "Blood": 0.0,
            "Fire": 0.0,
            "Ice": 0.0,
            "Lightning": 0.0,
        }

        self.guarding_defense = {
            "Slash": 0,
            "Crush": 0,
            "Pierce": 0,
            "Blood": 0,
            "Fire": 0,
            "Ice": 0,
            "Lightning": 0,
        }

        self.resistance = {
            "Disease": 0,
            "Wound": 0,
            "Bleed": 0,
            "Curse": 0,
        }

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


class Builder:
    def __init__(self):
        self.character = Character()
        self.blood_codes = dict()
        self.weapons = dict()
        self.boosters = dict()
        self.formae = dict()
        self.offensive_formae = dict()
        self.defensive_formae = dict()
        self.jails = dict()
        self.translation = dict()
        self.char_to_widget_mapping = dict()
        self.widget_to_char_mapping = dict()
        self.last_transaction = []
        self.class_to_handler = {
            "Weapon": self.build_weapon_transaction,
            "Forma": self.build_forma_transaction,
            "Booster": self.build_booster_transaction,
            "BloodCode": self.build_blood_code_transaction,
            "Jail": self.build_jail_transaction,
            "DefensiveForma": self.build_defensive_transaction,
            "OffensiveForma": self.build_offensive_transaction,
        }

        blood_codes = open_json(u"GameData/BloodCode.json")
        weapons = open_json(u"GameData/Weapon.json")
        boosters = open_json(u"GameData/Booster.json")
        formae = open_json(u"GameData/Forma.json")
        offensive_formae = open_json(u"GameData/Offensive.json")
        defensive_formae = open_json(u"GameData/Defensive.json")
        jails = open_json(u"GameData/Jail.json")
        self.translation = open_json("GameData/Translation/en.json")

        for doc in blood_codes:
            name = doc["Name"]
            self.blood_codes[name] = BloodCode(doc)
            # print(vars(self.blood_codes[name]))
        self.blood_codes["Empty"] = BloodCode()

        for doc in weapons:
            name = doc["Name"]
            self.weapons[name] = Weapon(doc)
        self.weapons["Empty"] = Weapon()

        for doc in boosters:
            name = doc["Name"]
            self.boosters[name] = Booster(doc)
        self.boosters["Empty"] = Booster()

        for doc in formae:
            name = doc["Name"]
            self.formae[name] = Forma(doc)
        self.formae["Empty"] = Forma()

        for doc in offensive_formae:
            name = doc["Name"]
            self.offensive_formae[name] = OffensiveForma(doc)
        self.offensive_formae["Empty"] = OffensiveForma()

        for doc in defensive_formae:
            name = doc["Name"]
            self.defensive_formae[name] = DefensiveForma(doc)
        self.defensive_formae["Empty"] = DefensiveForma()

        for doc in jails:
            name = doc["Name"]
            self.jails[name] = Jail(doc)
        self.jails["Empty"] = Jail()

    def is_transaction_ongoing(self):
        return True if self.last_transaction else False

    def start_transaction(self, data):
        """
        Replaces UI values with transaction values (does NOT change anything in Character)
        :return:
        """
        transaction = self.build_transaction(data)
        for type, widget, name, value in transaction:
            widget.setText(str(value))

        self.last_transaction = transaction

    def rollback_transaction(self):
        """
        Replaces UI values with Character values

        Need to do this if there is not-committed transaction
        because e.g a previous booster may affect more things than new booster
        so just overwriting with new values is not enough
        :return:
        """
        if not self.last_transaction:
            return

        for type, widget, name, value in self.last_transaction:
            # TODO
            # if type == "Bleed":
            #     widget.setText(str(self.character.bleed))
            if type == "Balance":
                widget.setText(str(self.character.balance))
            elif type == "Ichor":
                widget.setText(str(self.character.ichor))
            elif type == "Attributes":
                widget.setText(str(self.character.attributes[name]))
            elif type == "Defense":
                widget.setText(str(self.character.defense[name]))
            elif type == "Resistance":
                widget.setText(str(self.character.resistance[name]))

        self.last_transaction = []

    def commit_transaction(self):
        """
        Replaces Character values with transaction values
        :return:
        """
        if not self.last_transaction:
            return

        # TODO shouldn't we just overwrite self.character.blood_code
        # and then recalculate values for whole character?
        for type, widget, name, value in self.last_transaction:
            # TODO
            # if type == "Bleed":
            #     widget.setText(str(self.character.bleed))
            if type == "Balance":
                self.character.balance = value
            elif type == "Ichor":
                self.character.ichor = value
            elif type == "Attributes":
                self.character.attributes[name] = value
            elif type == "Defense":
                self.character.defense[name] = value
            elif type == "Resistance":
                self.character.resistance[name] = value

        print(self.character.balance)
        print(self.character.ichor)

        self.last_transaction = []

    def build_transaction(self, data):
        """
        :return:
        """
        transaction_handler = self.class_to_handler[type(data).__name__]
        transaction = transaction_handler(data)

        # if "Attributes" in data:
        #     for attr, val in data["Attributes"].items():
        #         widget = self.char_to_widget_mapping["Attribute_" + attr]
        #         transaction.append(["Attributes", widget, attr, val])
        # if "Attribute" in data:
        #     for attr, val in data["Attribute"].items():
        #         widget = self.char_to_widget_mapping["Attribute_" + attr]
        #         transaction.append(["Attribute", widget, attr, val])
        # if "Burden" in data:
        #     for attr, val in data["Burden"].items():
        #         widget = self.char_to_widget_mapping["Burden_" + attr]
        #         transaction.append(["Burden", widget, attr, val])

        for x in transaction:
            print(x)

        return transaction

    def build_weapon_transaction(self, data):
        print("weapon")

        transaction = []

        return transaction

    def build_forma_transaction(self, data):
        print("forma")

        transaction = []

        return transaction

    def build_booster_transaction(self, data):
        print("booster")

        transaction = []

        return transaction

    def build_blood_code_transaction(self, data):
        print("blood_code")

        transaction = []

        # first handle the base blood code
        # then handle the cascading consequences

        transaction.append(["Bleed", self.char_to_widget_mapping["Weapon_1_Bleed"], "Weapon_1", data.bleed])
        transaction.append(["Bleed", self.char_to_widget_mapping["Weapon_2_Bleed"], "Weapon_2", data.bleed])
        transaction.append(["Bleed", self.char_to_widget_mapping["Jail_Bleed"], "Jail", data.bleed])
        transaction.append(["Balance", self.char_to_widget_mapping["Balance"], "Balance", data.balance])
        transaction.append(["Ichor", self.char_to_widget_mapping["Ichor"], "Ichor", data.ichor])

        for attr, val in data.attributes.items():
            widget = self.char_to_widget_mapping["Attribute_" + attr]
            transaction.append(["Attributes", widget, attr, val])
        # for attr, val in data.burden.items():
        #     widget = self.char_to_widget_mapping["Burden_" + attr]
        #     transaction.append(["Defense", widget, attr, val])
        for attr, val in data.defense.items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            transaction.append(["Defense", widget, attr, val])
        for attr, val in data.resistance.items():
            widget = self.char_to_widget_mapping["Resistance_" + attr]
            transaction.append(["Resistance", widget, attr, val])

        return transaction

    def build_jail_transaction(self, data):
        print("jail")

        transaction = []

        return transaction

    def build_defensive_transaction(self, data):
        print("defensive")

        transaction = []

        return transaction

    def build_offensive_transaction(self, data):
        print("offensive")

        transaction = []

        return transaction


class MainWindow(QMainWindow, builder_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.builder = Builder()
        self.setupUi(self)


def main():
    app = QApplication([])
    form = MainWindow()
    form.show()
    form.placeDynamicUIElements()

    # sorting order (e.g. weapons order) is dependent on .json
    # json [] guarantees order is preserved, make sure to add to dict in order

    # build save / load will require a mapping table
    # since there is no short unique identifier for items (e.g. weapons)

    # sorting order cannot be an unique identifier, because order may change in DLC
    app.exec()
    

main()
