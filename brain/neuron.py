


class Neuron(object):

    def __init__(self):
        self.state = 0
        self.connections = []
        self.parents = []

    @staticmethod
    def crush(neurons, size=8):
        datum = 0
        for index, neuron in enumerate(neurons):
            datum ^= neuron.state << (index % size)
        return datum

    def get_code(self):
        upper = Neuron.crush(self.parents, size=16)
        lower = Neuron.crush(self.connections, size=16)
        code = (upper << 16) + lower
        return code

    def connect(self, neuron, check_existing=True):
        connect = True
        if check_existing:
            connect = neuron not in self.connections
        if connect:
            self.connections.append(neuron)
            neuron.parents.add(self)

    def __unicode__(self):
        print unichr(self.get_code())

