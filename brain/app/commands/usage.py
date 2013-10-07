import argparse

from brain.app.command import BaseCommand


class Command(BaseCommand):

    args = argparse.ArgumentParser(description="Show app usage.")

    def run(self, args):
        self.args.print_help()
        return 0