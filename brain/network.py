#!/usr/bin/env python

from brain import neuron


class Network(list):


    def __init__(self, neurons):
        super(Network, self).__init__(*neurons)


    def __unicode__(self):
         return u''.join((unicode(neuron) for neuron in self))


def spawn_random(length=128, connections=5):
    import random
    rand = random.Random()
    network = Network(
        (neuron.Neuron(state=rand.getrandbits(1)) for 
        dummy_x in xrange(length))
    )

    for dummy_x in xrange(connections * length):

        parent = rand.choice(network)
        child = rand.choice(network)
        if parent != child:
            parent.connect(child)

    return network


if __name__ == '__main__':
    import sys

    program, network_size, connections = sys.argv
    network = spawn_random(length=network_size, connections=connections)

    print network