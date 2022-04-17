import logging
import os
from dataclasses import dataclass

from py.dotfile import Config, DotFile


@dataclass
class AlacrittyConfig(Config):
    name: str = "alacritty.yml"
    src: str = os.path.join(os.path.dirname(__file__))
    dst: str = os.path.join(os.environ["HOME"], '.config', 'alacritty')


class DotAlacritty(DotFile):
    def config(self):
        return AlacrittyConfig()


if __name__ == '__main__':
    DotAlacritty().info()
