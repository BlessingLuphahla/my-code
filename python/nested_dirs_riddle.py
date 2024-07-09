import itertools
import random
import string
import sys
from pathlib import Path

location = Path(r'C:\Users\Admin\Desktop\riddle\good_luck')

alpha_cycle = itertools.cycle(string.ascii_uppercase)

NUMBER_OF_NESTED_ALPHA = 70
RECURSIVE_LIMIT = 400
HIDE_VALUE_MIN = 300


def create_folder(n):
    path = location / str(n)
    Path.mkdir(path) if not path.exists() else 'File Already Exists'
    return create_folder(n - 1) if n > 0 else 'Finished'


def from_other_folders(locate: Path):
    folders = []
    for folder in locate.iterdir():
        if folder.is_dir():
            folders.append(folder)
    return folders


def word() -> str:
    return next(alpha_cycle)


def nested(path: Path, start: int, /, *, limit=NUMBER_OF_NESTED_ALPHA):
    path /= str(word())
    if not path.exists():
        path.mkdir()

    return nested(path, start + 1) if start < limit else 0


def real_file(file_path):
    with open(file_path / 'notme.txt', 'w') as file:
        file.write('You found it well done!!!!!')


def random_file():
    possible_folders = []
    for folder, _, _ in tuple(location.walk()):
        if folder.name.isdigit() and int(folder.name) > HIDE_VALUE_MIN:
            possible_folders.append(folder)
    return random.choice(possible_folders)


def main():
    try:
        create_folder(RECURSIVE_LIMIT)
        for folder in from_other_folders(location):
            nested(folder, 1)

        for folder in location.walk():
            if folder[0] != location:
                with open(folder[0] / 'notme.txt', 'w') as not_me:
                    not_me.write('Nah ahh its not that easy check another file')
        real_file(random_file())

        print('I m done')
    except FileNotFoundError as e:
        print(e)
        pass
    except KeyboardInterrupt:
        print('You stopped the program')
        sys.exit(0)


if __name__ == '__main__':
    main()
