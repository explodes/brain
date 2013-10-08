import mock
from unittest2 import TestCase


class MainTestCase(TestCase):

    def test_rel_returns_directory(self):
        import os
        from brain.app.main import rel
        self.assertTrue(os.path.isdir(rel()))

    def test_command_dir_returns_directory(self):
        import os
        from brain.app.main import command_dir
        self.assertTrue(os.path.isdir(command_dir()))

    def test_command_by_name_returns_file(self):
        import os
        from brain.app.main import command_by_name
        # about.py will always be in the command directory.
        init = command_by_name('about')
        self.assertTrue(os.path.isfile(init))

    def test_gather_command_names(self):
        from brain.app.main import gather_command_names

        commands = gather_command_names()
        self.assertIsInstance(commands, list)

    def test_print_commands(self):
        from brain.app.main import print_commands
        print_commands()

    def test_import_command_klass(self):
        from brain.app.command import BaseCommand
        from brain.app.main import import_command_klass

        klass = import_command_klass('about')

        self.assertTrue(issubclass(klass, BaseCommand))

    def test_import_command_klass_not_found(self):
        from brain.app.main import import_command_klass

        klass = import_command_klass('THIS DOESNT EXIST.py')

        self.assertIsNone(klass)

    def test_run_command(self):
        from brain.app.main import run_command

        result = run_command('about')
        self.assertEqual(result, ':)')

    def test_run_command_not_found(self):
        from brain.app.command import InvalidCommandException
        from brain.app.main import run_command

        self.assertRaises(InvalidCommandException, run_command,
                          'THIS DOESNT EXIST.py')

    def test_run_command_line(self):
        from brain.app.main import run_command_line

        result = run_command_line('about')
        self.assertEqual(result, ':)')

    @mock.patch('brain.app.main.print_commands')
    def test_run_command_line_no_args(self, print_commands):
        from brain.app.main import run_command_line

        result = run_command_line()
        print_commands.assert_called_with()

    def test_main(self):
        from brain.app.main import main

        result = main(['./bin/main', 'about'])
        self.assertEqual(result, ':)')
