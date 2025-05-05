import matplotlib.pyplot as plt
import pandas as pd
import io
from PIL import Image
import pygame

class EarnPerFloorChart:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        earn_df = pd.read_csv("data_record/earn.csv")
        earn_by_floor = earn_df.groupby("floor")["coin_earned"].sum()

        fig, ax = plt.subplots()
        ax.bar(earn_by_floor.index, earn_by_floor.values, color='orange')
        ax.set_title("Coins Earned per Floor")
        ax.set_xlabel("Floor Number")
        ax.set_ylabel("Coins Earned")
        ax.set_xticks(earn_by_floor.index-1) 
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
