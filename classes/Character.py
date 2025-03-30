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
        damage = self.attack
        actual_damage = enemy.take_damage(damage)
        return actual_damage

    def use_ability(self):
        pass

    def take_damage(self, damage):

        # Absorb damage with defense
        damage_to_defense = min(self.defense, damage)
        self.defense -= damage_to_defense
        self.defense = max(self.defense, 0)  # Prevent negative defense

        # Apply leftover damage to health
        remaining_damage = damage - damage_to_defense
        self.health -= remaining_damage
        self.health = max(self.health, 0)  # Prevent negative health

        return damage_to_defense + remaining_damage

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
