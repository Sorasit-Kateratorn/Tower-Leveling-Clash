import matplotlib.pyplot as plt
import pandas as pd
import io
from PIL import Image
import pygame

class SpendDistributionChart:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        spend_df = pd.read_csv("data_record/spend.csv")
        spend_by_item = spend_df.groupby("item_bought")["coin_spent"].sum()

        fig, ax = plt.subplots()
        ax.bar(spend_by_item.index, spend_by_item.values, color='green')
        ax.set_title("Item Spending Distribution")
        ax.set_xlabel("Item Name")
        ax.set_ylabel("Coins Spent")
        ax.tick_params(axis='x', rotation=45)
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