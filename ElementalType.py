class ElementalType:

    # defaults to normal if no type is specified
    def __init__(self, name="normal", attack_effective=[], attack_weakness=["rock", "steel", "ghost"], defense_ineffective=["ghost"],
     defense_weakness=["fighting"]):
        self.name = name
        self.attack_effective = attack_effective
        self.attack_weakness = attack_weakness
        self.defense_ineffective = defense_ineffective
        self.defense_weakness = defense_weakness
