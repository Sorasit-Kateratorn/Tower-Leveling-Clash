import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import pygame

class ReachPercentChart:
    def __init__(self, floor_n=2):
        self.img_surface = None
        self.floor_n = floor_n

    def generate_graph(self):
        stats_df = pd.read_csv("data_record/game_stats.csv")

        # Count how many players of each character reached at least floor_n
        reach_stats = stats_df[stats_df['total_floors'] >= self.floor_n]
        total_by_char = stats_df.groupby("character")["play_id"].count()
        reached_by_char = reach_stats.groupby("character")["play_id"].count()
        percent_reached = ((reached_by_char / total_by_char) * 100).fillna(0)

        # Plot pie chart
        fig, ax = plt.subplots()
        colors = plt.cm.Set3.colors  # Use a predefined colormap
        ax.pie(percent_reached, labels=percent_reached.index, autopct='%1.1f%%', startangle=140, colors=colors[:len(percent_reached)])
        ax.set_title(f"Percent% of Characters Reaching Floor {self.floor_n + 1}")
        fig.tight_layout()

        # Convert to Pygame surface
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
