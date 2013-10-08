import random

from brain.neuron import Neuron


class Network(list):

    def __init__(self, neurons=()):
        super(Network, self).__init__(neurons)

    def visual(self):
        return u''.join(neuron.visual() for neuron in self)


def spawn_random(length=1024, connections=32, rng=None):

    if rng is None:
        rng = random.Random()

    network = Network((
        Neuron(state=rng.getrandbits(1)) for
        dummy_x in xrange(length)
    ))

    for dummy_x in xrange(connections * length):
        parent = rng.choice(network)
        child = rng.choice(network)
        if parent != child:
            parent.connect(child)

    return network
