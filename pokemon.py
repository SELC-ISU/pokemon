class ElementalType:

    # defaults to normal if no type is specified
    def __init__(self, name="normal", attack_effective=[], attack_weakness=["rock", "steel", "ghost"], defense_ineffective=["ghost"],
     defense_weakness=["fighting"]):
        self.name = name
        self.attack_effective = attack_effective
        self.attack_weakness = attack_weakness
        self.defense_ineffective = defense_ineffective
        self.defense_weakness = defense_weakness

class Pokemon:

    def __init__(self, name: str, personal_name: str, elemental_type: ElementalType):
        self.name = name
        self.personal_name = personal_name
        self.elemental_type = elemental_type

    # equivalent to javas toString kind of 
    def __str__(self):
        return " POKEMON NAME: %s\n PERSONAL NAME: %s\n ELEMENTAL TYPE: %s\n" % (self.name, self.personal_name, self.elemental_type.name)
    


def main():
    electric = ElementalType(name="electric", attack_effective=["flying", "water"], attack_weakness=["dragon", "electric", "grass", "ground"], 
    defense_ineffective=["electric", "flying"], defense_weakness=["ground"])
    
    pika = Pokemon(name="pikachu", personal_name="pwn man", elemental_type=ElementalType())
    print(pika)

if __name__== "__main__":
    main()
