class Car:
    def __init__(self, name: str, brand: str):
        self.name = name
        self.brand = brand


    def fast(self) -> bool:
        if self.brand == "ford":
            return True
        else:
            return False
