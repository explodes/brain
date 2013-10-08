import argparse
import mock
from unittest2 import TestCase

from brain.app.command import BaseCommand


class MyCommand(BaseCommand):

    args = argparse.ArgumentParser(description='test')
    args.add_argument('-a', dest='a', type=str)
    args.add_argument('-b', dest='b', type=str)

    run = mock.Mock()  # Just to note that this method is mocked.

class CommandTestCase(TestCase):

    @mock.patch('brain.test.brain.app.test_command.MyCommand.run')
    def test_command_run_command_runs_run_with_args(self, run):
        # Test that the that `BaseCommand.run_command`
        # runs `run` with argparse args.

        command = MyCommand()

        # Run function
        command.run_command('-a', 'a', '-b', 'b')

        # Test result
        call_args_list = command.run.call_args_list
        self.assertEqual(len(call_args_list), 1)

        call = call_args_list[0]
        call_args, call_kwargs = call
        self.assertEqual(len(call_args), 1)
        self.assertEqual(len(call_kwargs), 0)

        parsed_args = call_args[0]
        self.assertEqual(parsed_args.a, 'a')
        self.assertEqual(parsed_args.b, 'b')
