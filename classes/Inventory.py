class Inventory:  # store item  for user
    def __init__(self):
        self.coin = 0
        self.items = []  # list of item
        self.max_slot = 10

    def add_coin(self, coin):
        if coin < 0:
            print("coin cant be negative")
            return
        self.coin += coin

    def add_item(self, item):
        if len(self.items) >= self.max_slot:
            print("Cant add more items")
            return
        self.items.append(item)

    def use_item(self, index, player):
        if index >= len(self.items) or index < 0:
            print("index out of range")
        # use item
        item = self.items.pop(index)
        item.apply_effect(player)  # Apply effect to the player
        # print(f"{player.name} used {item.name}.")
        return True

    def discard_item(self, index):

        if index >= len(self.items) or index < 0:
            print("index out of range")
        # discard and sale item for half price
        self.coin += self.items[index].cost // 2
        self.items.pop(index)
        return True
        
    def remove_item(self, item):
        
        if item in self.items:
            self.items.remove(item)
