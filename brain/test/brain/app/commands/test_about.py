import mock
from unittest2 import TestCase


class AboutTestCase(TestCase):

    @mock.patch('brain.app.commands.about.print_about_information')
    def test_print_about_info_called(self, print_about_information):
        from brain.app.commands.about import Command
        command = Command()
        command.run(None)
        print_about_information.assert_called_with()
