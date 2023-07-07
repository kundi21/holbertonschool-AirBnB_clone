#!/usr/bin/env python3
"""
Console for AirBnB Clone.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when the EOF (Ctrl+D) is encountered"""
        print()
        return True

    def do_help(self, args):
        """
        Gets help for a certain command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            model = BaseModel()
            print(model.id)

    def do_show(self, *args):

        model = BaseModel()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[1] != model.id:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
