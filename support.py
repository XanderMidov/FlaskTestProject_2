from datetime import datetime as dt
import locale
class SomeBaseClass:
    param1 = 'Some shit param'
    param2 = 'Another shit param'
    param3 = 'Class param'
    __list = iter(['Jopa', 'Piska', 'Sosat', 'Siski', 'Sosiski'])
    value = 0

    @classmethod
    def param3_change(cls, new_name):
        cls.param3 = new_name
        return cls.param3


    def __call__(self, *args):
        result = ''
        for arg in args:
            result += f'Argument {arg}\n'
        return result

    def __str__(self):
        return f'Param1: {SomeBaseClass.param1}, Param2: {self.param2}, Param3: {self.param3}'

    def __repr__(self):
        return f'Param1: {SomeBaseClass.param1}, Param2: {self.param2}, Param3: {self.param3}'

    def __iter__(self):
        return self.__list

    def __next__(self):
        return 'jopa'

item1 = SomeBaseClass()
item2 = SomeBaseClass()

class AnotherBaseClass:
    item1 = SomeBaseClass()
    item2 = SomeBaseClass()

    @classmethod
    def __repr__(cls):
        return f'Item 1: {cls.item1}, Item 2: {cls.item2}'

another_example = AnotherBaseClass()
pass
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(dt.now().strftime('%A-%d-%B-%y'))

my_list = [('Admin', 'John'), ('User', 'Susan'), ('User', 'David'), ('User', 'Sashulka'), ('Admin', 'Сашулька'), ('User', 'Побрекушкин'), ('User', 'Galushka'), ('User', 'Hrenushkin')]

for role, user in my_list:
    print(role, user)
