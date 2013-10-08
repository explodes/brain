from unittest2 import TestCase


class NeuronTestCase(TestCase):

    def test_crush(self):
        from brain.neuron import Neuron

        node = Neuron()

        self.assertIsInstance(Neuron.crush([node]), int)

    def test_get_code(self):
        from brain.neuron import Neuron

        node = Neuron()

        self.assertIsInstance(node.get_code(), int)

    def test_connect(self):
        from brain.neuron import Neuron

        parent = Neuron()
        child = Neuron()

        parent.connect(child)

        self.assertSequenceEqual(parent.parents, [])
        self.assertSequenceEqual(parent.connections, [child])

        self.assertSequenceEqual(child.parents, [parent])
        self.assertSequenceEqual(child.connections, [])

    def test_visual(self):
        from brain.neuron import Neuron

        node = Neuron()

        self.assertIsInstance(node.visual(), (str, unicode))

    def test_neuron(self):
        from brain.neuron import Neuron

        node = Neuron()

        self.assertEqual(node.state, 0)
        self.assertSequenceEqual(node.parents, [])
        self.assertSequenceEqual(node.connections, [])
