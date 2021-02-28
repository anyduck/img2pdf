#!/usr/bin/python
from pathlib import Path
from PIL import Image


SUFFIXES = (
    '.png',
    '.jpg',
    '.jpeg'
)

IS_AUTO_PORTAIT_MODE = True
OUTPUT = 'output.pdf'


def get_images(folder: Path) -> list[Image.Image]:
    return [Image.open(path) for path in folder.iterdir()
            if path.is_file() and path.suffix in SUFFIXES]


def convert2portrait(images: list[Image.Image]) -> None:
    for image in images:
        if image.width > image.height:
            image.rotate(-90)  # TODO: detection of -90, 0, 90, 180


def save2pdf(images: list[Image.Image], path: Path) -> None:
    images[0].save(path, save_all=True, append_images=images[1:])


if __name__ == '__main__':
    folder = Path(input('Enter folder: '))
    images = get_images(folder)
    if IS_AUTO_PORTAIT_MODE:
        convert2portrait(images)
    save2pdf(images, OUTPUT)
