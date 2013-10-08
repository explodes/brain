import mock
from unittest2 import TestCase


class NetworkTestCase(TestCase):

    def test_no_construct(self):
        from brain.network import Network

        net = Network()
        self.assertIsInstance(net, list)

    def test_empty_construct(self):
        from brain.network import Network

        net = Network([])
        self.assertIsInstance(net, list)

    def test_some_construct(self):
        from brain.network import Network

        neuron = mock.NonCallableMock()
        net = Network([neuron, neuron, neuron])
        self.assertIsInstance(net, list)

    def test_visual(self):
        from brain.network import Network

        neuron = mock.NonCallableMock()
        neuron.visual.return_value = 'A'

        net = Network([neuron, neuron, neuron])

        self.assertEqual(net.visual(), 'AAA')


    def test_spawn_random(self):
        from brain.network import Network
        from brain.network import spawn_random

        net = spawn_random(length=10, connections=10, rng=None)

        self.assertIsInstance(net, Network)
        self.assertEqual(len(net), 10)
