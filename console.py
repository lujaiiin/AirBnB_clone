#!/usr/bin/python3
"""Modules"""
import cmd
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class for consolo in airbnb"""

    prompt = "(hbnb) "
    __cl = {
            "Review",
            "Place",
            "State",
            "User",
            "BaseModel",
            "Amenity",
            "City"
            }

    def do_EOF(self, lin):
        """EOF command to exit the program"""

        print('')
        return True

    def do_quit(self, lin):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """do nothing"""

        pass

    def do_create(self, lin):
        """to create"""

        firs = lin.split()
        if len(firs) == 0:
            print("** class name missing **")
        elif firs[0] not in HBNBCommand.__cl:
            print("** class doesn't exist **")
        else:
            print(eval(firs[0])().id)
            models.storage.save()

        """__show - print class name and id___"""

    def do_show(self, lin):

        _str = lin.split()
        if not lin:
            print("** class name missing **")
            return
        elif not self.do_check(_str[0]):
            return
        elif len(_str) < 2:
            print("** instance id missing **")
            return

        _object = _str[0] + '.' + _str[1]
        _dict = storage.all()

        if _object not in _dict:
            print("** no instance found **")
            return
        else:
            print(_dict[_object])

    def do_destroy(self, lin):

        _str = lin.split()
        if not lin:
            print("** class name missing **")
            return
        elif not self.do_check(_str[0]):
            return
        elif len(_str) < 2:
            print("** instance id missing **")
            return

        _object = _str[0] + '.' + _str[1]
        _dict = storage.all()

        if _object not in _dict:
            print("** no instance found **")
            return
        else:
            if _dict[_object] is not None:
                del _dict[_object]
                storage.save()

    def do_check(self, class_name):
        """__checks if the class name is exist in the __cl__"""

        if class_name not in HBNBCommand.__cl:
            print("** class doesn't exist **")
            return False
        return True

    def do_all(self, lin):
        """do all fun"""

        firs = lin.split(lin)
        lis = []
        if firs[0] not in HBNBCommand.__cl and len(firs) > 0:
            print("** class doesn't exist **")
        else:
            for k in storage.all().values():
                if len(firs) > 0 and firs[0] == i.__class__.__name__:
                    lis.append(obj.__str__())
                elif len(firs) == 0:
                    lis.append(i.__str__())
                    print(lis)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
