import time
import csv


class GameStats:
    def __init__(self):
        self.total_floors = 0
        self.total_damage_dealt = 0
        self.total_wins = 0
        self.total_earned = 0
        self.total_spent = 0
        self.start_time = None
        self.total_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        if self.start_time:
            self.total_time += time.time() - self.start_time
            self.start_time = None

    def record_floor_clear(self):
        self.total_floors += 1

    def record_damage(self, dmg):
        self.total_damage_dealt += dmg

    def record_win(self):
        self.total_wins += 1

    def record_earned(self, coins):
        self.total_earned += coins

    def record_spent(self, coins):
        self.total_spent += coins

    def reset(self):
        self.__init__()

    def get_summary(self):
        return {
            "floors": self.total_floors,
            "damage": self.total_damage_dealt,
            "wins": self.total_wins,
            "earned": self.total_earned,
            "spent": self.total_spent,
            "time_sec": round(self.total_time, 2)
        }

    def to_csv(self):
        return [
            self.total_floors,
            self.total_damage_dealt,
            self.total_wins,
            self.total_earned,
            self.total_spent,
            round(self.total_time, 2)
        ]
