import logging
import os
from dataclasses import dataclass
from subprocess import Popen, PIPE

from py.dotfile import Config, DotFile


@dataclass
class ZshConfig(Config):
    name: str = ".zshrc"
    src: str = os.path.join(os.path.dirname(__file__), ".zshrc")
    dst: str = os.path.join(os.environ["HOME"], ".zshrc")


class DotZsh(DotFile):
    def config(self):
        return ZshConfig()

    def build(self):
        if os.path.exists('~/.zplug'):
            logging.info('Zplug is already installed.')
            return

        url = 'https://raw.githubusercontent.com/zplug/installer/master/installer.zsh'
        p = Popen(['curl', '-sL', url], stdout=PIPE)
        p = Popen(['zsh'], stdin=p.stdout)
        p.wait()

    def update(self):
        Popen(['zsh', '-c', 'source $HOME/.zplug/init.zsh; zplug update']).wait()


if __name__ == '__main__':
    DotZsh().info()
