#!/usr/bin/python
from pathlib import Path

SUFFIXES = (
    '.png',
    '.jpg',
    '.jpeg'
)

def get_images(folder: Path) -> list[Path]:
    return [path for path in folder.iterdir() if path.is_file() and path.suffix in SUFFIXES]


if __name__ == '__main__':
    folder = input('Enter folder: ')
    print(get_images(Path(folder)))