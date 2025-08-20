class Engine:
    def __init__(self, hp: int, volume: int):
        self.hp = hp
        self.volume = volume


    def speedy(self):
        return self.hp > 100
