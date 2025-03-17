from classes.Player import *
from classes.Enemy import *
from classes.Save import *
from classes.Inventory import *
import random

# Define the number of floors in the game
FLOORS = 10


class GamePlay:
    def __init__(self):
        # Choose a hero
        self.player = self.choose_hero()
        self.inventory = Inventory()
        self.current_floor = 1

    def choose_hero(self):
        heroes = [Wonderwoman(), Wizard(), Omen(), Hulk(), Predator()]
        print("Choose your hero:")
        for i, hero in enumerate(heroes):
            print(f"{i+1}. {hero.name} - Ability: {hero.special_ability}")

        while True:
            choice = input("Enter the number of your hero: ")
            if choice.isdigit() and 1 <= int(choice) <= len(heroes):
                print(f"You chose {heroes[int(choice) - 1].name}!")
                return heroes[int(choice) - 1]
            print("Invalid choice. Please select a valid hero number.")

    def run_game_loop(self):
        while self.player.health > 0 and self.current_floor <= FLOORS:
            self.progress_to_next_floor()

        self.check_game_over()

    def progress_to_next_floor(self):
        print(f"\n--- Entering Floor {self.current_floor} ---")
        enemies = [random.choice(
            [Clayman(), Skull(), Dragon(), Stealer(), DarkKnight()]) for _ in range(3)]

        for enemy in enemies:
            print(f"\nA wild {enemy.name} appears with {enemy.health} HP!")
            while self.player.health > 0 and enemy.health > 0:
                print("Choose an action:")
                print("1. Attack")
                print("2. Use Special Ability")
                print("3. Use items")
                print("4. Discard items")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.player.attack_enemy(enemy)
                elif choice == "2":
                    self.player.use_ability(enemy)
                elif choice == "3":
                    self.use_item()

                # TODO discard item
                # Show Shop for buy items

                if enemy.health > 0:  # Enemy still alive, it attacks back
                    enemy.attack_enemy(self.player)
                    enemy.use_ability(self.player)

            if self.player.health <= 0:
                break

        if self.player.health > 0:
            print(
                f"\nFloor {self.current_floor} cleared! Health remaining: {self.player.health}")
            self.current_floor += 1

    def use_item(self):
        if not self.inventory.items:
            print("No items in inventory!")
            return

        print("\nChoose an item to use:")
        for i, item in enumerate(self.inventory.items):
            print(f"{i+1}. {item.name} - {item.ability}")

        choice = input("Enter the item number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.inventory.items):
            # Pass player to apply effect
            self.inventory.use_item(int(choice) - 1, self.player)

    def check_game_over(self):
        if self.player.health <= 0:
            print("\nGame Over!")
            # save_data([self.current_floor, "Lost")
        else:
            print("\nVictory! You cleared all floors!")
            # save_data(["Won")
