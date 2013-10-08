import argparse


from brain.app.command import BaseCommand
from brain.network import spawn_random


class Command(BaseCommand):

    args = argparse.ArgumentParser(description="Print the results of constructing a random neural network.")
    args.add_argument('-n', '--length', dest='length', type=int, default=256, help='Number of neurons')
    args.add_argument('-c', '--connections', dest='connections', type=int, default=15, help='Number of connections per neuron')


    def run(self, args):

        length = args.length
        connections = args.connections

        network = spawn_random(length=length, connections=connections)

        print network.visual()