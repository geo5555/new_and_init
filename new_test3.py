class Animal(object):
    def __new__(cls):
        print('__new__() called.')
        return super().__new__(cls)

    def __init__(self):
        print('__init__() called')

    def printName(self):
        print("name")


a = Animal()
# __new__ is called
# __init__ is  called
# if i call Animal('monkey') I will get an error
a.printName()
# fucntion is called
