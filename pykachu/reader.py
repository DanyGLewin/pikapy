"""
Provide a basic assembler for the pikachu language.

Classes:
PikaReader -- The basic pikachu assembler
"""
from pykachu.utils import pika_error, pika_print


class PikaReader():
    """
    Provide a basic pikachu assembler and command parser.
    
    Methods:
    PikaReader(fileName) -> PikaReader
    goto(lineNo) -> void
    """

    def __init__(self, fileName):
        """
        Construct a PikaReader Object.

        Arguments:
        fileName -> the path to a pika file.
        """
        try:
            fi = open(fileName)
        except FileNotFoundError:
            pika_print("No file named: {}".format(fileName))
            exit()
        l = fi.readlines()
        self.lines = {x+1: l[x].strip().split(' chu ')[0] for x in range(len(l))}
        for lineNo in self.lines:
            for word in self.lines[lineNo].split():
                if word not in ('pi', 'pika', 'pikachu'):
                    raise pika_error(lineNo, 'unknown word "{}"'.format(word))
        if self.lines[len(self.lines)][-1] != '\n':
            self.lines[len(self.lines)+1] = 'pika pika pi pikachu' #arbitrary command that won't change the output
        self.lineNo = 0 
        fi.close()

    def next(self):
        """
        Provide support for the next() function.

        next(this) is used to iterate through the pikachu code a line at a time.
        
        Exceptions:
        StopIteration -- when the end of the file has been reached.
        """
        self.lineNo += 1
        if self.lineNo > len(self.lines):
            raise StopIteration
        line = self.lines[self.lineNo]
        if not line:
            return self.next()

        # check for invalid repetition of pi, pika, pikachu
        target = None
        reps = 0
        for term in line.split():
            if term == target:
                reps += 1
                if reps >= 3:
                    pika_error(self.lineNo, 'too many repetitions')
            else:
                target = term
                reps = 1

        return line

    def goto(self, lineNo):
        """
        Directs the reader to a specific line of code.

        Arguments:
        lineNo -- the line of code (1 based) to set the reader to.
        
        Error Handling:
        If lineNo is greater than the number of lines in the code. The reader 
        will be set at the end of the code.
        """
        if lineNo > len(self.lines):
            lineNo = len(self.lines)
        self.lineNo = lineNo - 1
