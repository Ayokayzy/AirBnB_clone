#!/usr/bin/python3
"""
console.py
"""
import cmd
from models import storage, all_class as my_list


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        return

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def do_create(self, line):
        c = line.split(" ")
        if len(c) == 1 and c[0] == "":
            print("** class name missing **")
        elif len(c) == 1:
            if c[0] not in my_list:
                print("** class doesn't exist **")
            else:
                instance = my_list[c[0]]()
                instance.save()
                print(instance.id)

    def help_create(self):
        print(
            """Creates a new instance of BaseModel,\
 saves it (to the JSON file) and prints the id\n"""
        )

    def do_show(self, line):
        c = line.split(" ")
        if len(c) == 1 and c[0] == "":
            print("** class name missing **")
        elif len(c) < 2:
            print("** instance id missing **")
            return
        elif len(c) == 2:
            if c[0] not in my_list:
                print("** class doesn't exist **")
                return

            my_id = f"{c[0]}.{c[1]}"
            my_obj = storage.all()
            if my_id not in my_obj:
                print("** no instance found **")
            else:
                print(my_obj[my_id])

    def help_show(self):
        print(
            "Show Prints the string representation of\
 an instance based on the class name and id"
        )

    def do_destroy(self, line):
        c = line.split(" ")
        my_obj = storage.all()
        if len(c) == 1 and c[0] == "":
            print("** class name missing **")
        elif len(c) < 2:
            print("** instance id missing **")
            return
        elif len(c) == 2:
            if c[0] not in my_list:
                print("** class doesn't exist **")
                return

            del my_obj[f"{c[0]}.{c[1]}"]
            storage.save()

    def help_destroy(self):
        print(
            "Deletes an instance based on\
 the class name and id"
        )

    def do_all(self, line):
        c = line.split(" ")
        my_obj = storage.all()
        if c[0] != "" and c[0] not in my_list:
            print("** class doesn't exist **")
        elif c[0] != "":
            all_models = [
                str(value) for value in my_obj.values()
                if value.__class__.__name__ == f"{c[0]}"
            ]
            print(all_models)
        else:
            all_models = list(
                str(my_obj[key]) for key, value in my_obj.items()
            )
            print(all_models)

    def help_all(self):
        print(
            "Prints all string representation of all\
instances based or not on the class name"
        )

    def do_update(self, line):
        c = line.split(" ")
        if c[0] == "":
            print("** class name missing **")
            return
        if c[0] not in my_list:
            print("** class doesn't exist **")
            return
        if len(c) < 2:
            print("** instance id missing **")
            return
        if len(c) >= 2:
            my_id = f"{c[0]}.{c[1]}"
            my_obj = storage.all()
            if my_id not in my_obj:
                print("** no instance found **")
                return
        if len(c) < 3:
            print("** attribute name missing **")
            return
        if len(c) < 4:
            print("** value missing **")
            return

        # find object instance
        obj = dict(filter(lambda item: item[0] == my_id, my_obj.items()))
        obj_dict = obj[my_id].__dict__
        obj_dict[c[2]] = c[3].strip('\"')
        obj[my_id].save()

    def help_update(self):
        print(
            "Updates an instance based on the class name\
and id by adding or updating attribute"
        )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
