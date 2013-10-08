"""
    Neurons represent connections and states.
    A rudimentary encoding algorithm has been created for visualization purposes.
"""


class Neuron(object):

    def __init__(self, state=0):
        self.state = state
        self.connections = []
        self.parents = []

    @staticmethod
    def crush(neurons):
        datum = 0
        for index, neuron in enumerate(neurons):
            datum ^= neuron.state << index
        return datum

    def get_code(self):
        upper = Neuron.crush(self.parents)
        lower = Neuron.crush(self.connections)
        code = (upper << lower.bit_length()) + lower
        return code

    def connect(self, neuron, check_existing=True):
        connect = True
        if check_existing:
            connect = neuron not in self.connections
        if connect:
            self.connections.append(neuron)
            neuron.parents.append(self)

    def visual(self):
        code = self.get_code()
        # A-Z,ord('A') => 65, ord('Z') => 90
        code %= 25 # Z - A
        code += 65 # + A
        return chr(code)

