from brain import neuron


class Network(list):

    def __init__(self, neurons):
        super(Network, self).__init__(neurons)

    def visual(self):
         return u''.join(neuron.visual() for neuron in self)

def spawn_random(length=1024, connections=32):
    import random

    rand = random.Random()

    network = Network((
        neuron.Neuron(state=rand.getrandbits(1)) for 
        dummy_x in xrange(length)
    ))

    for dummy_x in xrange(connections * length):
        parent = rand.choice(network)
        child = rand.choice(network)
        if parent != child:
            parent.connect(child)

    return network
