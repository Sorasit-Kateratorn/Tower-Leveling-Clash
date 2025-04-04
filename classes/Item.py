class Item:  # item has 8 type

    def __init__(self, image, name, cost, ability):
        self.image = image
        self.name = name
        self.cost = cost
        self.ability = ability


class HealPotion(Item):
    def __init__(self):
        super().__init__("image/heal-potion.png", "Heal Potion", 10, "Restore 10 health")

    def apply_effect(self, player):
        player.health += 10
        if player.health > 100:
            player.health = 100
        return True


class StrengthPotion(Item):
    def __init__(self):
        super().__init__("image/strength-potion.png",
                         "Strength Potion", 20, "Increase attack by 5")

    def apply_effect(self, player):
        player.attack += 5


class IronSkinTonic(Item):
    def __init__(self):
        super().__init__("image/iron-skin.png", "Iron Skin Tonic", 20, "Increase defense by 5")

    def apply_effect(self, player):
        player.defense += 5


class CoinBoost(Item):
    def __init__(self):
        super().__init__("image/coin-boost.png", "Coin Boost",
                         40, "Gain more coins from floor clear")

    def apply_effect(self, player):
        player.coin += 30


class BerserkerTonic(Item):
    def __init__(self):
        super().__init__("image/berserker-tonic.png", "Berserker Tonic",
                         50, "Increase attack and defense by 15")

    def apply_effect(self, player):
        player.attack += 15
        player.defense += 15


class LuckyElixir(Item):
    def __init__(self):
        super().__init__("image/lucky.png", "Lucky Elixir",
                         60, "Increase critical hit chance by 10%")

    def apply_effect(self, player):
        player.critical_chance += 10


class VampireEssence(Item):
    def __init__(self):
        super().__init__("image/vampire.png", "Vampire Essence", 70,
                         "Attacks heal 50% of the damage dealt for that turns.")

    def apply_effect(self, player):
        player.vampire_mode = True


class Poison(Item):
    def __init__(self):
        super().__init__("image/poison.png", "Poison",
                         30, "Deal 10 damage to enemy for 3 turns")

    def apply_effect(self, player):
        player.apply_poison_turns = True
        player.apply_poison_turn = 3
