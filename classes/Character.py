class Character:
    def __init__(self, image, name="none", health=0, attack=0, defense=0, special_ability="none", level=1):
        self.image = image
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_ability = special_ability
        self.level = level

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        actual_damage = enemy.take_damage(damage)
        return actual_damage

    def use_ability(self):
        pass

    def take_damage(self, damage):
        # Ensure damage doesn't go below 0
        effective_damage = max(damage - self.defense, 0)
        self.health -= effective_damage
        return effective_damage

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
