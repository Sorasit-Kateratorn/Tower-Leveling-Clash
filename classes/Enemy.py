from classes.Character import Character


class Clayman(Character):
    def __init__(self):
        super().__init__("image/Clayman.png", "Clayman", 90, 12, 8, "Berserk Rage")

    def use_ability(self, player):
        print(f"{self.name} enters Berserk Rage, increasing attack!")
        self.attack += 5
        player.take_damage(self.attack)


class Skull(Character):
    def __init__(self):
        super().__init__("image/Skull.png", "Skull", 70, 14, 5, "Bone Throw")

    def use_ability(self, player):
        print(f"{self.name} throws a bone and weakens the player!")
        player.take_damage(15)
        player.attack -= 2  # Weakens player's attack


class Dragon(Character):
    def __init__(self):
        super().__init__("image/Dragon.png", "Dragon", 150, 20, 15, "Flame Breath")

    def use_ability(self, player):
        print(f"{self.name} breathes fire, dealing massive damage!")
        player.take_damage(30)


class Stealer(Character):
    def __init__(self):
        super().__init__("image/Stealer.png", "Stealer", 60, 10, 3, "Sneaky Stab")

    def use_ability(self, player):
        print(f"{self.name} stabs the player and steals coins!")
        player.take_damage(12)


class DarkKnight(Character):
    def __init__(self):
        super().__init__("image/DarkKnight.png", "Dark Knight", 110, 16, 12, "Dark Slash")

    def use_ability(self, player):
        print(f"{self.name} performs a Dark Slash that reduces defense!")
        player.take_damage(18)
        player.defense -= 3  # Reduces player's defense
