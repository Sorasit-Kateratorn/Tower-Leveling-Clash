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
        if len(self.items) > self.max_slot:
            print("Cant add more items")
            return
        self.items.append(item)

    def use_item(self, index):
        if index >= len(self.items) or index < 0:
            print("index out of range")
        # TODO: use item
        self.items.pop(index)

    def discard_item(self, index):

        if index >= len(self.items) or index < 0:
            print("index out of range")
        # TODO: discard and sale item
        self.items[index].cost
        self.items.pop(index)
