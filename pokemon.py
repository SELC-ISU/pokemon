from ElementalType import ElementalType

class Pokemon:

    def __init__(self, name: str, personal_name: str, elemental_type: ElementalType):
        self.name = name
        self.personal_name = personal_name
        self.elemental_type = elemental_type

    # equivalent to javas toString kind of
    def __str__(self):
        return " POKEMON NAME: %s\n PERSONAL NAME: %s\n ELEMENTAL TYPE: %s\n" % (self.name, self.personal_name, self.elemental_type.name)



def main():
    #Instantiate an electric type
    electric = ElementalType(name="electric", attack_effective=["flying", "water"], attack_weakness=["dragon", "electric", "grass", "ground"],
    defense_ineffective=["electric", "flying"], defense_weakness=["ground"])

    # Instantiate a fire type
    fire = ElementalType(name="fire", attack_effective=["bug","grass"],
    defense_ineffective=["fire, water"], defense_weakness=["ground", "water"])

    pika = Pokemon(name="pikachu", personal_name="pwn man", elemental_type=electric)
    vulpix = Pokemon(name="vulpix", personal_name="ya boi", elemental_type=fire)

    print(pika)
    print(vulpix)

if __name__== "__main__":
    main()
