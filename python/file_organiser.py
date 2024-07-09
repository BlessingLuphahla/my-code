from pathlib import Path



class Organiser:
    def __init__(self, main_location: Path):
        self.main_loc = main_location

    def __create_dir(self, name):
        location = self.main_loc / name
        if not Path.exists(location):
            Path.mkdir(location)

    def organise(self, ):
        for file in self.main_loc.iterdir():
            pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


def main():
    location = Path(r'C:\Users\Admin\Desktop\TEST')
    org = Organiser(location)


if __name__ == '__main__':
    main()
