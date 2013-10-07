import argparse

from brain.app.command import BaseCommand


class Command(BaseCommand):

    args = argparse.ArgumentParser(description="Print the results of constructing a random neural network.")

    def run(self, args):
        self.args.print_help()
        return 0