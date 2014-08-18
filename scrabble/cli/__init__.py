import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class ScrabbleApp(App):

    def __init__(self):
        super(ScrabbleApp, self).__init__(
            description='Scrabble solver',
            version='0.1',
            command_manager=CommandManager('scrabble.cli')
        )


def main(argv=sys.argv[1:]):
    app = ScrabbleApp()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main())