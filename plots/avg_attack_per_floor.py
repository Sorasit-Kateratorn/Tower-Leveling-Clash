import matplotlib.pyplot as plt
import pandas as pd
import io
from PIL import Image
import pygame

class AvgAttackPerFloorChart:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        damage_df = pd.read_csv("data_record/damage.csv")
        avg_damage_by_floor = damage_df.groupby("floor")["damage"].mean()

        fig, ax = plt.subplots()
        ax.plot(avg_damage_by_floor.index, avg_damage_by_floor.values, marker='o')
        ax.set_title("Avg Attack Points per Floor")
        ax.set_xlabel("Floor Number")
        ax.set_ylabel("Avg Attack Points")
        ax.grid(True)
        fig.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        image = Image.open(buf)
        mode = image.mode
        size = image.size
        data = image.tobytes()
        self.img_surface = pygame.image.fromstring(data, size, mode)

    def get_graph_surface(self):
        if not self.img_surface:
            self.generate_graph()
        return self.img_surface
