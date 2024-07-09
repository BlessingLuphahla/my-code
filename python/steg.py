import fileinput
from pathlib import Path


class Steganography:
    def __init__(self, multiple: bool = False):

        self.multiple = multiple

        self.main_location: Path = Path(r'C:\Users\Admin\Desktop\steg')
        self.picture: Path = self.main_location / 'pic.jpg'
        self.song: Path = self.main_location / 'song.mp3'
        self.new_location: Path = self.main_location / 'pic.png'

    def __extract_from_picture(self):
        with open(self.picture, 'rb') as f:
            return f.read()

    def __extract_from_song(self):
        if self.multiple:
            return b''
        with open(self.song, 'rb') as f:
            return f.read()

    def inject_bytes_to_file(self, data: bytes):
        with open(self.new_location, 'wb') as f:
            f.write(data)
        return 0

    def data(self):
        data_set = set()
        data_set.add(self.__extract_from_picture())
        data_set.add(self.__extract_from_song())
        data_set.update(self.multiple_files())

        data_set = sorted(list(data_set), key=lambda x: x == self.__extract_from_picture()[0:10])

        return b'\n'.join(data_set)

    def conditions_for_mul_data(self, file: Path):
        if file.suffix.lower() in ('mp3', 'm4a'):
            return True
        return False

    def multiple_files(self):

        if not self.multiple:
            return set()

        data = set()
        locations = set()
        for file in self.main_location.iterdir():
            locations.add(file)

        for file in fileinput.input(tuple(locations), mode='rb'):
            data.add(file)

        return data


def main():
    instance = Steganography(True)
    data = instance.data()
    result = instance.inject_bytes_to_file(data)
    print(result)


if __name__ == '__main__':
    main()
