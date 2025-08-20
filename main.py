from models.Car import Car
from models.Engine import Engine

def main():
    focus = Car("focus", "ford", Engine(200, 4000))
    cross_golf = Car("golf", "FolkeVogn", Engine(2, 100))

    if focus.fast():
        print("Fast as fuck boy")

    if not cross_golf.fast():
        print("Not so fast boy")
    print("mordi")


if __name__ == "__main__":
    main()
