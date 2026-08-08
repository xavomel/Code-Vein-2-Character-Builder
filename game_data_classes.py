class Weapon:
    name = "Weapon"
    description = ""
    type = "" # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    bleed = 0
    scaling = "TODO"
    transformable = False
    transforms = {}

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

    def __init__(self, number):
        self.name += " " + str(number)


class Forma:
    name = "Forma"
    description = ""
    # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    # Magic Range Long, Magic Range Short, Assistance Attack, Assistance Defense, Assistance Other
    type = ""
    ichor_cost = 0

    capacity = {
        "Reliability": 		0,
        "Handling": 		0,
        "Conversion": 		0,
        "Conductivity": 	0,
    }

    def __init__(self, number):
        self.name += " " + str(number)


class Booster:
    name = "Booster"
    description = ""
    type = ""  # 0, 1, 2, 3
    conditions = []

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

    def __init__(self, number):
        self.name += " " + str(number)


class BloodCode:
    name = "Blood Code"
    description = ""
    bloodline = ""
    bleed = 0
    ichor = 0
    balance = 0
    traits = []

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

    resistances = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }


class Jail:
    name = "Jail"
    description = ""
    type = ""
    balance = 0

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


class DefensiveForma:
    name = "Defensive"
    description = ""
    type = ""
    ichor_cost = 0
    stamina_guard_cost = 0
    balance = 0
    transformable = False
    transforms = {}

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

    resistances = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }


class OffensiveForma:
    name = "Offensive"
    description = ""
    ichor_cost = 0
    scaling = {}
