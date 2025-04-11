import time
import csv
import os

class GameStats:
    def __init__(self):
        self.total_floors = 0
        self.total_damage_dealt = 0
        self.total_wins = 0
        self.total_earned = 0
        self.total_spent = 0
        self.start_time = None
        self.total_time = 0
        self.character = None
        self.play_id = None  
        
        
        
        self.floor_logs = []       # (play_id, floor, start_time, end_time, kill_count)
        self.damage_logs = []      # (play_id, floor, damage)
        self.earn_logs = []        # (play_id, floor, coin_earned)
        self.spend_logs = []       # (play_id, item_name, floor, coin_spent)
        
    def set_character_name(self, name):
        self.character = name
        
    def set_play_id(self, pid):
        self.play_id = pid

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
        
        
    def record_floor_log(self, floor, start_time, end_time, kill_count):
        self.floor_logs.append((self.play_id, floor, start_time, end_time, kill_count))

    def record_damage_log(self, floor, damage):
        self.damage_logs.append((self.play_id, floor, damage))

    def record_earn_log(self, floor, coins):
        self.earn_logs.append((self.play_id, floor, coins))

    def record_spend_log(self, floor, item_name, coins):
        self.spend_logs.append((self.play_id, item_name, floor, coins))   
    

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

    def to_csv(self, filename="data_record/game_stats.csv"):
        os.makedirs("data_record", exist_ok=True)
        headers = [
            "play_id", "character", "total_floors", "total_damage_dealt",
            "total_wins", "total_earned", "total_spent", "total_time_sec"
        ]
        row = [
            self.play_id,
            self.character,
            self.total_floors,
            self.total_damage_dealt,
            self.total_wins,
            self.total_earned,
            self.total_spent,
            round(self.total_time, 2)
        ]

        try:
            with open(filename, "a", newline="") as f:
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(headers)
                writer.writerow(row)
        except Exception as e:
            print("Error writing to game_stats.csv:", e)

    
    def save_logs(self):
        self._save_csv("floors.csv", self.floor_logs,
                       ["play_id", "floor", "start_time", "end_time", "kill_count"])
        self._save_csv("damage.csv", self.damage_logs,
                       ["play_id", "floor", "damage"])
        self._save_csv("earn.csv", self.earn_logs,
                       ["play_id", "floor", "coin_earned"])
        self._save_csv("spend.csv", self.spend_logs,
                       ["play_id", "item_bought", "floor", "coin_spent"])

    def _save_csv(self, filename, rows, headers):
        os.makedirs("data_record", exist_ok=True)
        full_path = os.path.join("data_record", filename)
        try:
            with open(full_path, "a", newline="") as f:
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(headers)
                writer.writerows(rows)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")


