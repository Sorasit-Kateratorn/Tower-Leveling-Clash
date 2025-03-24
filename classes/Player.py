from classes.Character import Character


class Wonderwoman(Character):
    def __init__(self):
        super().__init__("image/Wonderwoman.png", "Wonderwoman", 100, 15, 10, "Power Strike")

    def use_ability(self, enemy):
        print(f"{self.name} performs a powerful strike!")
        enemy.take_damage(self.attack * 2)  # Double damage


class Wizard(Character):
    def __init__(self):
        super().__init__("image/Wizard.png", "Wizard", 80, 20, 5, "Fireball")

    def use_ability(self, enemy):
        print(f"{self.name} casts Fireball!")
        enemy.take_damage(25)  # Fixed high damage


class Omen(Character):
    def __init__(self):
        super().__init__("image/Omen.png", "Omen", 90, 18, 0, "Shadow Strike")

    def use_ability(self, enemy):
        print(f"{self.name} uses Shadow Strike and evades the next attack!")
        enemy.take_damage(20)
        self.defense += 5  # Temporary dodge


class Hulk(Character):
    def __init__(self):
        super().__init__("image/Hulk.png", "Hulk", 120, 12, 1, "Healing Factor")

    def use_ability(self, enemy):
        print(f"{self.name} activates Healing Factor!")
        self.health += 20
        enemy.take_damage(10)


class Predator(Character):
    def __init__(self):
        super().__init__("image/Predator.png", "Predator", 85, 17, 7, "Piercing Shot")

    def use_ability(self, enemy):
        print(f"{self.name} fires a Piercing Shot, ignoring enemy defense!")
        enemy.take_damage(self.attack)
