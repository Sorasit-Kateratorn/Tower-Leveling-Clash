from classes.Item import *
from classes.Inventory import Inventory
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

    def buy_item(self, inventory, index):
        if index < 0 or index >= len(self.items_in_shop):
            print("Invalid item selection")
            return
        item = self.items_in_shop[index]
        if inventory.coin >= item.cost:
            inventory.coin -= item.cost
            inventory.add_item(item)
            print(f"Bought {item.name} for {item.cost} coins")
            self.items_in_shop[index] = random.choice(
                self.available_items)  # Generate a new item
        else:
            print("Not enough coins")


# check the shop
if __name__ == "__main__":
    inventory = Inventory()
    shop = Shop()

    print("Items available in the shop:")
    for i, item in enumerate(shop.items_in_shop):
        print(f"{i+1}. {item.name} - {item.cost} coins")

    inventory.add_coin(50)
    shop.buy_item(inventory, 0)  # Buy first item in the shop
