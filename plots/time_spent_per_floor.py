import matplotlib.pyplot as plt
import pandas as pd
import io
from PIL import Image
import pygame

class TimeSpentPerFloorChart:
    def __init__(self):
        self.img_surface = None

    def generate_graph(self):
        floor_df = pd.read_csv("data_record/floors.csv")
        floor_df["time_spent"] = floor_df["end_time"] - floor_df["start_time"]
        time_by_floor = floor_df.groupby("floor")["time_spent"].mean()

        fig, ax = plt.subplots()
        ax.plot(time_by_floor.index, time_by_floor.values, marker='o')
        ax.set_title("Time Spent per Floor")
        ax.set_xlabel("Floor Number")
        ax.set_ylabel("Time Spent (seconds)")
        ax.grid(True)
        
        ax.set_xticks(time_by_floor.index)
        ax.set_xticklabels([str(i) for i in time_by_floor.index])
        
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
