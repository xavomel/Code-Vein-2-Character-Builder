from fractions import Fraction


def attribute_or_burden_table(type, data):
    attr_short = [
        "STR",
        "DEX",
        "MND",
        "WIL",
        "VIT",
        "FOR",
    ]
    header = ""
    row = ""

    for idx, (k, v) in enumerate(data.items()):
        if v != 0:
            header += '<th>%s</th>' % attr_short[idx]
            row += '<td style="text-align: center;">%s</td>' % v

    if header:
        text = """
            <table align="center" width="100%">
            <caption><h3>{0}</h3></caption>
            <thead><tr>{1}</tr></thead>
            <tbody><tr>{2}</tr></tbody>
            </table>
                """.format(type, header, row)
    else:
        text = ""

    return text


def capacity_table(capacity):
    header = ""
    row = ""

    for k, v in capacity.items():
        if v != 0:
            header += '<th>%s</th>' % k
            row += '<td style="text-align: center;">%s</td>' % v

    if header:
        text = """
            <p></p>
            <table align="center" width="100%">
            <thead><tr>{0}</tr></thead>
            <tbody><tr>{1}</tr></tbody>
            </table>
                """.format(header, row)
    else:
        text = ""

    return text


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

    def get_hover_text(self, detailed=True):
        text = """<body><h2><p align="center">{0}</p></h2>""".format(self.name)

        # to do choose right transform
        if detailed:
            text += capacity_table(self.transforms["Weapon_Off"]["Capacity"])
            text += attribute_or_burden_table("Burden", self.transforms["Weapon_Off"]["Burden"])
        text += """<br><div style="white-space: pre-wrap;">{0}</div>""".format(self.description)
        text += "</body>"

        return text


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

    # to do add matching weapons?
    def get_hover_text(self, detailed=True):
        text = """<body><h2><p align="center">{0}</p></h2>""".format(self.name)

        if detailed:
            text += capacity_table(self.capacity)
        text += """<h3>Ichor Consumption: {0}</h3>""".format(self.ichor_cost)
        text += """<br><div style="white-space: pre-wrap;">{0}</div>""".format(self.description)
        text += "</body>"

        return text

class Booster:
    def __init__(self, doc=None, dummy_number=None):
        self.name = ""
        self.description = ""
        self.type = ""  # 0, 1, 2, 3
        self.conditions = [{}]
        self.conditions_print = ""
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
        self.conditions_print = self.print_conditions()

    # to do add conditions
    def get_hover_text(self, detailed=True):
        text = """<body><h2><p align="center">{0}</p></h2>""".format(self.name)
        if detailed:
            text += attribute_or_burden_table("Burden", self.burden)
        text += self.conditions_print
        text += """<div style="white-space: pre-wrap;">{0}</div>""".format(self.description)
        text += "</body>"

        return text

    def print_conditions(self):
        text = ""

        for conditions in self.conditions:
            for name, values in conditions.items():
                if name == "Overburden":
                    if values:
                        text += "Any Overburden Effect"
                    else:
                        text += "No Overburden Effect"
                elif name == "Attribute":
                    for k, v in values.items():
                        text += "%s %s " % (k, v)
                elif name in ["Burden", "Margin"]:
                    text += "\n%s: " % name
                    for k, v in values.items():
                        text += "%s %s " % (k, v)
                elif name == "Bloodline":
                    text += "\n%s: %s" % (name, values)
        if not text:
            text = "No Conditions"

        return """<br><div style="white-space: pre-wrap;"><h3>{0}</h3></div>""".format(text)

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
        self.has_burden = False

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
        self.attributes = doc["Attributes"]
        self.defense = {k: Fraction(v) for k, v in doc["Defense"].items()}
        self.resistance = doc["Resistance"]
        self.traits = doc["Traits"]

        for trait in self.traits:
            burden = trait.get("Burden")
            if burden and not trait["Conditions"]:
                self.has_burden = True
                for attribute, value in burden.items():
                    self.burden[attribute] += value

        # print("\n\n", self.name)
        # for k, v in self.burden.items():
        #     print(k, v)

    # to do add traits
    def get_hover_text(self, detailed=True):
        text = """<body>
            <h2><p align="center">{0}</p></h2>""".format(self.name)

        if detailed:
            text += attribute_or_burden_table("Attributes", self.attributes)
        if self.has_burden:
            text += attribute_or_burden_table("Burden", self.burden)
        if detailed:
            text += """<h3>Bloodline: {0}</h3>""".format(self.bloodline)
        text += """<br><div style="white-space: pre-wrap;">{0}</div>""".format(self.description)
        text += "</body>"

        return text


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

    def get_hover_text(self, detailed=True):
        text = """<body><h2><p align="center">{0}</p></h2>""".format(self.name)
        if detailed:
            text += attribute_or_burden_table("Burden", self.burden)
        text += """<br><div style="white-space: pre-wrap;">{0}</div>""".format(self.description)
        text += "</body>"

        return text


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

    # to do choose right transform
    def get_hover_text(self, detailed=True):
        text = """<body><h2><p align="center">{0}</p></h2>""".format(self.name)

        if detailed:
            text += attribute_or_burden_table("Burden", self.transforms["Defensive_Off"]["Burden"])
        text += """
            <h3>Type: {0}</h3>
            <h3>Ichor Consumption: {1}</h3>
            <br><div style="white-space: pre-wrap;">{2}</div>
            </body>""".format(self.type, self.ichor_cost, self.description)
        text += ""

        return text


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

    def get_hover_text(self, detailed=True):
        return """<body>
            <h2><p align="center">{0}</p></h2>
            <h3>Ichor Consumption: {1}</h3>
            <br><div style="white-space: pre-wrap;">{2}</div>
            </body>""".format(
                self.name,
                self.ichor_cost,
                self.description)
