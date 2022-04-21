import logging
import os
from dataclasses import dataclass
from subprocess import Popen, PIPE

from py.dotfile import Config, DotFile


@dataclass
class ZshenvConfig(Config):
    name: str = ".zshenv"
    src: str = os.path.join(os.path.dirname(__file__), ".zshenv")
    dst: str = os.path.join(os.environ["HOME"], ".zshenv")


class DotZshenv(DotFile):
    def config(self):
        return ZshenvConfig()
