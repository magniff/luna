import sys

from pylua.bytecode import Parser

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print "You must supply a filename"
        return 1
    p = Parser(filename).parse()
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)