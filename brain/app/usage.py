import argparse


class Command(object):

    args = argparse.ArgumentParser(description="Show app usage.")

    def run(self, *args, **kwargs):
        self.print_help()
        return 0