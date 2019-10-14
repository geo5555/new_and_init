class Animal(object):
    def __new__(cls):
        print('__new__() called.')

    def __init__(self):
        print('__init__() called')

    def printName():
        print("name")


a = Animal()
# init is not called
# i have not returned an instance of the class
a.printName()
# AttributeError: 'NoneType' object has no attribute 'printName'
