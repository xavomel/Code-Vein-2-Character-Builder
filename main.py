from PySide6.QtWidgets import QApplication, QMainWindow
import builder_ui
from math import floor
from game_data_classes import *
from utility import open_json


class Character:
    def __init__(self):
        self.name = ""
        self.bloodline = ""
        self.blood_code = BloodCode()
        # TODO add weapons dict in character to hold weapons?
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
        self.transform = {
            "Weapon_1": "Weapon_Off",
            "Weapon_2": "Weapon_Off",
            "Defensive": "Defensive_Off",
        }
        self.bleed = {
            "Weapon_1": 0,
            "Weapon_2": 0,
            "Jail": 0,
        }
        self.capacity = {
            "Weapon_1_Reliability": 0,
            "Weapon_1_Handling": 0,
            "Weapon_1_Conversion": 0,
            "Weapon_1_Conductivity": 0,
            "Weapon_1_Reliability_Max": 0,
            "Weapon_1_Handling_Max": 0,
            "Weapon_1_Conversion_Max": 0,
            "Weapon_1_Conductivity_Max": 0,
            "Weapon_2_Reliability": 0,
            "Weapon_2_Handling": 0,
            "Weapon_2_Conversion": 0,
            "Weapon_2_Conductivity": 0,
            "Weapon_2_Reliability_Max": 0,
            "Weapon_2_Handling_Max": 0,
            "Weapon_2_Conversion_Max": 0,
            "Weapon_2_Conductivity_Max": 0,
        }

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
            "Slash": Fraction(0, 10),
            "Crush": Fraction(0, 10),
            "Pierce": Fraction(0, 10),
            "Blood": Fraction(0, 10),
            "Fire": Fraction(0, 10),
            "Ice": Fraction(0, 10),
            "Lightning": Fraction(0, 10),
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

    def start_transaction(self, data, slot="", transform=""):
        """
        Replaces UI values with transaction values (does NOT change anything in Character)
        :return:
        """
        transaction = self.build_transaction(data, slot, transform)

        attributes = dict()

        for type, var, key, value, old_value, widget in transaction:
            if not widget:
                continue

            if widget.__class__.__name__ == "AttributeProgressBar":
                # fetch maximum from attributes in same transaction
                # or from character if attributes are not in transaction (ok to fetch since they won't be changed)
                maximum = attributes.get(key)
                # check for None as maximum = 0 is a valid value
                if maximum is None:
                    maximum = self.character.attributes[key]
                new_value = value + old_value
                if new_value > maximum:
                    maximum = new_value
                widget.setMaximum(maximum)
                widget.setValue(new_value)
            else:
                # need to process attributes first, to later re-use them
                # but we need to process attributes first anyway for booster / trait condition
                if var == "Attributes":
                    attributes[key] = value + old_value

                if var == "Defense":
                    new_value = value + old_value
                    # general format for floating point (Fraction in this case)
                    # Fractions are used because adding and subtracting Floats many times could introduce errors
                    widget.setText(str(format(new_value, "g")))
                else:
                    widget.setText(str(value + old_value))

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
                widget.setMaximum(maximum)
                widget.setValue(old_value)
            else:
                if var == "Defense":
                    # general format for floating point (Fraction in this case)
                    # Fractions are used because adding and subtracting Floats many times could introduce errors
                    widget.setText(str(format(old_value, "g")))
                else:
                    widget.setText(str(old_value))

        self.last_transaction = []

    def commit_transaction(self, data, slot="", transform=""):
        """
        Replaces Character values with transaction values
        :return:
        """
        if not self.last_transaction:
            return

        # overwrite old item with new
        _type = type(data).__name__  # could use this instead self.last_transaction[0][0]
        if _type == "Weapon":
            if slot == "Weapon_1":
                self.character.weapon_1 = data
                self.character.transform[slot] = transform
            else:
                self.character.weapon_2 = data
                self.character.transform[slot] = transform
        elif _type == "BloodCode":
            self.character.blood_code = data
        elif _type == "Jail":
            self.character.jail = data
        elif _type == "DefensiveForma":
            self.character.defensive_forma = data
            self.character.transform["Defensive"] = transform

        # then handle consequences of changing blood code
        for _type, var, key, value, old_value, widget in self.last_transaction:
            if var == "Bloodline":
                self.character.bloodline = value
            elif var == "Attributes":
                self.character.attributes[key] += value
            elif var == "Burden":
                self.character.burden[key] += value
                self.character.margin[key] -= value
            elif var == "Defense":
                self.character.defense[key] += value
            elif var == "GuardingDefense":
                self.character.guarding_defense[key] += value
            elif var == "Resistance":
                self.character.resistance[key] += value
            elif var == "Ichor":
                self.character.ichor += value
            elif var == "Bleed":
                self.character.bleed[key] += value
            elif var == "Balance":
                self.character.balance += value
            elif var == "Capacity":
                self.character.capacity[key] += value
            elif var == "StaminaGuardCost":
                self.character.stamina_guard_cost += value

        self.last_transaction = []

    def build_transaction(self, data, slot="", transform=""):
        """
        :return:
        """
        transaction_handler = self.class_to_handler[type(data).__name__]
        transaction = transaction_handler(data, slot, transform)

        for x in transaction:
            print(x)

        return transaction

    def build_blood_code_transaction(self, data, slot="", transform=""):
        print("blood_code")

        transaction = []

        _type = type(data).__name__
        equipped = self.character.blood_code
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
            val = val - equipped.attributes[attr]
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
            val = val - equipped.burden[attr]
            transaction.append([_type, "Burden", attr, val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # defense
        for attr, val in data.defense.items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            # todo comment
            old_value = self.character.defense[attr]
            val = val - equipped.defense[attr]
            transaction.append([_type, "Defense", attr, val, old_value, widget])

        # resistance
        #
        # seems attributes also affect resistance, but for now let's ignore it
        for attr, val in data.resistance.items():
            widget = self.char_to_widget_mapping["Resistance_" + attr]
            # todo comment
            old_value = self.character.resistance[attr]
            val = val - equipped.resistance[attr]
            transaction.append([_type, "Resistance", attr, val, old_value, widget])

        # ichor
        widget = self.char_to_widget_mapping["Ichor"]
        # todo comment
        old_value = self.character.ichor
        val = data.ichor - equipped.ichor
        transaction.append([_type, "Ichor", None, val, old_value, widget])

        # bleed
        # todo comment
        val = data.bleed - equipped.bleed
        transaction.append([_type, "Bleed", "Weapon_1", val, self.character.bleed["Weapon_1"], self.char_to_widget_mapping["Weapon_1_Bleed"]])
        transaction.append([_type, "Bleed", "Weapon_2", val, self.character.bleed["Weapon_2"], self.char_to_widget_mapping["Weapon_2_Bleed"]])
        transaction.append([_type, "Bleed", "Jail", val, self.character.bleed["Jail"], self.char_to_widget_mapping["Jail_Bleed"]])

        # balance
        widget = self.char_to_widget_mapping["Balance"]
        # todo comment
        old_value = self.character.balance
        val = data.balance - equipped.balance
        transaction.append([_type, "Balance", None, val, old_value, widget])

        return transaction

    def build_weapon_transaction(self, data, slot="", transform=""):
        print("weapon")

        transaction = []

        _type = type(data).__name__
        transformed = data.transforms[transform]
        equipped_transform = self.character.transform[slot]
        if slot == "Weapon_1":
            equipped = self.character.weapon_1.transforms[equipped_transform]
            other_equipped = self.character.weapon_2.transforms[equipped_transform]
        else:
            equipped = self.character.weapon_2.transforms[equipped_transform]
            other_equipped = self.character.weapon_1.transforms[equipped_transform]

        # burden
        for attr, val in transformed["Burden"].items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact

            # Dual Wielding burden
            val_other = other_equipped["Burden"][attr]
            val_equipped = equipped["Burden"][attr]
            val_equipped_other = other_equipped["Burden"][attr]

            # TODO add handling for Weapon Rack
            # if dual wielding calc needed (weapons in this slot and other slot both have non-zero burden for same attr)
            if val_other != 0:
                # if equipped weapon has HIGHER burden (is not halved)
                # take HALF of other weapon burden as equip load
                # or NO value if Weapon Rack is active
                if equipped["Burden"][attr] > other_equipped["Burden"][attr]:
                    val_equipped_other = floor(val_equipped_other / 2)

                    # - pick the WHOLE value from weapon with HIGHER burden
                    # - and add HALF value (rounded down) from weapon with LOWER burden
                    # - or add NO value from weapon with LOWER burden if Weapon Rack is active
                    if val_other > val:
                        val = floor(val / 2)
                    else:
                        val_other = floor(val_other / 2)
                # if equipped weapon has LOWER burden (is halved)
                # take HALF of equipped weapon burden as equip load
                # or NO value if Weapon Rack is active
                else:
                    val_equipped = floor(val_equipped / 2)

                    # same as above
                    if val_other > val:
                        val = floor(val / 2)
                    else:
                        val_other = floor(val_other / 2)

            new_val = val + val_other - val_equipped - val_equipped_other
            # if attr == "Willpower":
            #     print("final", new_val, "current", val, "other", val_other, "equipped", val_equipped, "val_equipped_other", val_equipped_other)
            transaction.append([_type, "Burden", attr, new_val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # Bleed
        # todo comment
        key = slot
        val = transformed["Bleed"] - equipped["Bleed"]
        transaction.append([_type, "Bleed", key, val, self.character.bleed[key], self.char_to_widget_mapping[key + "_Bleed"]])

        # capacity
        for attr, val in transformed["Capacity"].items():
            key = slot + "_" + attr + "_Max"
            widget = self.char_to_widget_mapping[key]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.capacity[key]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            val = val - equipped["Capacity"][attr]
            transaction.append([_type, "Capacity", key, val, old_value, widget])

        return transaction

    def build_forma_transaction(self, data, slot="", transform=""):
        print("forma")

        transaction = []

        return transaction

    def build_booster_transaction(self, data, slot="", transform=""):
        print("booster")

        transaction = []

        return transaction

    def build_jail_transaction(self, data, slot="", transform=""):
        print("jail")

        transaction = []

        _type = type(data).__name__
        equipped = self.character.jail

        # burden
        for attr, val in data.burden.items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than jail
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            val = val - equipped.burden[attr]
            transaction.append([_type, "Burden", attr, val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # defense
        for attr, val in data.defense.items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            # todo comment
            old_value = self.character.defense[attr]
            val = val - equipped.defense[attr]
            transaction.append([_type, "Defense", attr, val, old_value, widget])

        # balance
        widget = self.char_to_widget_mapping["Balance"]
        # todo comment
        old_value = self.character.balance
        val = data.balance - equipped.balance
        transaction.append([_type, "Balance", None, val, old_value, widget])

        return transaction

    def build_defensive_transaction(self, data, slot="", transform=""):
        print("defensive")

        transaction = []

        _type = type(data).__name__
        transformed = data.transforms[transform]
        equipped_transform = self.character.transform["Defensive"]
        equipped = self.character.defensive_forma.transforms[equipped_transform]

        # burden
        for attr, val in transformed["Burden"].items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            val = val - equipped["Burden"][attr]
            transaction.append([_type, "Burden", attr, val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # defense
        # TODO some Defensive Formae have silly defense values like 0.96000004 or 1.8374999 - shall we simplify them?
        for attr, val in transformed["Defense"].items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            # todo comment
            old_value = self.character.defense[attr]
            val = val - equipped["Defense"][attr]
            transaction.append([_type, "Defense", attr, val, old_value, widget])

        # guarding defense
        for attr, val in transformed["GuardingDefense"].items():
            widget = self.char_to_widget_mapping["GuardingDefense_" + attr]
            # todo comment
            old_value = self.character.guarding_defense[attr]
            val = val - equipped["GuardingDefense"][attr]
            transaction.append([_type, "GuardingDefense", attr, val, old_value, widget])

        # resistance
        #
        # seems attributes also affect resistance, but for now let's ignore it
        for attr, val in transformed["Resistance"].items():
            widget = self.char_to_widget_mapping["Resistance_" + attr]
            # todo comment
            old_value = self.character.resistance[attr]
            val = val - equipped["Resistance"][attr]
            transaction.append([_type, "Resistance", attr, val, old_value, widget])

        # balance
        widget = self.char_to_widget_mapping["Balance"]
        # todo comment
        old_value = self.character.balance
        val = transformed["Balance"] - equipped["Balance"]
        transaction.append([_type, "Balance", None, val, old_value, widget])

        # stamina guard cost
        widget = self.char_to_widget_mapping["StaminaGuardCost"]
        # todo comment
        old_value = self.character.stamina_guard_cost
        val = transformed["StaminaGuardCost"] - equipped["StaminaGuardCost"]
        transaction.append([_type, "StaminaGuardCost", None, val, old_value, widget])

        return transaction

    def build_offensive_transaction(self, data, slot="", transform=""):
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
