import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager
from scrabble.scrabble import Solver


class Colors:
    BLACK = '\033[0;30m'
    DARK_GRAY = '\033[1;30m'
    LIGHT_GRAY = '\033[0;37m'
    BLUE = '\033[0;34m'
    LIGHT_BLUE = '\033[1;34m'
    GREEN = '\033[0;32m'
    LIGHT_GREEN = '\033[1;32m'
    CYAN = '\033[0;36m'
    LIGHT_CYAN = '\033[1;36m'
    RED = '\033[0;31m'
    LIGHT_RED = '\033[1;31m'
    PURPLE = '\033[0;35m'
    LIGHT_PURPLE = '\033[1;35m'
    BROWN = '\033[0;33m'
    YELLOW = '\033[1;33m'
    WHITE = '\033[1;37m'
    DEFAULT_COLOR = '\033[00m'
    RED_BOLD = '\033[01;31m'
    ENDC = '\033[0m'


class ScrabbleApp(App):

    def __init__(self):
        super(ScrabbleApp, self).__init__(
            description='Scrabble solver',
            version='0.1',
            command_manager=CommandManager('scrabble.cli')
        )
        self.solver = None

    def out(self, msg='', color=Colors.DEFAULT_COLOR, newline=True):
        self.stdout.write(color + msg + Colors.ENDC)
        if newline:
            self.stdout.write('\n')

    def initialize_app(self, argv):
        self.solver = Solver(dict_file=os.path.join(sys.prefix, 'dictionaries', 'ospd.dict'))


def main(argv=sys.argv[1:]):
    app = ScrabbleApp()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main())