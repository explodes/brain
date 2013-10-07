class InvalidCommandException(Exception):
	pass

class BaseCommand(object):

	def run_command(self, *args):
		args = self.args.parse_args(args)
		self.run(args)
