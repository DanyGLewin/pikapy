"""
Provide common functions to the other modules in pikachu

Methods:
syntax_error -- print information about syntax errors in the pikachu program
"""

from click import secho

def pika_error(lineNo, msg):
    """
    Display information about syntax errors in the pikachu program then exit.

    Arguments:
    lineNo -- the line where the syntax error was found.
    """
    pika_print('SyntaxError in line {}: {}'.format(lineNo, msg))
    exit()

def pika_print(msg, nl=False, fg='yellow'):
	if type(msg) != msg:
		msg = str(msg)
	secho(msg, fg=fg, nl=nl)