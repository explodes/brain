import argparse

from brain.app.command import BaseCommand


def print_about_information():
    print 'Brain'
    print 'By Evan Leis'
    print 'v0.0.0'


class Command(BaseCommand):

    args = argparse.ArgumentParser(description="What is Brain.")

    def run(self, args):
        print_about_information()
        return ':)'
