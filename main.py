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
        self.weapons = {
            "Weapon_1": Weapon(dummy_number=1),
            "Weapon_2": Weapon(dummy_number=2),
        }
        self.offensive_forma = OffensiveForma()
        self.defensive_forma = DefensiveForma()
        self.jail = Jail()
        self.formae = {
            "Weapon_1_Forma_1": Forma(dummy_number=1),
            "Weapon_1_Forma_2": Forma(dummy_number=2),
            "Weapon_1_Forma_3": Forma(dummy_number=3),
            "Weapon_1_Forma_4": Forma(dummy_number=4),
            "Weapon_2_Forma_1": Forma(dummy_number=1),
            "Weapon_2_Forma_2": Forma(dummy_number=2),
            "Weapon_2_Forma_3": Forma(dummy_number=3),
            "Weapon_2_Forma_4": Forma(dummy_number=4),
        }
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
        Replaces UI values with transaction values.
        Transaction value are stored in self.last_transaction.
        Does NOT change anything in Character until transaction is committed.

        :return: None
        """
        transaction = self.build_transaction(data, slot, transform)

        attributes = dict()

        # TODO rename "value" to "diff" to be more accurate
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
                    # 2 decimal places format for floating point (Fraction in this case) just like ingame
                    # Fractions are used because adding and subtracting Floats many times could introduce errors
                    widget.setText(str(format(new_value, "0.2f")))
                elif var == "Stylesheet":
                    widget.setStyleSheet(value)
                else:
                    widget.setText(str(value + old_value))

        self.last_transaction = transaction

    def rollback_transaction(self):
        """
        Replaces UI values with old values stored in transaction.

        Need to do this if there is a non-committed transaction
        because e.g a previous booster may affect more things than new booster
        so just overwriting with new values is not enough.

        Resets last transaction.

        :return: None
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
                    # 2 decimal places format for floating point (Fraction in this case) just like ingame
                    # Fractions are used because adding and subtracting Floats many times could introduce errors
                    widget.setText(str(format(old_value, "0.2f")))
                elif var == "Stylesheet":
                    widget.setStyleSheet(old_value)
                else:
                    widget.setText(str(old_value))

        self.last_transaction = []

    def commit_transaction(self, data, slot="", transform=""):
        """
        Update Character values by adding values stored in transaction.
        Resets last transaction.

        :return: None
        """
        if not self.last_transaction:
            return

        # Overwrite Character item with item selected in transaction.
        # Does not impact Character parameters immediately, only on future transactions.
        _type = type(data).__name__
        if _type == "Weapon":
            self.character.weapons[slot] = data
            self.character.transform[slot] = transform
        elif _type == "BloodCode":
            self.character.blood_code = data
        elif _type == "Jail":
            self.character.jail = data
        elif _type == "DefensiveForma":
            self.character.defensive_forma = data
            self.character.transform["Defensive"] = transform
        elif _type == "Forma":
            self.character.formae[slot] = data

        # Update Character parameters
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
        Builds transaction based on data by calling handler for given data class.

        :return: list - transaction
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
            # The only handling needed for Weapon Rack in Blood Code,
            # is checking if it's attribute condition is fulfilled, and if it changes then handling the impact
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

        stylesheet, transform_widget, selected, equipped, other_equipped = self.handle_weapon_transform(data, slot, transform)

        # add red border to transform button on invalid transform
        transaction.append([_type, "Stylesheet", None, stylesheet, transform_widget.styleSheet(), transform_widget])

        # burden
        for attr, val in selected["Burden"].items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            new_val = self.get_burden_after_dual_wielding(attr, val, equipped, other_equipped)
            # if attr == "Willpower":
            #     print("final", new_val, "current", val, "other", val_other, "equipped", val_equipped, "val_equipped_other", val_equipped_other)
            transaction.append([_type, "Burden", attr, new_val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # Bleed
        # todo comment
        key = slot
        val = selected["Bleed"] - equipped["Bleed"]
        transaction.append([_type, "Bleed", key, val, self.character.bleed[key], self.char_to_widget_mapping[key + "_Bleed"]])

        # capacity
        for attr, val in selected["Capacity"].items():
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

    def handle_weapon_transform(self, data, slot, transform):
        """
        Handle transform logic and return values for later use.

        Show red border around transform button if transform is not possible.
        - some weapons cannot be transformed at all
        - or do not have all transforms (e.g. poison weapon doesn't have poison transform)
        If Weapon (selected or equipped in any slot) has incompatible transform, return the weapon's default transform.

        :param data: Weapon
        :param slot: string
        :param transform: string
        :return:
            stylesheet: string
            transform_widget: transform button for selected weapon
            selected: dict - transform values for weapon selected in transaction
            equipped: dict - transform values for weapon equipped before transaction
            other_equipped: dict - transform values for weapon equipped in other weapon slot
        """
        other_slot = "Weapon_2" if slot == "Weapon_1" else "Weapon_1"
        transform_widget = self.char_to_widget_mapping[slot + "_Transform"]

        if transform in data.transforms:
            selected = data.transforms[transform]

            # set stylesheet for valid state
            stylesheet = "#Transform_" + slot + "_Button:hover { border: 1px solid #b6a98d; }"
        else:
            selected = data.transforms["Weapon_Off"]

            # set stylesheet for invalid state
            stylesheet = u"""
                    #Transform_{0}_Button {{ border: 1px solid red; }}
                    #Transform_{0}_Button:hover {{ border: 1px solid #b6a98d; }}
                """.format(slot)

        equipped_transform = self.character.transform[slot]
        if equipped_transform not in self.character.weapons[slot].transforms:
            equipped_transform = "Weapon_Off"
        equipped = self.character.weapons[slot].transforms[equipped_transform]

        other_equipped_transform = self.character.transform[other_slot]
        if other_equipped_transform not in self.character.weapons[other_slot].transforms:
            other_equipped_transform = "Weapon_Off"
        other_equipped = self.character.weapons[other_slot].transforms[other_equipped_transform]

        return stylesheet, transform_widget, selected, equipped, other_equipped

    def get_burden_after_dual_wielding(self, attr, val, equipped, other_equipped):
        """
        Return attribute burden value after accounting for dual wielding (if any)

        If both weapons have burden for same attribute the LOWER burden is halved (rounded down).
        With Weapon Rack booster (not implemented yet) the LOWER burden is set to 0.

        :param attr: string
        :param val: int
        :param equipped: Weapon
        :param other_equipped: Weapon
        :return: int
        """
        # Dual Wielding burden
        val_other = other_equipped["Burden"][attr]
        val_equipped = equipped["Burden"][attr]
        val_equipped_other = other_equipped["Burden"][attr]

        # TODO add handling for Weapon Rack
        # if dual wielding calc needed (weapons in this slot and other slot both have non-zero burden for same attr)
        if val_other != 0:
            if equipped["Burden"][attr] > other_equipped["Burden"][attr]:
                # if equipped weapon has HIGHER burden (is not halved)
                # take HALF of other weapon burden as equip load
                # or NO value if Weapon Rack is active
                val_equipped_other = floor(val_equipped_other / 2)
            else:
                # if equipped weapon has LOWER burden (is halved)
                # take HALF of equipped weapon burden as equip load
                # or NO value if Weapon Rack is active
                val_equipped = floor(val_equipped / 2)

            # - pick the WHOLE value from weapon with HIGHER burden
            # - and take HALF value (rounded down) from weapon with LOWER burden
            # - or NO value from weapon with LOWER burden if Weapon Rack is active
            if val_other > val:
                val = floor(val / 2)
            else:
                val_other = floor(val_other / 2)

        return val + val_other - val_equipped - val_equipped_other

    def build_forma_transaction(self, data, slot, transform=""):
        print("forma")

        transaction = []

        _type = type(data).__name__
        equipped = self.character.formae[slot]

        # matching weapons

        # capacity
        # TODO transform impact on capacity
        # TODO weapon change impact on capacity
        #
        # for going over capacity, it would be much easier to only highlight the capacity number
        # rather than also highlighting forma which caused it
        # because there are many scenarios where clearing highlight after going under capacity is tricky
        # like forma which previously was highlighted staying red, despite removal of other forma while lowered capacity enough
        # BUT possibly we will have to iterate over all formas anyways, because of MATCHING WEAPONS ?
        #
        for attr, val in data.capacity.items():
            # get "Weapon_X" from "Weapon_X_Forma_X"
            key = slot[:8] + "_" + attr
            widget_capacity = self.char_to_widget_mapping[key]
            widget_forma = self.char_to_widget_mapping[slot]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.capacity[key]
            val = val - equipped.capacity[attr]
            max = self.character.capacity[key + "_Max"]
            # print(val, old_value, max)

            if val + old_value <= max:
                # capacity ok
                stylesheet_forma = "#" + slot + ":hover { border: 1px solid #c2c2c2; }"
                stylesheet_capacity = "{}"
            else:
                # capacity exceeded
                stylesheet_forma = u"""
                        #{0} {{ border: 1px solid red; }}
                        #{0}:hover {{ border: 1px solid #c2c2c2; }}
                    """.format(slot)
                stylesheet_capacity = "border: 1px solid red;"

            if data.type == "":
                # removing forma, treat as capacity ok but only for widget_forma
                # widget_capacity should retain red border if above maximum
                stylesheet_forma = "#" + slot + ":hover { border: 1px solid #c2c2c2; }"

            # if stylesheet_forma != widget_forma.styleSheet():
            # transaction.append([_type, "Stylesheet", None, stylesheet_forma, widget_forma.styleSheet(), widget_forma])

            # if stylesheet_capacity != widget_capacity.styleSheet():
            transaction.append([_type, "Stylesheet", None, stylesheet_capacity, widget_capacity.styleSheet(), widget_capacity])

            transaction.append([_type, "Capacity", key, val, old_value, widget_capacity])

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

        stylesheet, transform_widget, selected, equipped = self.handle_defensive_transform(data, "Defensive", transform)

        # add red border to transform button on invalid transform
        transaction.append([_type, "Stylesheet", None, stylesheet, transform_widget.styleSheet(), transform_widget])

        # burden
        for attr, val in selected["Burden"].items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            # The only handling needed for Weapon Rack in Defensive Forma,
            # is checking if it's attribute condition is fulfilled, and if it changes then handling the impact
            val = val - equipped["Burden"][attr]
            transaction.append([_type, "Burden", attr, val, old_value, widget])

        # traits

        # boosters

        # Dodge Effectiveness

        # defense
        # TODO some Defensive Formae have silly defense values like 0.96000004 or 1.8374999 - shall we simplify them?
        for attr, val in selected["Defense"].items():
            widget = self.char_to_widget_mapping["Defense_" + attr]
            # todo comment
            old_value = self.character.defense[attr]
            val = val - equipped["Defense"][attr]
            transaction.append([_type, "Defense", attr, val, old_value, widget])

        # guarding defense
        for attr, val in selected["GuardingDefense"].items():
            widget = self.char_to_widget_mapping["GuardingDefense_" + attr]
            # todo comment
            old_value = self.character.guarding_defense[attr]
            val = val - equipped["GuardingDefense"][attr]
            transaction.append([_type, "GuardingDefense", attr, val, old_value, widget])

        # resistance
        #
        # seems attributes also affect resistance, but for now let's ignore it
        for attr, val in selected["Resistance"].items():
            widget = self.char_to_widget_mapping["Resistance_" + attr]
            # todo comment
            old_value = self.character.resistance[attr]
            val = val - equipped["Resistance"][attr]
            transaction.append([_type, "Resistance", attr, val, old_value, widget])

        # balance
        widget = self.char_to_widget_mapping["Balance"]
        # todo comment
        old_value = self.character.balance
        val = selected["Balance"] - equipped["Balance"]
        transaction.append([_type, "Balance", None, val, old_value, widget])

        # stamina guard cost
        widget = self.char_to_widget_mapping["StaminaGuardCost"]
        # todo comment
        old_value = self.character.stamina_guard_cost
        val = selected["StaminaGuardCost"] - equipped["StaminaGuardCost"]
        transaction.append([_type, "StaminaGuardCost", None, val, old_value, widget])

        return transaction

    def handle_defensive_transform(self, data, slot, transform):
        """
        Handle transform logic and return values for later use.

        Show red border around transform button if transform is not possible.
        - some defensive forma cannot be transformed at all
        - or do not have all transforms (e.g. poison weapon doesn't have poison transform)
        If defensive forma (selected or equipped) has incompatible transform, return the default transform.

        :param data: DefensiveForma
        :param slot: string
        :param transform: string
        :return:
            stylesheet: string
            transform_widget: transform button for selected defensive forma
            selected: dict - transform values for defensive forma selected in transaction
            equipped: dict - transform values for defensive forma equipped before transaction
        """
        transform_widget = self.char_to_widget_mapping[slot + "_Transform"]

        if transform in data.transforms:
            selected = data.transforms[transform]

            # set stylesheet for valid state
            stylesheet = "#Transform_" + slot + "_Button:hover { border: 1px solid #b6a98d; }"
        else:
            selected = data.transforms["Defensive_Off"]

            # set stylesheet for invalid state
            stylesheet = u"""
                    #Transform_{0}_Button {{ border: 1px solid red; }}
                    #Transform_{0}_Button:hover {{ border: 1px solid #b6a98d; }}
                """.format(slot)

        equipped_transform = self.character.transform[slot]
        if equipped_transform not in self.character.defensive_forma.transforms:
            equipped_transform = "Defensive_Off"
        equipped = self.character.defensive_forma.transforms[equipped_transform]

        return stylesheet, transform_widget, selected, equipped

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
