#!/usr/bin/python
from argparse import ArgumentParser, Namespace
from pathlib import Path
from PIL import Image


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


def save2pdf(images: list[Image.Image], path: Path, quality: int) -> None:
    images[0].save(path, format='pdf', quality=quality,
                   save_all=True, append_images=images[1:])


def main(folder: Path, output: Path, quality: int, portrait: bool) -> None:
    images = get_images(folder)
    if portrait:
        convert2portrait(images)
    save2pdf(images, output, quality)


def parse_args() -> Namespace:
    parser = ArgumentParser(description='Convert photos to pdf')
    parser.add_argument('folder', type=Path, help='folder with photos')
    parser.add_argument(
        '-o', '--output', dest='output', type=Path, default='output.pdf',
        help='output pdf path'
    )
    parser.add_argument(
        '-q', '--quality', dest='quality', type=int, default=70,
        help='quality of output images on a scale from 0 (worst) to 100 (best)'
    )
    parser.add_argument(
        '-p', '--portrait', dest='portrait', action='store_true',
        help='convert photos to portrait orientation'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args.folder, args.output, args.quality, args.portrait)
