#!/usr/bin/python3
"""Entry point module for command interpreter."""

import cmd

class ABNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(abnb) "
    def do_EOF(self, line):
        """Handles End of file character.
        """

        print()
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER
        """

        pass


    def do_quit(self, line):
        """Exits the program."""

        return True


if __name__ == "__main__":
    ABNBCommand().cmdloop()
