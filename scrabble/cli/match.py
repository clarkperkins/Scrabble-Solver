from cliff.command import Command
from scrabble.cli import Colors
from scrabble.scrabble import Solver


class Match(Command):
    """
    scrabble matcher
    """

    def get_parser(self, prog_name):
        parser = super(Match, self).get_parser(prog_name)
        parser.add_argument('match_str')
        return parser

    def take_action(self, parsed_args):
        score_map = self.app.solver.match(parsed_args.match_str)

        self.app.out()
        for score, words in sorted(score_map.items()):
            for word in sorted(words):
                self.app.out('{0} '.format(word), Colors.GREEN, newline=False)
                self.app.out('({0})'.format(score), Colors.LIGHT_BLUE)
        self.app.out()


class SolveMatch(Command):
    """
    scrabble solve & match
    """

    def get_parser(self, prog_name):
        parser = super(SolveMatch, self).get_parser(prog_name)
        parser.add_argument('letters')
        parser.add_argument('match_str')
        return parser

    def take_action(self, parsed_args):
        wl = self.app.solver.solve(parsed_args.letters)

        score_map = self.app.solver.match(parsed_args.match_str, wl)

        self.app.out()
        for score, words in sorted(score_map.items()):
            for word in sorted(words):
                self.app.out('{0} '.format(word), Colors.GREEN, newline=False)
                self.app.out('({0})'.format(score), Colors.LIGHT_BLUE)
        self.app.out()

