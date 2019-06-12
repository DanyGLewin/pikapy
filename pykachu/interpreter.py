"""Check the syntax and execute Pikachu commands.

Methods:
run -- The main context for the pikachu vm.
"""

import sys
from pykachu.utils import pika_error, pika_print
from pykachu.reader import PikaReader
from pykachu.stack import PikaStack


def run(fileName, args):
    """
    Run a specified Pikachu file in a virtual environment.

    Arguments:
    fileName -- the name and path of a file containing a pikachu program.
    args -- the command line arguments specified when the pikachu interpreter was
    run.
    """
    piStack = PikaStack()
    pikaStack = PikaStack()

    stackDict = {
        "pi pikachu": piStack,
        "pika pikachu": pikaStack
    }

    for a in args:
        piStack.PUSH(a)

    reader = PikaReader(fileName)
    while True:
        try:
            command = next(reader)
        except StopIteration:
            break
        command = command.split(' chu')[0]
        terms = command.split()
        if len(terms) == 0:
            continue
        if len(terms) == 1:
            pika_error(reader.lineNo, 'unknown command "{}"'.format(terms[0]))
        elif len(terms) < 3:
            command = " ".join(terms)
            if command == "pi pikachu":
                piStack.POP()
            elif command == "pika pikachu":
                pikaStack.POP()
            elif command == "pi pika":
                if not piStack.EMPTY():
                    pikaStack.PUSH(piStack.PEEK())
            elif command == "pika pi":
                if not pikaStack.EMPTY():
                    piStack.PUSH(pikaStack.PEEK())
            elif command == "pikachu pikachu":
                try:
                    lineNo = len(next(reader).split())
                except StopIteration:
                    pika_error(reader.lineNo - 1, "unexpected EoF, expected new line")
                if piStack.PEEK() != pikaStack.PEEK():
                    continue
                reader.goto(lineNo)
            elif command == "pika pika":
                try:
                    lineNo = len(next(reader).split())
                except StopIteration:
                    pika_error(reader.lineNo - 1, "unexpected EoF, expected new line")
                if piStack.PEEK() == pikaStack.PEEK():
                    continue
                reader.goto(lineNo)
            else:
                pika_error(reader.lineNo, 'unknown command "{}"'.format(reader.lines[reader.lineNo]))
        elif len(terms) < 4:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                pika_error(reader.lineNo, 'unknown pikachu "{}"'.format(" ".join(terms[-2:])))
            command = terms[0]
            if command == "pikachu":
                tStack.DIV()
            else:
                tStack.PUSH(1)
        elif len(terms) < 5:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                pika_error(reader.lineNo, 'unknown pikachu "{}"'.format(" ".join(terms[-2:])))
            command = " ".join(terms[:-2])
            if command == "pi pika":
                tStack.ADD()
            elif command == "pika pi":
                tStack.SUB()
            elif command == "pi pikachu":
                tStack.MULT()
            elif command == "pika pikachu":
                if not tStack.EMPTY():
                    pika_print(tStack.POP())
                else:
                    pika_print("undefined")
            elif command == "pikachu pikachu":
                n = tStack.POP()
                if n != None and type(n) == int:
                    pika_print(chr(n))
                else:
                    pika_print("undefined")
            else:
                tStack.PUSH(2)
        else:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                pika_error(reader.lineNo, 'unknown pikachu "{}"'.format(" ".join(terms[-2:])))
            tStack.PUSH(len(terms) - 2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        pika_print("No Pika file specified")
        exit()
    fileName = sys.argv[1]
    try:
        args = [int(x) for x in sys.argv[2:]]
    except ValueError:
        pika_print("invalid argument list: ", sys.argv[2:])
        exit()
    run(fileName, args)
