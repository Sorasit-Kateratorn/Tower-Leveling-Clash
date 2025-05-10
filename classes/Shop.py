from classes.Item import *
from classes.Inventory import Inventory
from classes.GameStats import GameStats
import random


class Shop:  # store item in shop for buy and generate new one to complete 5 items set in shop always
    def __init__(self):
        self.available_items = [HealPotion(), StrengthPotion(), IronSkinTonic(
        ), CoinBoost(), BerserkerTonic(), LuckyElixir(), VampireEssence()]
        self.items_in_shop = random.sample(
            self.available_items, 5)  # Store 5 items in the shop

    def reroll(self):
        self.items_in_shop = random.sample(self.available_items, 5)

    def check_money(self, player_money, item):
        return player_money >= item.cost

    def buy_item(self, inventory, index, stats: GameStats=None, floor=None):
        if index < 0 or index >= len(self.items_in_shop):
            return False
        item = self.items_in_shop[index]
        if inventory.coin >= item.cost:
            inventory.coin -= item.cost
            inventory.add_item(item)
            
            if stats:
                stats.record_spent(item.cost)
                stats.record_spend_log(floor, item.name, item.cost)
            
            self.items_in_shop[index] = random.choice(self.available_items)  # Generate a new item
            return True
        else:
            return False

