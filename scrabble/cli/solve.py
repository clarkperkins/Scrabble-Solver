from cliff.command import Command
from scrabble.cli import Colors


class Solve(Command):
    """
    scrabble solver
    """

    def get_parser(self, prog_name):
        parser = super(Solve, self).get_parser(prog_name)
        parser.add_argument('letters')
        return parser

    def take_action(self, parsed_args):
        wl = self.app.solver.solve(parsed_args.letters)

        sorter = {}
        for word in wl:
            sorter.setdefault(len(word), []).append(word)

        self.app.out()

        for length, words in reversed(sorted(sorter.items())):
            self.app.out('{0} letter words ({1}):'.format(length, len(words)), Colors.GREEN)
            self.app.out('{0}'.format(', '.join(sorted(words))))
            self.app.out()
