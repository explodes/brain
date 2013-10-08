import imp
import os

from brain.app.command import InvalidCommandException


rel = lambda * x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))
command_dir = lambda *x: rel('commands', *x)
command_by_name = lambda command_name: command_dir('%s.py' % command_name)

def gather_command_names():
    directory = command_dir()

    commands = []
    for fname in os.listdir(directory):
        if not fname.startswith('_'):
            if fname.endswith('.py'):
                fpath = command_dir(fname)
                if os.path.isfile(fpath):
                    mod_name, file_ext = os.path.splitext(fname)
                    commands.append(mod_name)
    return sorted(commands)

def print_commands():
    print 'Available commands:'
    for command in gather_command_names():
        print '    %s' % command

def import_command_klass(command_name):
    filepath = command_by_name(command_name)

    expected_class = 'Command'

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    try:
        py_mod = imp.load_source(mod_name, filepath)
    except IOError as e:
        print e
        return None

    if hasattr(py_mod, expected_class):
        klass = getattr(py_mod, expected_class)
        return klass

def run_command(command_name, *command_line_args):
    klass = import_command_klass(command_name)

    if klass is not None:
        instance = klass()
        return instance.run_command(*command_line_args)
    else:
        raise InvalidCommandException('%s is not a valid command.' % command_name)

def run_command_line(*command_line_args):
    try:
        command_name = command_line_args[0]
        return run_command(command_name, *command_line_args[1:])
    except IndexError:
        return print_commands()

def main(argv):
    return run_command_line(*argv[1:])

