class Weapon:
    name = "Weapon"
    type = 0  # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    bleed_factor = 0

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
    # One-Handed Swords, Two-Handed Swords, Twin Blades, Bayonets, Halberds, Hammers, Rune Blades
    # Magic Range Long, Magic Range Short, Assistance Attack, Assistance Defense, Assistance Other
    type = 0
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
    type = 0  # 0, 1, 2, 3
    conditions = []

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
    bloodline = ""
    bleed_factor = 0
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

    burden = {
        "Strength":     0,
        "Dexterity":    0,
        "Mind":         0,
        "Willpower":    0,
        "Vitality":     0,
        "Fortitude":    0,
    }

    defense = {
        "Slash":        0,
        "Crush":        0,
        "Pierce":       0,
        "Fire":         0,
        "Ice":          0,
        "Lightning":    0,
        "Blood":        0,
    }

    resistances = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }


class Jail:
    name = "Jail"
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
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Fire": 		0,
        "Ice": 			0,
        "Lightning": 	0,
        "Blood":	 	0,
    }


class DefensiveForma:
    name = "Defensive"
    balance = 0
    guard = 0

    burden = {
        "Strength": 0,
        "Dexterity": 0,
        "Mind": 0,
        "Willpower": 0,
        "Vitality": 0,
        "Fortitude": 0,
    }

    defense = {
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Fire": 		0,
        "Ice": 			0,
        "Lightning": 	0,
        "Blood":	 	0,
    }

    guarding_defense = {
        "Slash": 		0,
        "Crush": 		0,
        "Pierce": 		0,
        "Fire": 		0,
        "Ice": 			0,
        "Lightning": 	0,
        "Blood":	 	0,
    }

    resistances = {
        "Disease":  0,
        "Wound":    0,
        "Bleed":    0,
        "Curse":    0,
    }


class OffensiveForma:
    name = "Offensive"
