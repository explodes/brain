import mock
from unittest2 import TestCase


class RandomNetTestCase(TestCase):

    @mock.patch('brain.app.commands.random_net.spawn_random')
    def test_spawn_random_called(self, spawn_random):
        from brain.app.commands.random_net import Command

        args = mock.NonCallableMock()
        args.length = 25
        args.connections = 25

        command = Command()
        command.run(args)

        spawn_random.assert_called_with(length=args.length, connections=args.connections)
