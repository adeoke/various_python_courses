"""module representing simple objects"""


class Animal:
    """example cat class"""

    def __init__(self, name):
        self.name = name

    def category(self):
        """returns the type of animal"""
        return 'Parent animal has no category'


class Cat(Animal):
    def category(self):
        """returns cat string as type of anumal"""
        return 'Type of Cat'


feline = Cat('Jane')
print(isinstance(feline, Animal) == True)
print(isinstance(feline, Cat) == True)
print(feline.name)

# override parent initial method in child class
print(feline.category())


class Car:
    def __init__(self, wheels):
        self.wheels = wheels


class Honda(Car):
    def __init__(self, wheels, model):
        super().__init__(wheels)
        self.model = model


honda = Honda(4, 'civic')
print(honda.wheels)
print(honda.model)


# Mixins

class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()


# pythonic getter setter
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age
        return self.__age


tom = Person(24)
print(tom.age)

# set age using decorator @age.setter
tom.age = 31
print(tom.age)

# set age again
tom.age = 22

# name mangling for privacy
try:
    tom.__age
except Exception as ex:
    print(ex)


# you can access the private local variable with this hack
print(tom._Person__age)


#class methods example
class A:
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm A")

    @classmethod
    def kids(cls):
        return f'this is the number of kids {cls.count}.'


letter_one = A()
letter_two = A()
letter_three = A()
print(A.kids())
print(A.count)

