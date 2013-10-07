#!/usr/bin/env python

commands = None; # Predefined


def usage(*args, **kwargs):
    print '-' * 13
    print '    BRAIN'
    print '-' * 13
    print
    global commands
    for command_name, details in commands.iteritems():
        func, about, args = details
        print '    ', command_name, '\n        ', about
    print

def random_net(*args, **kwargs):

    from brain.network import spawn_random

    net = spawn_random()
    print net.visual()



commands = {
    'help' : (usage, 'Show usage information', None),
    'random_net' : (random_net, 'Print out a random network', None)
}

def main(argv):
    try:
        command_name = argv[1]
    except IndexError:
        command_name = 'help'

    try:
        command, about, parser = commands[command_name]
        command(parser)
    except KeyError:
        print 'Command not found.'
        print
        usage()


if __name__ == '__main__':
    import sys
    main(sys.argv)