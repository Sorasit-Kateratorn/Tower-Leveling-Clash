import matplotlib.pyplot as plt
import pandas as pd
import io
from PIL import Image
import pygame

class KillChart:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        floor_df = pd.read_csv("data_record/floors.csv")
        stats_df = pd.read_csv("data_record/game_stats.csv")
        avg_kills = floor_df.groupby("play_id")["kill_count"].mean().reset_index()
        merged = pd.merge(avg_kills, stats_df[["play_id", "character"]], on="play_id")
        avg_kills_by_char = merged.groupby("character")["kill_count"].mean()

        
        fig, ax = plt.subplots()
        ax.bar(avg_kills_by_char.index, avg_kills_by_char.values, color='skyblue')
        ax.set_title("Avg Kill Count per Character")
        ax.set_xlabel("Character Name")
        ax.set_ylabel("Avg Kills")
        fig.tight_layout()

        # Save graph to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Convert to Pygame surface
        image = Image.open(buf)
        mode = image.mode
        size = image.size
        data = image.tobytes()
        self.img_surface = pygame.image.fromstring(data, size, mode)

    def get_graph_surface(self):
        if not self.img_surface:
            self.generate_graph()
        return self.img_surface
