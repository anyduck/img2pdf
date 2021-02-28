#!/usr/bin/python
from pathlib import Path
from PIL import Image
from argparse import ArgumentParser


SUFFIXES = (
    '.png',
    '.jpg',
    '.jpeg'
)


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
    parser = ArgumentParser(description='Convert photos to pdf')
    parser.add_argument('folder', type=Path, help='folder with photos')
    parser.add_argument('-o', '--output', type=Path, default='output.pdf',
                        help='output pdf path')
    parser.add_argument('-p', '--portrait', action='store_true',
                        help='convert photos to portrait orientation')
    args = parser.parse_args()

    images = get_images(args.folder)
    if args.portrait:
        convert2portrait(images)
    save2pdf(images, args.output)
