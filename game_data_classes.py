class Weapon:
    name = ""
    description = ""
    type = "" # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    bleed = 0
    scaling = "TODO"
    transformable = False
    transforms = {}
    favorite = False

    capacity = {
        "Reliability": 		0,
        "Handling": 		0,
        "Conversion": 		0,
        "Conductivity": 	0,
    }

    burden = {
        "Strength": 	0,
        "Dexterity": 	0,
        "Mind": 		0,
        "Willpower": 	0,
        "Vitality": 	0,
        "Fortitude": 	0,
    }

    def __init__(self, doc=None, dummy_number=None):
        if not doc:
            self.name += "Weapon " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.bleed = doc["Bleed"]
        # self.scaling = "TODO"
        self.transformable = doc["Transformable"]
        self.transforms = {k: v for k, v in doc.items() if k.startswith("Transform_")}
        self.capacity = doc["Capacity"]
        self.burden = doc["Burden"]


class Transform:
    name = ""
    description = ""
    type = ""
    weapon_key = ""

    def __init__(self, doc=None):
        if not doc:
            self.name = "Transform"
            return

        self.name = doc["Name"]
        self.description = doc.get("Description", "")
        self.type = doc["Type"]
        self.weapon_key = doc["WeaponKey"]


class Forma:
    name = ""
    description = ""
    # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    # Magic Range Long, Magic Range Short, Assistance Attack, Assistance Defense, Assistance Other
    type = ""
    ichor_cost = 0
    favorite = False

    capacity = {
        "Reliability": 		0,
        "Handling": 		0,
        "Conversion": 		0,
        "Conductivity": 	0,
    }

    matching_weapons = {
        "SingleSword": True,
        "GreatSword": True,
        "DualSword": True,
        "Bayonet": True,
        "Halberd": True,
        "Hammer": True,
        "RuneBlade": True,
    }

    def __init__(self, doc=None, dummy_number=None):
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
    name = ""
    description = ""
    type = ""  # 0, 1, 2, 3
    conditions = []
    favorite = False

    # for positive effects
    attributes = {
        "Strength": 	0,
        "Dexterity": 	0,
        "Mind": 		0,
        "Willpower": 	0,
        "Vitality": 	0,
        "Fortitude": 	0,
    }

    burden = {
        "Strength": 	0,
        "Dexterity": 	0,
        "Mind": 		0,
        "Willpower": 	0,
        "Vitality": 	0,
        "Fortitude": 	0,
    }

    def __init__(self, doc=None, dummy_number=None):
        if not doc:
            self.name = "Booster " + str(dummy_number)
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        # self.conditions = doc[""]
        # self.attributes = doc["Attributes"]
        self.burden = doc["Burden"]


class BloodCode:
    name = ""
    description = ""
    bloodline = ""
    bleed = 0
    ichor = 0
    balance = 0
    traits = []
    favorite = False

    attributes = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    # for negative effects
    burden = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    defense = {
        "Slash": 		0.0,
        "Crush": 		0.0,
        "Pierce": 		0.0,
        "Blood":		0.0,
        "Fire": 		0.0,
        "Ice": 			0.0,
        "Lightning": 	0.0,
    }

    resistance = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }

    def __init__(self, doc=None):
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


class Jail:
    name = ""
    description = ""
    type = ""
    balance = 0
    # favorite = False  # NOT USED

    burden = {
        "Strength": 	0,
        "Dexterity": 	0,
        "Mind": 		0,
        "Willpower": 	0,
        "Vitality": 	0,
        "Fortitude": 	0,
    }

    defense = {
        "Slash": 		0.0,
        "Crush": 		0.0,
        "Pierce": 		0.0,
        "Blood":		0.0,
        "Fire": 		0.0,
        "Ice": 			0.0,
        "Lightning": 	0.0,
    }

    def __init__(self, doc=None):
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
    name = ""
    description = ""
    type = ""
    ichor_cost = 0
    stamina_guard_cost = 0
    balance = 0
    transformable = False
    transforms = {}
    favorite = False

    burden = {
        "Strength": 	0,
        "Dexterity": 	0,
        "Mind": 		0,
        "Willpower": 	0,
        "Vitality": 	0,
        "Fortitude": 	0,
    }

    defense = {
        "Slash": 		0.0,
        "Crush": 		0.0,
        "Pierce": 		0.0,
        "Blood":		0.0,
        "Fire": 		0.0,
        "Ice": 			0.0,
        "Lightning": 	0.0,
    }

    guarding_defense = {
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Blood":		0,
        "Fire": 		0,
        "Ice": 			0,
        "Lightning": 	0,
    }

    resistance = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }

    def __init__(self, doc=None):
        if not doc:
            self.name = "Defensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.type = doc["Type"]
        self.ichor_cost = doc["IchorCost"]
        self.stamina_guard_cost = doc["StaminaGuardCost"]
        self.balance = doc["Balance"]
        self.transformable = False
        self.transforms = {k: v for k, v in doc.items() if k.startswith("Transform_")}
        self.burden = doc["Burden"]
        self.defense = doc["Defense"]
        self.guarding_defense = doc["GuardingDefense"]
        self.resistance = doc["Resistance"]


class OffensiveForma:
    name = ""
    description = ""
    ichor_cost = 0
    scaling = {}
    # favorite = False  # NOT USED

    def __init__(self, doc=None):
        if not doc:
            self.name = "Offensive"
            return

        self.name = doc["Name"]
        self.description = doc["Description"]
        self.ichor_cost = doc["IchorCost"]
        self.scaling = doc["Scaling"]


def escape_filename(filename):
    # replace : with 2 underscores
    # replace " " with 1 underscore
    return filename.replace(":", "__").replace(" ", "_")


def unescape_filename(filename):
    # replace 2 underscores with :
    # replace underscore with " "
    return filename.replace("__", ":").replace("_", " ")
