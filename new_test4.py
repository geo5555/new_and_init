class Animal(object):
    def __new__(cls, *args, **kwargs):
        print('__new__() called.')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('__init__() called')
        self.args = args
        self.kwargs = kwargs

    def printName(self):
        print("name")
        print("Args=", self.args)
        print("Kwargs=", self.kwargs)


a = Animal("monkey", 1, 2, 3)
# __new__ is called
# __init__ is  called
a.printName()
# fucntion is called
