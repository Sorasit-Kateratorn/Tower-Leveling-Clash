import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import pygame

class FloorStatsTable:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        floors_df = pd.read_csv("data_record/floors.csv")
        stats_df = pd.read_csv("data_record/game_stats.csv")

        # Calculate total kills per game
        kills_per_game = floors_df.groupby("play_id")["kill_count"].sum().reset_index(name="total_kills")

        # Merge with game stats to get character info
        merged_df = pd.merge(stats_df, kills_per_game, on="play_id")

        # Group by character
        summary = merged_df.groupby("character").agg(
            average_kills=pd.NamedAgg(column="total_kills", aggfunc="mean"),
            max_floor_clear=pd.NamedAgg(column="total_floors", aggfunc="max"),
            average_floor=pd.NamedAgg(column="total_floors", aggfunc="mean"),
            total_games=pd.NamedAgg(column="play_id", aggfunc="count")
        ).reset_index()

        summary = summary.round(1)

        # Plot as table
        fig, ax = plt.subplots(figsize=(7, 2 + len(summary) * 0.3))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(
            cellText=summary.values,
            colLabels=summary.columns,
            loc='center',
            cellLoc='center'
        )
        table.scale(1, 1.5)
        table.auto_set_font_size(False)
        table.set_fontsize(10)
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
