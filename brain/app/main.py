import imp
import os

from brain.app.command import InvalidCommandException


rel = lambda * x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))

def import_command_klass(command_name):
    filepath = rel('commands', '%s.py' % command_name)

    expected_class = 'Command'

    mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

    try:
        py_mod = imp.load_source(mod_name, filepath)
    except IOError as e:
        print e
        return None

    if hasattr(py_mod, expected_class):
        klass = getattr(py_mod, expected_class)
        return klass

def run_command(command_name, *args):
    klass = import_command_klass(command_name)

    if klass is not None:
        instance = klass()
        instance.run(*args)
    else:
        raise InvalidCommandException('%s is not a valid command.' % command_name)

def run_command_line(argv):
    try:
        command_name = argv[1]
    except IndexError:
        command_name = 'usage'

    run_command(command_name, argv[2:])


def main(argv):
    run_command_line(argv)

