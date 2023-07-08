#!/usr/bin/env python3
"""
Console for AirBnB Clone.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """console for AirBnB Clone"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

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
        """Creates new instance of existing class"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        found = False
        for dictClasses in HBNBCommand.classes:
            if args[0] == dictClasses:
                found = True
                model = eval(args[0])()
                print(model.id)
                model.save()
                break
            else:
                found = False
        if found is False:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """Show specified class instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        found = False
        for dictClasses in HBNBCommand.classes:
            if args[0] == dictClasses:
                found = True
                break
            else:
                found = False
        if found is False:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model_id = args[1]
        key = args[0] + "." + model_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys specified class instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        found = False
        for dictClasses in HBNBCommand.classes:
            if args[0] == dictClasses:
                found = True
                break
            else:
                found = False
        if found is False:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model_id = args[1]
        key = args[0] + "." + model_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of specified class or not"""
        if not arg:
            for key in storage.all():
                print(storage.all()[key])
        else:
            classesDictCopy = HBNBCommand.classes[:]
            found = False
            for dictClasses in classesDictCopy:
                args = arg.split()
                if args[0] == dictClasses:
                    found = True
                    for key in storage.all():
                        if key.split('.')[0] == args[0]:
                            print(storage.all()[key])
                    break
                else:
                    found = False
            if found is False:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """Updates specified class instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        found = False
        for dictClasses in HBNBCommand.classes:
            if args[0] == dictClasses:
                found = True
                break
            else:
                found = False
        if found is False:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model_id = args[1]
        key = args[0] + "." + model_id
        if key in storage.all():
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
