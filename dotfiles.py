import argparse
from ast import arg

from yaml import parse

# modules
from modules.zsh.zshrc import DotZshrc
from modules.zsh.zshenv import DotZshenv
from modules.alacritty.alacritty import DotAlacritty

dots = [
    DotZshrc(),
    DotZshenv(),
    DotAlacritty(),
]


def main():
    # top parser
    parser = argparse.ArgumentParser('.dotfiles')

    # global arguments

    # subcommand parser node
    subparsers = parser.add_subparsers(title='commands')

    # for build command
    parser_build = subparsers.add_parser(
        'build',
        help='Build configuration files.'
    )

    parser_build.set_defaults(func=build)

    # for apply command
    parser_apply = subparsers.add_parser(
        'apply',
        help='Place and apply configuration files.'
    )

    parser_apply.add_argument('--force', action='store_true',
                              help='Remove existing configuration files before applying')
    parser_apply.set_defaults(func=apply)

    # for update command
    parser_update = subparsers.add_parser(
        'update',
        help='Update configuration files.'
    )

    parser_update.set_defaults(func=update)

    args = parser.parse_args()

    args.func(args)


def build(args):
    for dot in dots:
        dot.build()


def apply(args):
    for dot in dots:
        dot.apply(args.force)


def update(args):
    for dot in dots:
        dot.update()


if __name__ == '__main__':
    main()
