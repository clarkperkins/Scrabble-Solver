from cliff.command import Command


class Solve(Command):

    def take_action(self, parsed_args):
        self.app.stdout.write('asdfasf')