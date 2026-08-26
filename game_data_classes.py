from fractions import Fraction


class Weapon:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        self.type = ""  # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
        self.transforms = {
            "Weapon_Off": {
                "Bleed": 0,
                "Capacity": {
                    "Reliability": 0,
                    "Handling": 0,
                    "Conversion": 0,
                    "Conductivity": 0,
                },
                "Burden": {
                    "Strength": 0,
                    "Dexterity": 0,
                    "Mind": 0,
                    "Willpower": 0,
                    "Vitality": 0,
                    "Fortitude": 0,
                },
                "Scaling": "TODO"
            }
        }
        self.favorite = False

        if not doc:
            self.name += "Weapon " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.transforms = dict()
        for transform in doc["Transforms"]:
            key = transform["Name"]
            self.transforms[key] = transform
            self.transforms[key].pop("Name")


class Forma:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
        # Magic Range Long, Magic Range Short, Assistance Attack, Assistance Defense, Assistance Other
        self.type = ""
        self.ichor_cost = 0
        self.favorite = False

        self.capacity = {
            "Reliability": 0,
            "Handling": 0,
            "Conversion": 0,
            "Conductivity": 0,
        }

        self.matching_weapons = {
            "SingleSword": True,
            "GreatSword": True,
            "DualSword": True,
            "Bayonet": True,
            "Halberd": True,
            "Hammer": True,
            "RuneBlade": True,
            "": False,  # default type when no Weapon equipped
        }

        if not doc:
            self.name = "Forma " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.ichor_cost = doc["IchorCost"]
        self.capacity = doc["Capacity"]
        self.matching_weapons = doc["WeaponMatch"]
        self.matching_weapons[""] = False


class Booster:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        self.type = ""  # 0, 1, 2, 3
        self.conditions = [{}]
        self.favorite = False
        self.equipped = False
        self.active = False

        self.burden = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        if not doc:
            self.name = "Booster " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.burden = doc["Burden"]
        # TODO instead of conditions like this [{...}, {...}, {...}] or [{}] when empty
        # do conditions like this {"1": {...}, "2": {...}, "3": {...}} or {} when empty - easier to iterate
        # or just get rid of remembering multiple conditions separately,
        # and make special case for only such booster - Phalanx I
        self.conditions = doc["Conditions"]
        if all([len(x) == 0 for x in self.conditions]):
            # boosters without conditions are always active, except the placeholder for making booster slot empty
            self.active = True


class BloodCode:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.bloodline = ""
        self.bleed = 0
        self.ichor = 0
        self.balance = 0
        self.traits = []
        self.favorite = False

        self.attributes = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        # for negative effects
        self.burden = {
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

        self.resistance = {
            "Disease": 0,
            "Wound": 0,
            "Bleed": 0,
            "Curse": 0,
        }

        if not doc:
            self.name = "Blood Code"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.bloodline = doc["Bloodline"]
        self.bleed = doc["Bleed"]
        self.ichor = doc["Ichor"]
        self.balance = doc["Balance"]
        # self.traits = []
        self.attributes = doc["Attributes"]
        # self.burden = doc["Burden"]
        self.defense = {k: Fraction(v) for k, v in doc["Defense"].items()}
        self.resistance = doc["Resistance"]
        self.traits = doc["Traits"]

        for trait in self.traits:
            burden = trait.get("Burden")
            if burden and not trait["Conditions"]:
                for attribute, value in burden.items():
                    self.burden[attribute] += value

        # print("\n\n", self.name)
        # for k, v in self.burden.items():
        #     print(k, v)


class Jail:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.type = ""
        self.balance = 0
        # self.favorite = False  # NOT USED

        self.burden = {
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

        if not doc:
            self.name = "Jail"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.balance = doc["Balance"]
        self.burden = doc["Burden"]
        self.defense = {k: Fraction(v) for k, v in doc["Defense"].items()}


class DefensiveForma:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.type = ""
        self.ichor_cost = 0
        self.transforms = {
            "Defensive_Off": {
                "StaminaGuardCost": 0,
                "Balance": 0,
                "Burden": {
                    "Strength": 0,
                    "Dexterity": 0,
                    "Mind": 0,
                    "Willpower": 0,
                    "Vitality": 0,
                    "Fortitude": 0,
                },
                "Defense": {
                    "Slash": Fraction(0, 10),
                    "Crush": Fraction(0, 10),
                    "Pierce": Fraction(0, 10),
                    "Blood": Fraction(0, 10),
                    "Fire": Fraction(0, 10),
                    "Ice": Fraction(0, 10),
                    "Lightning": Fraction(0, 10),
                },
                "GuardingDefense": {
                    "Slash": 0,
                    "Crush": 0,
                    "Pierce": 0,
                    "Blood": 0,
                    "Fire": 0,
                    "Ice": 0,
                    "Lightning": 0,
                },
                "Resistance": {
                    "Disease": 0,
                    "Wound": 0,
                    "Bleed": 0,
                    "Curse": 0,
                }
            }
        }
        self.favorite = False

        if not doc:
            self.name = "Defensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.ichor_cost = doc["IchorCost"]
        self.transforms = dict()
        for transform in doc["Transforms"]:
            key = transform["Name"]
            defense = transform["Defense"]
            defense = {k: Fraction(v) for k, v in defense.items()}
            transform["Defense"] = defense
            self.transforms[key] = transform
            self.transforms[key].pop("Name")


class OffensiveForma:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.bleed = 0
        self.ichor_cost = 0
        self.scaling = {}
        # self.favorite = False  # NOT USED

        if not doc:
            self.name = "Offensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.bleed = doc["Bleed"]
        self.ichor_cost = doc["IchorCost"]
        self.scaling = doc["Scaling"]
