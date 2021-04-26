
class A:
    total_no_of_executes = 0

    def __init__(self, name):
        self.name = name
        self.no_of_executes = 0
        print(name)
        print('Class A')

    def execute(self, **kwargs):
        self.no_of_executes += 1
        A.total_no_of_executes += 1
        print(kwargs)
        print(self.name)
        print('Class A')

    def __del__(self):
        print(self.name)
        print('Class A')


class B:
    total_no_of_executes = 0

    def __init__(self, name):
        self.name = name
        self.no_of_executes = 0
        print(name)
        print('Class B')

    def execute(self, **kwargs):
        self.no_of_executes += 1
        B.total_no_of_executes += 1
        print(kwargs)
        print(self.name)
        print('Class B')

    def __del__(self):
        print(self.name)
        print('Class B')


class C:
    total_no_of_executes = 0

    def __init__(self, name):
        self.name = name
        self.no_of_executes = 0
        print(name)
        print('Class C')

    def execute(self, **kwargs):
        self.no_of_executes += 1
        C.total_no_of_executes += 1
        print(kwargs)
        print(self.name)
        print('Class C')

    def __del__(self):
        print(self.name)
        print('Class C')


if __name__ == "__main__":
    objs = {}

    while 1:
        try:
            choice = int(input("1. Create object of particular class with a name\t 2. Delete object of given name\n "
                               "3. Invoke execute with args for a given class\t 4. Print number of executes of given "
                               "object name\n 5. Print number of executes of a class\t 6. Quit\n"))
        except ValueError:
            print("Make an integer choice")
            continue

        if choice == 1:
            try:
                class_choice, name = input("Choose which class object is to be created and its name: ").split()
            except ValueError:
                print("Give two values. One for class among A,B,C and other the class name")
                continue
            if class_choice == 'A':
                objs[name] = A(name)
            elif class_choice == 'B':
                objs[name] = B(name)
            elif class_choice == 'C':
                objs[name] = C(name)
            else:
                print("Unknown Class")

        elif choice == 2:
            name = input("Class name to be deleted: ")
            if name not in objs:
                print("Object with this name is not created")
                continue
            del objs[name]

        elif choice == 3:
            try:
                raw = input("Class name and arguments: ")
            except ValueError:
                print("Give class name first and the arguments like a=1 b='Mr. John' so on")
                continue
            name = raw.split()[0]
            dic = raw[len(name) + 1:]
            dic = eval("dict(%s)" % dic.replace(" ", ","))
            objs[name].execute(**dic)

        elif choice == 4:
            name = input("Object name: ")
            if name not in objs:
                print("Object with this name is not created")
                continue
            print(name,'is executed',objs[name].no_of_executes,'times')

        elif choice == 5:
            class_choice = input("Class name: ")
            if class_choice == 'A':
                print(class_choice, 'is executed', A.total_no_of_executes, 'times')
            elif class_choice == 'B':
                print(class_choice, 'is executed', B.total_no_of_executes, 'times')
            elif class_choice == 'C':
                print(class_choice, 'is executed', C.total_no_of_executes, 'times')
            else:
                print("Unknown class")

        elif choice == 6:
            break

        else:
            print("Unknown choice")
