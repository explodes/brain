class InvalidCommandException(Exception):
	pass

class BaseCommand(object):

	def run_command(self, *command_line_args):
		command_args = self.args.parse_args(*command_line_args)
		self.run(command_args)
