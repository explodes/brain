import mock
from unittest2 import TestCase


class CommandTestCase(TestCase):


    @mock.patch('brain.app.commands.command.Command')
    def test_command_runs_with_args(self, ):
        from brain.commands.command import Command

        patcher = mock.patch(Command, run=mock.Mock())

        with patcher as Command:

            c = Command()

