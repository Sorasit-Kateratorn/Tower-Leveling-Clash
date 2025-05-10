from classes.Character import Character


class Wonderwoman(Character):
    def __init__(self):
        super().__init__("image/Wonderwoman.png", "Wonderwoman", 130, 20, 8, "Power Strike")

    def use_ability(self, enemies):
        for enemy in enemies:
            enemy.take_damage(self.attack * 2)  # Double damage
        return f"{self.name} uses Power Strike on all enemies!"


class Wizard(Character):
    def __init__(self):
        super().__init__("image/Wizard.png", "Wizard", 110, 25, 4, "Fireball")

    def use_ability(self, enemies):
        for enemy in enemies:
            enemy.take_damage(25)  # Fixed high damage
        return f"{self.name} casts Fireball and burns all enemies for 25 damage!"       


class Omen(Character):
    def __init__(self):
        super().__init__("image/Omen.png", "Omen", 120, 19, 6, "Shadow Strike")

    def use_ability(self, enemies):
        
        for enemy in enemies:
            enemy.take_damage(20)
        self.defense += 5  # Temporary dodge
        return f"{self.name} strikes shadows and gains 5 defense!"


class Hulk(Character):
    def __init__(self):
        super().__init__("image/Hulk.png", "Hulk", 150, 16, 12, "Healing Factor")

    def use_ability(self, enemies):
        self.health += 20
        if self.health > self.base_health + (self.level - 1) * 10:
            self.health = self.base_health + (self.level - 1) * 10  # cap to max
        for enemy in enemies:
            enemy.take_damage(10)
        return f"{self.name} regenerates 20 HP and slams all enemies for 10 damage!"


class Predator(Character):
    def __init__(self):
        super().__init__("image/Predator.png", "Predator", 125, 22, 7, "Piercing Shot")

    def use_ability(self, enemies):
        for enemy in enemies:
            enemy.health -= self.attack  # Ignores defense
            enemy.health = max(0, enemy.health)
        return f"{self.name} fires piercing shots ignoring all defenses!"
