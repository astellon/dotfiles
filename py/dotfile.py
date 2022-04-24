from dataclasses import asdict, dataclass
from distutils.command.config import config
import logging
import os
import shutil


@dataclass
class Config:
    name: str
    src: str
    dst: str


class DotFile:
    def __init__(self) -> None:
        self.conf = self.config()

    def config(self) -> Config:
        raise NotImplementedError

    def info(self) -> None:
        print(asdict(self.conf))

    def build(self) -> None:
        pass

    def apply(self, force=False) -> None:
        if os.path.islink(self.conf.dst) or os.path.islink(self.conf.dst):
            logging.warn(f"Configuration already exits at {self.conf.dst}")

            if force:
                logging.warn(f"Remove existing files at {self.conf.dst}")
                if os.path.islink(self.conf.dst):
                    os.unlink(self.conf.dst)
                elif os.path.isdir(self.conf.dst):
                    shutil.rmtree(self.conf.dst)
                else:
                    os.remove(self.conf.dst)
            else:
                logging.info(f"Skip apply {self.conf.name}.")
                return False

        os.symlink(self.conf.src, self.conf.dst,
                   target_is_directory=os.path.isdir(self.conf.src))

        logging.info(f'Finish placing {self.conf.dst}')

        return True

    def update(self) -> None:
        pass
