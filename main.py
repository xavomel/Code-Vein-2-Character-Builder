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

        attributes = dict()

        for type, var, key, value, old_value, widget in transaction:
            if not widget:
                continue

            if widget.__class__.__name__ == "AttributeProgressBar":
                # test
                value = 10

                # fetch maximum from attributes in same transaction
                maximum = attributes[key]
                if value > maximum:
                    maximum = value
                widget.setValue(value)
                widget.setMaximum(maximum)
            else:
                # need to process attributes first, to later re-use them
                # but we need to process attributes first anyway for booster / trait condition
                if var == "Attributes":
                    attributes[key] = value

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

        for type, var, key, value, old_value, widget in self.last_transaction:
            if not widget:
                continue

            if widget.__class__.__name__ == "AttributeProgressBar":
                maximum = self.character.attributes[key]
                if old_value > maximum:
                    maximum = old_value
                widget.setValue(old_value)
                widget.setMaximum(maximum)
            else:
                widget.setText(str(old_value))

        self.last_transaction = []

    def commit_transaction(self, data):
        """
        Replaces Character values with transaction values
        :return:
        """
        if not self.last_transaction:
            return

        # overwrite old blood code with new
        self.character.blood_code = data

        # then handle consequences of changing blood code
        for type, var, key, value, old_value, widget in self.last_transaction:
            if var == "Bloodline":
                self.character.bloodline = value
            elif var == "Attributes":
                self.character.attributes[key] += value - old_value
            elif var == "Burden":
                # test
                value = 10

                self.character.burden[key] += value - old_value
                self.character.margin[key] -= value - old_value
            elif var == "Defense":
                self.character.defense[key] += value - old_value
            elif var == "Resistance":
                self.character.resistance[key] += value - old_value

        self.last_transaction = []

    def build_transaction(self, data):
        """
        :return:
        """
        transaction_handler = self.class_to_handler[type(data).__name__]
        transaction = transaction_handler(data)

        for x in transaction:
            print(x)

        return transaction

    def build_blood_code_transaction(self, data):
        print("blood_code")

        transaction = []

        # first handle the base blood code
        _type = type(data).__name__

        # class - IS IT NECESSARY?
        # class variable - to set on
        # key - to set on (can be None)
        # value - to set
        # old value - to restore on rollback
        # widget - to set on (can be None)

        # bloodline
        transaction.append([_type, "Bloodline", None, data.bloodline, self.character.bloodline, None])

        # attributes
        for attr, val in data.attributes.items():
            widget = self.char_to_widget_mapping["Attribute_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from boosters, partner, food
            old_value = self.character.attributes[attr]
            transaction.append([_type, "Attributes", attr, val, old_value, widget])

        # burden
        for attr, val in data.burden.items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            transaction.append([_type, "Burden", attr, val, old_value, widget])

        # defense
        for attr, val in data.defense.items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            # todo comment
            old_value = self.character.defense[attr]
            transaction.append([_type, "Defense", attr, val, old_value, widget])

        # resistance
        for attr, val in data.resistance.items():
            widget = self.char_to_widget_mapping["Resistance_" + attr]
            # todo comment
            old_value = self.character.resistance[attr]
            transaction.append([_type, "Resistance", attr, val, old_value, widget])

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
