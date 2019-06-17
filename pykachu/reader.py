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
    goto(line_num) -> void
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
        lines = fi.readlines()
        self.lines = {x+1: lines[x].strip().split(' chu ')[0] for x in range(len(lines))}
        for line_num in self.lines:
            for word in self.lines[line_num].split():
                if word not in ('pi', 'pika', 'pikachu'):
                    raise pika_error(line_num, 'unknown word "{}"'.format(word))
        if self.lines[len(self.lines)][-1] != '\n':
            self.lines[len(self.lines)+1] = 'pika pika pi pikachu' #arbitrary command that won't change the output
        self.line_num = 0 
        fi.close()

    def next(self):
        """
        Provide support for the next() function.

        next(this) is used to iterate through the pikachu code a line at a time.
        
        Exceptions:
        StopIteration -- when the end of the file has been reached.
        """
        self.line_num += 1
        if self.line_num > len(self.lines):
            raise StopIteration
        line = self.lines[self.line_num]
        if not line:
            return self.next()

        # check for invalid repetition of pi, pika, pikachu
        target = None
        reps = 0
        for term in line.split():
            if term == target:
                reps += 1
                if reps >= 3:
                    pika_error(self.line_num, 'too many repetitions')
            else:
                target = term
                reps = 1

        return line

    def goto(self, line_num):
        """
        Directs the reader to a specific line of code.

        Arguments:
        line_num -- the line of code (1 based) to set the reader to.
        
        Error Handling:
        If line_num is greater than the number of lines in the code. The reader
        will be set at the end of the code.
        """
        if line_num > len(self.lines):
            line_num = len(self.lines)
        self.line_num = line_num - 1
