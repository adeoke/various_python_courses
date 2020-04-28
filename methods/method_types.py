class One:
    def instance_method(self):
        print(f'this is an instance methods {self}')

    @classmethod
    def class_method(cls):
        ''' This method prints the class method name'''
        print(f'this is a class method {cls}')

    @staticmethod
    def static_method():
        print('this is a static method')


one = One()

print(One.instance_method(one))

print(One.class_method())

print(One.static_method())

print(One.class_method.__doc__)
