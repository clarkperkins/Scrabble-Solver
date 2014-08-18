from cliff.command import Command


class Match(Command):
    """
    scrabble matcher
    """

    def take_action(self, parsed_args):
        self.app.stdout.write('asdfasf')