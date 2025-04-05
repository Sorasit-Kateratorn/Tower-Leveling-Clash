import random
class Character:
    def __init__(self, image, name="none", health=0, attack=0, defense=0, special_ability="none", level=1):
        self.image = image
        self.name = name
        self.health = health
        self.base_health = health
        self.attack = attack
        self.base_attack = attack
        self.defense = defense
        self.base_defense = defense
        self.special_ability = special_ability
        self.level = level
        
        
        # attibute for support items
        self.critical_chance = 0
        self.vampire_mode = False
        self.poison_enemy = False
        self.poisoned = False
        self.poison_turns = 0
        self.extra_coin_boost = 0
        

    def attack_enemy(self, enemy):
        is_crit = random.randint(1,100) <= self.critical_chance
        damage = self.attack * 2 if is_crit else self.attack
        actual_damage = enemy.take_damage(damage)
        
        if self.vampire_mode:
            healed = int(actual_damage *0.5)
            self.health += healed
            self.vampire_mode = False
        
        if self.poison_enemy:
            enemy.poisoned = True
            enemy.poison_turns = 3
            self.poison_enemy = False
            

        return actual_damage

    def apply_poison_damage(self):
        if self.poisoned and self.poison_turns > 0 :
            self.health -= 10
            self.poison_turns -= 1
            
            if self.poison_turns == 0:
                self.poisoned = False
                


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
        self.health = self.base_health + (self.level - 1) * 10
        self.attack = self.base_attack + (self.level - 1) * 5
        self.defense = self.base_defense + (self.level - 1) * 5

    def scale_to_level(self, level):
        self.level = level
        self.health += (level - 1) * 10
        self.attack += (level - 1) * 3
        self.defense += (level - 1) * 2