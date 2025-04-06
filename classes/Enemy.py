from classes.Character import Character

# skill คูณพลังโจมตีม


class Clayman(Character):
    def __init__(self):
        super().__init__("image/Clayman.png", "Clayman", 75, 12, 1, "Berserk Rage")



class Skull(Character):
    def __init__(self):
        super().__init__("image/Skull.png", "Skull", 60, 13, 1, "Bone Throw")



class Dragon(Character):
    def __init__(self):
        super().__init__("image/Dragon.png", "Dragon", 100, 16, 3, "Flame Breath")



class Stealer(Character):
    def __init__(self):
        super().__init__("image/Stealer.png", "Stealer", 55, 10, 2, "Sneaky Stab")


class DarkKnight(Character):
    def __init__(self):
        super().__init__("image/DarkKnight.png", "Dark Knight", 90, 14, 2, "Dark Slash")

