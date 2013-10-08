class InvalidCommandException(Exception):
	pass

class BaseCommand(object):

	def run_command(self, *args):
		command_args = self.args.parse_args(args)
		self.run(command_args)
