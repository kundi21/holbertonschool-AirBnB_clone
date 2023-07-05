#!/usr/bin/env python3
"""
Console for AirBnB Clone.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when the EOF (Ctrl+D) is encountered"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
