class Weapon:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        self.type = ""  # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
        self.bleed = 0
        # self.scaling = "TODO"
        self.transformable = False
        self.transforms = {}
        self.favorite = False

        self.capacity = {
            "Reliability": 0,
            "Handling": 0,
            "Conversion": 0,
            "Conductivity": 0,
        }

        self.burden = {
            "Strength": 0,
            "Dexterity": 0,
            "Mind": 0,
            "Willpower": 0,
            "Vitality": 0,
            "Fortitude": 0,
        }

        if not doc:
            self.name += "Weapon " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.bleed = doc["Bleed"]
        # self.scaling = "TODO"
        self.capacity = doc["Capacity"]
        self.burden = doc["Burden"]

        self.transformable = doc["Transformable"]
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


class Booster:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        self.type = ""  # 0, 1, 2, 3
        self.conditions = []
        self.favorite = False

        # for positive effects
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

        if not doc:
            self.name = "Booster " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        # self.conditions = doc[""]
        # self.attributes = doc["Attributes"]
        self.burden = doc["Burden"]
        self.conditions = doc["Conditions"]


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
            "Slash": 0.0,
            "Crush": 0.0,
            "Pierce": 0.0,
            "Blood": 0.0,
            "Fire": 0.0,
            "Ice": 0.0,
            "Lightning": 0.0,
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
        self.defense = doc["Defense"]
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
            "Slash": 0.0,
            "Crush": 0.0,
            "Pierce": 0.0,
            "Blood": 0.0,
            "Fire": 0.0,
            "Ice": 0.0,
            "Lightning": 0.0,
        }

        if not doc:
            self.name = "Jail"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.balance = doc["Balance"]
        self.burden = doc["Burden"]
        self.defense = doc["Defense"]


class DefensiveForma:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.type = ""
        self.ichor_cost = 0
        self.stamina_guard_cost = 0
        self.balance = 0
        self.transformable = False
        self.transforms = {}
        self.favorite = False

        self.burden = {
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

        if not doc:
            self.name = "Defensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.ichor_cost = doc["IchorCost"]
        self.stamina_guard_cost = doc["StaminaGuardCost"]
        self.balance = doc["Balance"]
        self.burden = doc["Burden"]
        self.defense = doc["Defense"]
        self.guarding_defense = doc["GuardingDefense"]
        self.resistance = doc["Resistance"]

        self.transformable = doc["Transformable"]
        self.transforms = dict()
        for transform in doc["Transforms"]:
            key = transform["Name"]
            self.transforms[key] = transform
            self.transforms[key].pop("Name")


class OffensiveForma:
    def __init__(self, doc=None):
        self.name = ""
        self.description = ""
        self.ichor_cost = 0
        self.scaling = {}
        # self.favorite = False  # NOT USED

        if not doc:
            self.name = "Offensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.ichor_cost = doc["IchorCost"]
        self.scaling = doc["Scaling"]
