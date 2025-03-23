class Config:
    __ALL_CONFIGS = {
        'WIN_SIZE_W': 800,
        'WIN_SIZE_H': 600,
        'GRID_SIZE': 20,
        'GRID_COUNT_W': 40,
        'GRID_COUNT_H': 30,
        'BLACK': (0, 0, 0),
        'GREEN': (0, 255, 0),
        'RED': (255, 0, 0),
        'WHITE': (200, 255, 255),
        'DarkBrown': (189, 150, 25),
    }

    @classmethod
    def get(cls, key):
        return cls.__ALL_CONFIGS[key]
