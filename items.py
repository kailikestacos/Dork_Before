class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not initialize raw weapon. Please specify.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "It's not a boulder! It's a rock!"
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A good start for any rogue."
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 20
        self.value = 100

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
