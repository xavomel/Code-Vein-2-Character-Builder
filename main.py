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
        self.boosters = {
            "Booster_1": Booster(dummy_number=1),
            "Booster_2": Booster(dummy_number=2),
            "Booster_3": Booster(dummy_number=3),
            "Booster_4": Booster(dummy_number=4),
            "Booster_5": Booster(dummy_number=5),
            "Booster_6": Booster(dummy_number=6),
        }

        self.traits = []

        self.overburden = False
        self.balance = 0
        self.ichor = 0
        self.dodge_effectiveness = "Medium"
        self.stamina_guard_cost = 0
        self.transform = {
            "Weapon_1": "Weapon_Off",
            "Weapon_2": "Weapon_Off",
            "Defensive": "Defensive_Off",
        }
        self.bleed = {
            "Weapon_1": 0,
            "Weapon_2": 0,
            "Offensive": 0,
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

        self.legal = {
            "Weapon_1_Forma_1": True,
            "Weapon_1_Forma_2": True,
            "Weapon_1_Forma_3": True,
            "Weapon_1_Forma_4": True,
            "Weapon_2_Forma_1": True,
            "Weapon_2_Forma_2": True,
            "Weapon_2_Forma_3": True,
            "Weapon_2_Forma_4": True,
            "Weapon_1_Reliability": True,
            "Weapon_1_Handling": True,
            "Weapon_1_Conversion": True,
            "Weapon_1_Conductivity": True,
            "Weapon_2_Reliability": True,
            "Weapon_2_Handling": True,
            "Weapon_2_Conversion": True,
            "Weapon_2_Conductivity": True,
            "Weapon_1_Transform": True,
            "Weapon_2_Transform": True,
            "Defensive_Transform": True,
        }


class Builder:
    def attribute_booster(self, attr, val, add, transaction_list):
        var = "Attributes"
        widget = self.char_to_widget_mapping["Attribute_" + attr]
        old_value = self.character.attributes[attr]
        val = val if add else -val

        idx_to_remove = []
        for idx, transaction in enumerate(transaction_list):
            if var == transaction[1] and attr == transaction[2]:
                # merge transactions of same type
                val += transaction[3]
                idx_to_remove.append(idx)

        for idx in reversed(idx_to_remove):
            # remove transactions that are included in the merged transaction
            transaction_list.pop(idx)

        transaction_list.append(["Booster", var, attr, val, old_value, widget])

    def resistance_booster(self, attr, val, add, transaction_list):
        var = "Resistance"
        widget = self.char_to_widget_mapping["Resistance_" + attr]
        old_value = self.character.resistance[attr]
        val = val if add else -val

        idx_to_remove = []
        for idx, transaction in enumerate(transaction_list):
            if var == transaction[1] and attr == transaction[2]:
                # merge transactions of same type
                val += transaction[3]
                idx_to_remove.append(idx)

        for idx in reversed(idx_to_remove):
            # remove transactions that are included in the merged transaction
            transaction_list.pop(idx)

        transaction_list.append(["Booster", var, attr, val, old_value, widget])

    def ichor_booster(self, val, add, transaction_list):
        var = "Ichor"
        widget = self.char_to_widget_mapping["Ichor"]
        old_value = self.character.ichor
        val = val if add else -val

        idx_to_remove = []
        for idx, transaction in enumerate(transaction_list):
            if var == transaction[1]:
                # merge transactions of same type
                val += transaction[3]
                idx_to_remove.append(idx)

        for idx in reversed(idx_to_remove):
            # remove transactions that are included in the merged transaction
            transaction_list.pop(idx)

        transaction_list.append(["Booster", var, None, val, old_value, widget])

    def balance_booster(self, val, add, transaction_list):
        var = "Balance"
        widget = self.char_to_widget_mapping["Balance"]
        old_value = self.character.balance
        val = val if add else -val

        idx_to_remove = []
        for idx, transaction in enumerate(transaction_list):
            if var == transaction[1]:
                # merge transactions of same type
                val += transaction[3]
                idx_to_remove.append(idx)

        for idx in reversed(idx_to_remove):
            # remove transactions that are included in the merged transaction
            transaction_list.pop(idx)

        transaction_list.append(["Booster", var, None, val, old_value, widget])

    def shrugged_burden_booster(self):
        return []

    # seems there's a bug where this booster reduces burden attr that is not present on 2nd weapon
    # this may happen if other booster in this transaction has increased burden of same attr
    # TODO ensure we only take weapon burden attr into account, maybe by filtering by _type ?
    def weapon_rack_booster(self, dummy, add, transaction_list):
        transform_1 = self.character.transform["Weapon_1"]
        transform_2 = self.character.transform["Weapon_1"]
        weapon_1_burden = self.character.weapons["Weapon_1"].transforms[transform_1]["Burden"]
        weapon_2_burden = self.character.weapons["Weapon_2"].transforms[transform_2]["Burden"]

        for attr, val in weapon_1_burden.items():
            val_other = weapon_2_burden[attr]

            val_equipped = weapon_1_burden[attr]
            val_equipped_other = weapon_2_burden[attr]

            if val_other != 0:
                if weapon_1_burden[attr] > weapon_2_burden[attr]:
                    # if equipped weapon has HIGHER burden (is not halved)
                    # take HALF of other weapon burden as equip load
                    # or NO value if Weapon Rack is active
                    if add:
                        val_equipped_other = 0
                    else:
                        val_equipped_other = floor(val_equipped_other / 2)

                    # subtract lesser value from greater value
                    val = val_equipped - val_equipped_other
                else:
                    # if equipped weapon has LOWER burden (is halved)
                    # take HALF of equipped weapon burden as equip load
                    # or NO value if Weapon Rack is active
                    if add:
                        val_equipped = 0
                    else:
                        val_equipped = floor(val_equipped / 2)

                    # subtract lesser value from greater value
                    val = val_equipped_other - val_equipped

                widget = self.char_to_widget_mapping["Burden_" + attr]
                old_value = self.character.burden[attr]
                new_val = old_value - val
                new_val = -new_val if add else new_val

                print("****** final", new_val, "val", val, "val_other", val_other, "val_equipped", val_equipped, "val_equipped_other", val_equipped_other, "add", add, "old_value", old_value)

                idx_to_remove = []
                for idx, transaction in enumerate(transaction_list):
                    if "Burden" == transaction[1] and attr == transaction[2]:
                        # merge transactions of same type
                        new_val += transaction[3]
                        idx_to_remove.append(idx)

                for idx in reversed(idx_to_remove):
                    # remove transactions that are included in the merged transaction
                    transaction_list.pop(idx)

                transaction_list.append(["Booster", "Burden", attr, new_val, old_value, widget])

    def bloodline_agnostic_booster(self, bloodline, add, transaction_list):
        character_bloodline = self.character.bloodline
        old_value = character_bloodline

        idx_to_remove = []
        for idx, transaction in enumerate(transaction_list):
            if transaction[1] == "Bloodline":
                # merge transactions of same type
                # we don't need the bloodline value from transaction, it will be overwritten
                idx_to_remove.append(idx)

        for idx in reversed(idx_to_remove):
            # remove transactions that are included in the merged transaction
            transaction_list.pop(idx)

        if add:
            value = bloodline  # Agnostic will be set here
            transaction_list.append(["Booster", "Bloodline", None, value, old_value, None])
        else:
            value = self.character.blood_code.bloodline  # restore original bloodline from blood code
            transaction_list.append(["Booster", "Bloodline", None, value, old_value, None])

    def glutton_booster(self):
        # need to implement losing 2nd food buff if booster is active?
        return []

    def ignore_trait_attribute_req_booster(self):
        return []

    def resistance_multiplier_booster(self):
        return []

    def bleed_multiplier_booster(self):
        return []

    def balance_multiplier_booster(self):
        return []

    def text_booster(self):
        return []

    booster_effects = {
        "Dexterity Booster - Overload": [[attribute_booster, "Dexterity", 5]],
        "Dexterity Booster":            [[attribute_booster, "Dexterity", 2]],
        "Fortitude Booster - Overload": [[attribute_booster, "Fortitude", 5]],
        "Fortitude Booster":            [[attribute_booster, "Fortitude", 2]],
        "Mind Booster - Overload":      [[attribute_booster, "Mind", 5]],
        "Mind Booster":                 [[attribute_booster, "Mind", 2]],
        "Strength Booster - Overload":  [[attribute_booster, "Strength", 5]],
        "Strength Booster":             [[attribute_booster, "Strength", 2]],
        "Vitality Booster - Overload":  [[attribute_booster, "Vitality", 5]],
        "Vitality Booster":             [[attribute_booster, "Vitality", 2]],
        "Willpower Booster - Overload": [[attribute_booster, "Willpower", 5]],
        "Willpower Booster":            [[attribute_booster, "Willpower", 2]],
        "The Tie That Binds: Holly":    [[attribute_booster, "Willpower", 10]],
        "The Tie That Binds: Josée":    [[attribute_booster, "Strength", 10]],
        "The Tie That Binds: Lyle":     [[attribute_booster, "Dexterity", 10]],
        "The Tie That Binds: Noah":     [[attribute_booster, "Fortitude", 10], [ignore_trait_attribute_req_booster]],
        "The Tie That Binds: Zenon":    [[attribute_booster, "Mind", 10], [ichor_booster, 22]],
        "Ichor Maximizer - Unum":       [[ichor_booster, 5]],
        "Ichor Maximizer - Duo":        [[ichor_booster, 6]],
        "Ichor Maximizer - Tria":       [[ichor_booster, 3]],
        # resistance
        "Resistance Booster - Blood":   [[resistance_booster, "Bleed", 40]],
        "Resistance Booster - Curse":   [[resistance_booster, "Curse", 40]],
        "Resistance Booster - Disease": [[resistance_booster, "Disease", 40]],
        "Resistance Booster - Wound":   [[resistance_booster, "Wound", 40]],
        # special
        "Shrugged Burden":              [[shrugged_burden_booster]],
        "Weapon Rack":                  [[weapon_rack_booster, "Dummy"]],
        "Bloodline Agnostic":           [[bloodline_agnostic_booster, "Agnostic"]],
        "Glutton":                      [[glutton_booster]],
        "Resistance Booster":           [[resistance_multiplier_booster]],
        "Hemorrhaging Weapon Boost":    [[bleed_multiplier_booster]],
        "Balance Booster":              [[balance_multiplier_booster]],
        # balance
        "Phalanx J":                    [[balance_booster, 100]],
        "Phalanx I":                    [[text_booster], [balance_booster, -25], [text_booster]],  # has multiple effects
    }

    def condition_none(self):
        return True

    def condition_attribute(self, doc, transaction):
        print(doc)
        for attr, value in doc.items():
            character_value = self.character.attributes[attr]
            for operation in transaction:
                print("      condition_attribute", operation)
                if operation[1] == "Attributes" and operation[2] == attr:
                    character_value += operation[3]

            print("condition_attribute", character_value, value)
            if character_value < value:
                return False
        return True

    # whether margin of attr X is at least Y
    # TODO use character.margin instead !
    def condition_margin(self, doc, transaction):
        print(doc)
        for attr, value in doc.items():
            character_attribute = self.character.attributes[attr]
            character_burden = self.character.burden[attr]
            for operation in transaction:
                if operation[1] == "Attributes" and operation[2] == attr:
                    character_attribute += operation[3]
                if operation[1] == "Burden" and operation[2] == attr:
                    character_burden += operation[3]

            character_margin = character_attribute - character_burden
            print("condition_margin", character_attribute, character_burden, character_margin, value)
            if character_margin < value:
                return False

    # whether burden of attr X is at least Y
    # test case: Phalanx I
    def condition_burden(self, doc, transaction):
        print(doc)
        for attr, value in doc.items():
            character_value = self.character.burden[attr]
            for operation in transaction:
                if operation[1] == "Burden" and operation[2] == attr:
                    character_value += operation[3]

            print("condition_burden", character_value, value)
            if character_value < value:
                return False
        return True

    # whether burden of attr X is at most Y
    def condition_burden_max(self, doc, transaction):
        print(doc)
        for attr, value in doc.items():
            character_value = self.character.burden[attr]
            for operation in transaction:
                if operation[1] == "Burden" and operation[2] == attr:
                    character_value += operation[3]

            print("condition_burden_max", character_value, value)
            if character_value > value:
                return False
        return True

    # TODO use character.margin instead !
    # test case overburden false - Usurper or Bloodline Agnostic
    def condition_overburden(self, wanted_overburden, transaction):
        print("condition_overburden: wanted", wanted_overburden)
        for attr, value in self.character.attributes.items():
            character_attribute = value
            character_burden = self.character.burden[attr]
            for operation in transaction:
                if operation[1] == "Attributes" and operation[2] == attr:
                    character_attribute += operation[3]
                if operation[1] == "Burden" and operation[2] == attr:
                    character_burden += operation[3]

            character_margin = character_attribute - character_burden
            if character_margin < 0:
                # if margin is negative we are overburdened
                if not wanted_overburden:
                    return False
                else:
                    return True

        if not wanted_overburden:
            return True
        else:
            return False

    # test case: Shrugged Burden
    def condition_bloodline(self, bloodline, transaction):
        print(bloodline)

        character_bloodline = self.character.bloodline
        for operation in transaction:
            if operation[1] == "Bloodline":
                character_bloodline = operation[3]

        print("condition_bloodline", bloodline, character_bloodline)
        if character_bloodline == "Agnostic":
            return True
        elif character_bloodline != bloodline:
            return False
        return True

    booster_and_trait_conditions = {
        "Attribute": condition_attribute,
        "Margin": condition_margin,
        "Burden": condition_burden,
        "BurdenMax": condition_burden,
        "Overburden": condition_overburden,
        "Bloodline": condition_bloodline,
    }

    def __init__(self, window):
        # give access to builder_ui methods without making Builder a subclass of Ui_MainWindow
        self.window = window

        self.character = Character()
        self.blood_codes = dict()
        self.weapons = dict()
        self.boosters = dict()
        self.formae = dict()
        self.offensive_formae = dict()
        self.defensive_formae = dict()
        self.jails = dict()
        self.translation = dict()
        self.build_save_order = dict()
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
        # this is necessary to ensure any codes remain backward compatible, even if new items are added to game
        # this json should only be added to
        # we should NEVER re-order items
        #
        # json could be modified, e.g. if item name is wrong
        # like "Resistance Booster - Blood" should be "Resistance Booster - Bleed" it might be renamed in DLC
        self.build_save_order = open_json("GameData/BuildSaveOrder.json")

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
        print("* start_transaction")
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
                elif var == "Active":
                    print("transaction", widget, key, old_value)
                    booster_slot, booster_name = key
                    self.window.set_booster_icon(widget, booster_name, value)
                else:
                    widget.setText(str(value + old_value))

        self.last_transaction = transaction

    # should we rollback transactions in reverse order?
    # so that if we have 2 transactions of same type:
    # - then old value from 1st operation should be the final value, not from 2nd operation
    #
    # probably unecessary as long as we are merging transactions
    #
    # but is this really a problem? until we commit we can always get old value from character
    #
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
        print("* rollback_transaction")

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
                elif var == "Active":
                    print("rollback", widget, key, old_value)
                    booster_slot, booster_name = key
                    self.window.set_booster_icon(widget, booster_name, old_value)
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
        print("* commit_transaction", data, slot, transform)

        # Overwrite Character item with item selected in transaction.
        # Does not impact Character parameters immediately, only on future transactions.
        _type = type(data).__name__
        if _type == "Weapon":
            self.character.weapons[slot] = data
            self.character.transform[slot] = transform
            self.window.update_weapon_icon_text(data.name, slot, transform)
        elif _type == "BloodCode":
            self.character.blood_code = data
            self.window.update_blood_code_icon_text(data.name)
        elif _type == "Jail":
            self.character.jail = data
            self.window.update_jail_icon_text(data.name)
        elif _type == "DefensiveForma":
            self.character.defensive_forma = data
            self.character.transform["Defensive"] = transform
            self.window.update_defensive_icon_text(data.name, slot, transform)
        elif _type == "Forma":
            self.character.formae[slot] = data
            self.window.update_forma_icon_text(data.name, slot)
        elif _type == "OffensiveForma":
            self.character.offensive_forma = data
            self.window.update_offensive_icon_text(data.name)
        elif _type == "Booster":
            # selected booster will be handled in "Active" below
            pass

        # holly
        # Update Character parameters
        for _type, var, key, value, old_value, widget in self.last_transaction:
            if var == "Active":
                booster_slot, booster_name = key
                print("commit", booster_slot, booster_name, value)

                if booster_slot == slot:
                    # selected booster slot
                    previous_booster = self.character.boosters[slot]
                    previous_booster.active = False

                    # COMMENTED OUT for easier troubleshooting
                    # TODO uncomment
                    # previous_booster.equipped = False
                    # if data.type != "":
                    #     # only set for real boosters (do not set for placeholder when making booster slot empty)
                    #     data.equipped = True

                    data.active = value
                    self.character.boosters[slot] = data
                    self.window.update_boosters_icon_text(data, slot)
                else:
                    self.character.boosters[booster_slot].active = value
            elif var == "Bloodline":
                # TODO if value is Agnostic, set Character variable bloodline_agnostic to True
                # otherwise set it to False ?
                #
                # could be easy way to remember if this booster is active, but is it necessary?
                # when resolving boosters and Agnostic is active it will overwrite blood code value anyway?
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
            elif var == "Dodge":
                self.character.dodge_effectiveness = value
            elif var == "Stylesheet":
                if key:
                    legal_slot, legal_value = key
                    self.character.legal[legal_slot] = legal_value


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
        transaction.append([_type, "Bleed", "Offensive", val, self.character.bleed["Offensive"], self.char_to_widget_mapping["Offensive_Bleed"]])

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

        transform_legal, transform_slot, stylesheet, transform_widget, selected, equipped, other_equipped = self.handle_weapon_transform(data, slot, transform)
        # add red border to transform button on invalid transform
        if transform_legal != self.character.legal[transform_slot]:
            transaction.append([_type, "Stylesheet", (transform_slot, transform_legal), stylesheet, transform_widget.styleSheet(), transform_widget])

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

        # calculate capacity and highlight which capacity is exceeded
        capacity_under = dict()
        for attr, val in selected["Capacity"].items():
            key = slot + "_" + attr
            key_max = key + "_Max"
            widget = self.char_to_widget_mapping[key_max]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.capacity[key_max]
            # TODO add handling for Shrugged Burden (booster and trait)
            # remember the state of Shrugged Burden in variable for easy checking, it has big impact
            # TODO add handling for Weapon Rack
            # remember the state of Weapon Rack in variable for easy checking, it has big impact
            val = val - equipped["Capacity"][attr]

            if self.character.capacity[key] <= val + old_value:
                capacity_legal = True
                capacity_under[attr] = True
            else:
                capacity_legal = False
                capacity_under[attr] = False

            if capacity_legal != self.character.legal[key]:
                stylesheet_capacity = self.capacity_stylesheet(capacity_legal, key)
                widget_capacity = self.char_to_widget_mapping[key]
                transaction.append([_type, "Stylesheet", (key, capacity_legal), stylesheet_capacity, widget_capacity.styleSheet(), widget_capacity])

            transaction.append([_type, "Capacity", key_max, val, old_value, widget])

        # matching forma type
        # and which specific forma exceeded capacity
        #
        # this function may add new elements to the transaction
        self.handle_formae_for_weapon(transaction, _type, self.character.formae, capacity_under, slot, data.type)

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
            legal: bool
            transform_slot: string
            stylesheet: string
            transform_widget: transform button for selected weapon
            selected: dict - transform values for weapon selected in transaction
            equipped: dict - transform values for weapon equipped before transaction
            other_equipped: dict - transform values for weapon equipped in other weapon slot
        """
        other_slot = "Weapon_2" if slot == "Weapon_1" else "Weapon_1"
        transform_slot = slot + "_Transform"
        transform_widget = self.char_to_widget_mapping[transform_slot]

        if transform in data.transforms:
            selected = data.transforms[transform]
            legal = True
        else:
            selected = data.transforms["Weapon_Off"]
            legal = False
        stylesheet = self.transform_stylesheet(legal, slot)

        equipped_transform = self.character.transform[slot]
        if equipped_transform not in self.character.weapons[slot].transforms:
            equipped_transform = "Weapon_Off"
        equipped = self.character.weapons[slot].transforms[equipped_transform]

        other_equipped_transform = self.character.transform[other_slot]
        if other_equipped_transform not in self.character.weapons[other_slot].transforms:
            other_equipped_transform = "Weapon_Off"
        other_equipped = self.character.weapons[other_slot].transforms[other_equipped_transform]

        return legal, transform_slot, stylesheet, transform_widget, selected, equipped, other_equipped

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

            # TODO - can this be simplified like weapon rack?
            #
            # - pick the WHOLE value from weapon with HIGHER burden
            # - and take HALF value (rounded down) from weapon with LOWER burden
            # - or NO value from weapon with LOWER burden if Weapon Rack is active
            if val_other > val:
                val = floor(val / 2)
            else:
                val_other = floor(val_other / 2)

        return val + val_other - val_equipped - val_equipped_other

    def handle_formae_for_weapon(self, transaction, _type, formae, capacity_under, weapon_slot, weapon_type):
        """
        Handle logic for relationship between weapon and formae.
        Checks if forma is compatible with that weapon (if not show red border around forma button).
        Checks each capacity attr in forma if it's inside capacity max (if not show red border around forma button).
        If requirements are fulfilled but they were not fulfilled before, cleanup red border.

        :param transaction: list
        :param _type: string
        :param formae: dict - formae to be processed
        :param capacity_under: dict - which formae capacity attrs are under or at maximum capacity, or above it
        :param weapon_slot: string - weapon slot associated with formae
        :param weapon_type: string - weapon type for weapon slot
        :return:
        """
        for key, forma in formae.items():
            if weapon_slot not in key:
                # do not check forma for the other weapon
                continue

            if forma.type == "" or forma.matching_weapons[weapon_type]:
                # forma is legal if it is unassigned, or has matching weapon type
                forma_legal = True
            else:
                forma_legal = False

            for attr, is_under_cap in capacity_under.items():
                if forma.capacity[attr] > 0:
                    forma_legal = forma_legal and is_under_cap

            if forma_legal != self.character.legal[key]:
                stylesheet_forma = self.forma_stylesheet(forma_legal, key)
                widget_forma = self.char_to_widget_mapping[key]
                transaction.append([_type, "Stylesheet", (key, forma_legal), stylesheet_forma, widget_forma.styleSheet(), widget_forma])

    def build_forma_transaction(self, data, slot, transform=""):
        print("forma", slot)

        transaction = []

        _type = type(data).__name__
        weapon_slot = slot[:8]
        equipped_weapon = self.character.weapons[weapon_slot]
        equipped_forma = self.character.formae[slot]

        # capacity
        capacity_under = dict()
        for attr, val in data.capacity.items():
            key = weapon_slot + "_" + attr
            widget_capacity = self.char_to_widget_mapping[key]
            # fetch old attributes from character rather than blood code
            # as it contains potential values from traits, boosters, defensive, jail, weapon(s)
            old_value = self.character.capacity[key]
            val = val - equipped_forma.capacity[attr]
            max = self.character.capacity[key + "_Max"]
            # print(val, old_value, max)

            if val + old_value <= max:
                # capacity ok
                capacity_legal = True
                capacity_under[attr] = True
            else:
                capacity_legal = False
                capacity_under[attr] = False

            if capacity_legal != self.character.legal[key]:
                stylesheet_capacity = self.capacity_stylesheet(capacity_legal, key)
                transaction.append([_type, "Stylesheet", (key, capacity_legal), stylesheet_capacity, widget_capacity.styleSheet(), widget_capacity])

            transaction.append([_type, "Capacity", key, val, old_value, widget_capacity])

        # matching forma type
        # and which specific forma exceeded capacity
        formae = dict()
        for key, forma in self.character.formae.items():
            if slot == key:
                # we want all formae for the same weapon
                # but 1 forma needs to be replaced with selected forma
                formae[key] = data
            else:
                formae[key] = forma
        # this function may add new elements to the transaction
        self.handle_formae_for_weapon(transaction, _type, formae, capacity_under, weapon_slot, equipped_weapon.type)

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

        transform_legal, transform_slot, stylesheet, transform_widget, selected, equipped = self.handle_defensive_transform(data, "Defensive", transform)

        # add red border to transform button on invalid transform
        if transform_legal != self.character.legal[transform_slot]:
            transaction.append([_type, "Stylesheet", (transform_slot, transform_legal), stylesheet, transform_widget.styleSheet(), transform_widget])

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
            legal: string
            transform_slot: string
            stylesheet: string
            transform_widget: transform button for selected defensive forma
            selected: dict - transform values for defensive forma selected in transaction
            equipped: dict - transform values for defensive forma equipped before transaction
        """
        transform_slot = slot + "_Transform"
        transform_widget = self.char_to_widget_mapping[transform_slot]

        if transform in data.transforms:
            selected = data.transforms[transform]
            legal = True
        else:
            selected = data.transforms["Defensive_Off"]
            legal = False
        stylesheet = self.transform_stylesheet(legal, slot)

        equipped_transform = self.character.transform[slot]
        if equipped_transform not in self.character.defensive_forma.transforms:
            equipped_transform = "Defensive_Off"
        equipped = self.character.defensive_forma.transforms[equipped_transform]

        return legal, transform_slot, stylesheet, transform_widget, selected, equipped

    def build_offensive_transaction(self, data, slot="", transform=""):
        print("offensive")

        transaction = []

        _type = type(data).__name__

        # Bleed
        key = "Offensive"
        equipped = self.character.offensive_forma
        widget = self.char_to_widget_mapping[key + "_Bleed"]
        # todo comment
        old_value = self.character.bleed[key]
        val = data.bleed - equipped.bleed
        transaction.append([_type, "Bleed", key, val, old_value, widget])

        return transaction

    def build_booster_transaction(self, data, slot, transform=""):
        print("booster")

        transaction = []

        _type = type(data).__name__

        equipped = self.character.boosters[slot]
        if data.name == equipped.name:
            # avoid replacing booster with itself
            return []

        # burden - handle first since it's predictable
        for attr, val in data.burden.items():
            widget = self.char_to_widget_mapping["Burden_" + attr]
            old_value = self.character.burden[attr]
            # TODO add handling for Shrugged Burden (booster and trait) ?
            # TODO add handling for Weapon Rack ?
            val = val - equipped.burden[attr]
            if val != old_value:
                # EXPERIMENTAL: only update transaction if values are different
                # if values are equal it will just set same value
                transaction.append([_type, "Burden", attr, val, old_value, widget])

        # unassign old booster
        if not equipped.active:
            # if booster was inactive do not subtract anything
            pass
        else:
            # if booster was active subtract it's effects by treating it as inactive
            self.resolve_effects(equipped, active=False, transaction=transaction)

        # booster list for iteration
        # replace 1 booster with selected
        boosters = list(self.character.boosters.values())
        slot_int = int(slot.replace("Booster_", "")) - 1
        boosters[slot_int] = data

        # keep original active values for faster access
        original_active = {booster_slot: v.active for booster_slot, v in self.character.boosters.items()}

        # keep temporary active values, they will be updated for real when transaction is committed
        # treat selected booster as inactive, since it's not equipped yet
        temp_active = [x.active for x in boosters]
        temp_active[slot_int] = False

        # === booster loop ===
        # changing selected booster can impact other boosters in unpredictable ways
        # a booster in later slot can impact booster in earlier slot,
        # so need to keep iterating until active status of all boosters stops changing (including selected booster)
        #
        # an basic problematic scenario is active Bloodline Agnostic (slot 1) and active Weapon Rack (slot 2)
        # - BA is active if no overburden
        # - WR is active if STR & DEX > 18
        # - assuming BA stays active but WR doesn't
        # - then WR going inactive will cause burden to rise, potentially impacting BA
        #
        # TODO should we start iteration from slot_int (selected booster) instead of 0?
        # since it's guaranteed to change active status
        #
        # resolves effects and determines active status
        idx = 0
        unchanged = [0, 0, 0, 0, 0, 0]
        while all(unchanged) is False:
            booster = boosters[idx]
            active = temp_active[idx]
            new_active = self.check_conditions(booster, transaction)
            if active != new_active:
                print(booster.name, "not equal", active, new_active, unchanged)
                temp_active[idx] = new_active
                self.resolve_effects(booster, new_active, transaction)
            else:
                print(booster.name, "equal", active, new_active, unchanged)
                unchanged[idx] = 1

            idx += 1
            if idx == len(unchanged):
                idx = 0

        # set active status if it changed (set it always for selected booster)
        for idx, new_active in enumerate(temp_active):
            booster_slot = "Booster_" + str(idx + 1)
            if booster_slot != slot:
                old_value = original_active[booster_slot]
                if old_value != new_active:
                    booster = boosters[idx]
                    widget = self.char_to_widget_mapping[booster_slot]
                    transaction.append(["Booster", "Active", (booster_slot, booster.name), new_active, old_value, widget])
            else:
                # always send update for selected booster and do not set widget, as it should not be displayed until it's clicked
                transaction.append(["Booster", "Active", (slot, None), temp_active[slot_int], None, None])

        return transaction

    def check_conditions(self, booster, transaction):
        """
        Check if all conditions for booster are met.
        :param booster: Booster
        :param transaction: list - containing all transactions so far
        :return:
            bool
        """
        if booster.type == "":
            # empty booster
            return False

        conditions_list = booster.conditions
        for conditions in conditions_list:
            for name, values in conditions.items():
                cond_fun = self.booster_and_trait_conditions[name]
                if not cond_fun(self, values, transaction):
                    return False

        return True

    def resolve_effects(self, booster, active, transaction):
        """
        Resolve all effects for booster.
        Depending on effect the transaction will be updated (inside booster_fun).
        :param booster: Booster
        :param active: bool - whether booster is active (need to add effects) or inactive (subtract)
        :param transaction: list - containing all transactions so far
        :return:
            None
        """
        print("  resolve_effects", booster.name, active)
        booster_effects = self.booster_effects.get(booster.name, [])
        for effect in booster_effects:
            print("effect", effect)
            booster_fun = effect[0]
            arguments = effect[1:]
            if arguments:
                print("booster active", active)
                arguments.append(active)          # add or subtract
                arguments.append(transaction)     # transactions to update
                booster_fun(self, *arguments)
            else:
                booster_fun(self)

    def transform_stylesheet(self, legal, slot):
        if legal:
            return "#Transform_" + slot + "_Button:hover { border: 1px solid #b6a98d; }"
        else:
            return u"""
                    #Transform_{0}_Button {{ border: 1px solid red; }}
                    #Transform_{0}_Button:hover {{ border: 1px solid #b6a98d; }}
                """.format(slot)

    def capacity_stylesheet(self, legal, slot):
        if legal:
            return ""
        else:
            return "border: 1px solid red;"

    def forma_stylesheet(self, legal, slot):
        if legal:
            return "#" + slot + ":hover { border: 1px solid #c2c2c2; }"
        else:
            return u"""
                    #{0} {{ border: 1px solid red; }}
                    #{0}:hover {{ border: 1px solid #c2c2c2; }}
                """.format(slot)


class MainWindow(QMainWindow, builder_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.builder = Builder(self)
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
