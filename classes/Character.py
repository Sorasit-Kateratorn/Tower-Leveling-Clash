class Character:
    def __init__(self, image, name, health, attack, defense, special_ability):
        self.image = image
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_ability = special_ability

    def attack_enemy(self):
        pass

    def use_ability(self):
        pass

    def take_damage(self):
        pass
