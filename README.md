# Pikachu Interpreter

This is an interpreter for Pikachu written in python 2.

The definition of the esoteric programming language named 'pikachu' can be found [here](http://trove42.com/introducing-pikachu-programming-language/)

### Installation:

1. run 
```bash
$ git clone https://github.com/DanyGLewin/Pykachu.git
```
2. Go to your Sublime Packages folder, which defaults to `~/Library/Application Support/Sublime Text 3/Packages` on Mac OSX and ` ` on Windows, create a new folder called Pikachu, and copy pikachu.sublime-syntax to there.

3. In the same Packages folder, find `Color Scheme - Default`, and copy `pikachu.sublime-color-scheme` there.

4. In Sublime Text, go to Preferences → Color Scheme, and select Pikachu.


### Usage - OSX

In the command line, go to the installation directory, and run:

```bash
$ pikachu {pikachu filename} [arguments*]
```