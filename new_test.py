class Animal(object):
    def __new__(cls, *args, **kw):
        return super().__new__(cls)

    def eat(self):
        print('eat something!')


# Python implicitly provides a default and typical implementation
# of __new__() which will invoke the superclass’s __new__() method
# to create a new instance object and then return it.
# so this return super().__new__(cls) returns an instance (self)
# so then I can call eat(self)
a = Animal()
a.eat()
