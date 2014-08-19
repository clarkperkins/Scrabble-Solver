from cliff.command import Command
from scrabble.cli import Colors


class Match(Command):
    """
    scrabble matcher
    """

    def get_parser(self, prog_name):
        parser = super(Match, self).get_parser(prog_name)
        parser.add_argument('letters')
        return parser

    def take_action(self, parsed_args):
        wl = self.app.solver.match(parsed_args.letters)

        self.app.out()
        self.app.out('{0}'.format(wl.string(', ')))
        self.app.out()