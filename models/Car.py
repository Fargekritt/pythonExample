from models import Engine
class Car:
    def __init__(self, name: str, brand: str, engine: Engine):
        self.name = name
        self.brand = brand
        self.engine = engine


    def fast(self) -> bool:
        if self.engine.speedy():
            return True
        if self.brand == "ford":
            return True
        else:
            return False
