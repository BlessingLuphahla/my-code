import os
from pathlib import Path

location = Path(r'C:\Users\Admin\Desktop\delete')

for file in location.iterdir():
    if file.is_file():
        if file.suffix.lower() == 'm4a':
            path = file.as_posix()
            name, ext = os.path.splitext(path)
            name = name + '.mp3'
            name = Path(name)
            name = name.open('wb')
            name.close()
