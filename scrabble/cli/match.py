from cliff.command import Command
from scrabble.cli import Colors
from scrabble.scrabble import Solver


class Match(Command):
    """
    scrabble matcher
    """

    def get_parser(self, prog_name):
        parser = super(Match, self).get_parser(prog_name)
        parser.add_argument('letters')
        return parser

    def take_action(self, parsed_args):
        remove_nums = parsed_args.letters.replace('2', '?').replace('3', '?')

        wl = self.app.solver.match(remove_nums)

        score_map = {}

        for word in wl:
            score = 0
            idx = 0
            for let in word:
                let_score = Solver.letter_mapping[let]
                if parsed_args.letters[idx] == '2':
                    let_score *= 2
                elif parsed_args.letters[idx] == '3':
                    let_score *= 3
                score += let_score
                idx += 1
            score_map.setdefault(score, []).append(word)

        self.app.out()
        for score, words in sorted(score_map.items()):
            for word in sorted(words):
                self.app.out('{0} '.format(word), Colors.GREEN, newline=False)
                self.app.out('({0})'.format(score), Colors.LIGHT_BLUE)
        self.app.out()