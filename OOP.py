# КУРС ПО ООП

"""class Gun:
        def shoot(self):
                print('pif')"""

"""class User:
        def __init__(self, name, friends = 0):
                self.name = name
                self.friends = friends
        def add_friends(self, n):
                self.friends += n"""

"""class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, color):
        self.color = color

    def add_rooms(self, n):
        self.rooms += n"""
from math import pi

"""class Circle:
        def __init__(self,radius):
                self.radius = radius
                self.diameter = 2 * radius
                self.area = math.pi*(radius**2)"""

"""class Bee:
        def __init__(self,x=0,y=0):
                self.x=x
                self.y=y
        def move_up(self,n):
                self.y +=n
        def move_down(self,n):
                self.y -=n
        def move_right(self,n):
                self.x +=n
        def move_left(self,n):
                self.x -=n"""
"""from itertools import cycle
class Gun:
        def __init__(self):
                self.sounds = cycle(['pif','paf'])
                self.count = 0
        def shoot(self):
                 print(next(self.sounds))
                 self.count += 1
        def shots_count(self):
                return self.count

        def shots_reset(self):
                self.sounds = cycle(['pif', 'paf'])
                self.count = 0"""

"""class Scales:
        def __init__(self):
                self.r = 0
                self.l = 0
        def add_right(self,n):
                self.r += n
        def add_left(self,n):
                self.l += n
        def get_result(self):
                if self.r == self.l:
                        return 'Весы в равновесии'
                if self.r > self.l:
                        return 'Правая чаша тяжелее'
                if self.l > self.r:
                        return 'Левая чаша тяжелее'"""

"""class Vector:
        def __init__(self,x=0,y=0):
                self.x = x
                self.y = y
        def abs(self):
                return math.sqrt((self.x**2) + (self.y **2) )"""

"""class Numbers:
        def __init__(self):
                self.lst = []
        def add_number(self,n):
                self.lst.append(n)
        def get_even(self):
                return [i for i in self.lst if i%2== 0]
        def get_odd(self):
                return [i for i in self.lst if i%2 != 0]"""

"""class TextHandler:
        def __init__(self):
                self.lst = []

        def add_words(self, n):
                self.lst+=n.split()

        def get_shortest_words(self):
                return [i for i in self.lst if len(i) == len(min(self.lst,key=len))]
        def get_longest_words(self):
                return [i for i in self.lst if len(i) == len(max(self.lst,key=len))]"""

"""class Todo:
        def __init__(self):
                self.things = []

        def add(self, t,p):
                self.things.append((t,p))
        def get_by_priority(self,n):
                return [i[0] for i in self.things if i[1] == n]
        def get_low_priority(self):
                res = min(self.things,key=lambda x:x[1],default=[])
                return [i[0] for i in self.things if i[1] == res[1]]
        def get_high_priority(self):
                res = max(self.things, key=lambda x: x[1],default=[])
                return [i[0] for i in self.things if i[1] == res[1]]"""

"""class Postman:
        def __init__(self):
                self.delivery_data = []
        def add_delivery(self,s,h,k):
                self.delivery_data.append((s,h,k))
        def get_houses_for_street(self,street):
                dict_k= {}.fromkeys([i[1] for i in self.delivery_data if i[0] == street])
                return list(dict_k.keys())
        def get_flats_for_house(self,street,house):
                dict_k = {}.fromkeys([i[2] for i in self.delivery_data if i[0] == street and i[1] == house])
                return list(dict_k.keys())"""

"""class Wordplay:
        def __init__(self,words = []):
                self.words = words.copy()

        def add_word(self,word):
                if word not in self.words:
                        self.words.append(word)

        def words_with_length(self,n):
                return [i for i in self.words if len(i) == n]

        def only(self,*args):
                return [i for i in self.words if set(i).issubset(set(args))]

        def avoid(self,*args):
                return [i for i in self.words if  set(i).isdisjoint(set(args))]"""

"""class Knight:
        def __init__(self,horizontal,vertical,color):
                self.horizontal= horizontal
                self.vertical = vertical
                self.color = color
                self.alf = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        def get_char(self):
                return 'N'

        def can_move(self, hor,ver):
                if abs(self.alf[self.horizontal] - self.alf[hor]) == 2 and abs(self.vertical - ver) == 1 or abs(self.alf[self.horizontal] - self.alf[hor]) == 1 and abs(self.vertical - ver) == 2:
                        return True
                else:
                        return False

        def move_to(self,hor,ver):
                if self.can_move(hor, ver):
                        self.horizontal = hor
                        self.vertical = ver

        def draw_board(self):
                x, y = self.horizontal, self.vertical
                n = 8
                board = [['.'] * n for _ in range(n)]
                x = ord(x) - 97
                y = n - int(y)
                board[y][x] = 'N'
                for i in range(n):
                        for j in range(n):
                                if abs(y - i) * abs(x - j) == 2:
                                        board[i][j] = '*'

                for row in board:
                        print(''.join(row))"""

"""class Circle:
        def __init__(self,radius):
                self._radius = radius
                self._diameter = 2 * radius
                self._area = math.pi * (radius ** 2)
        def get_radius(self):
                return self._radius
        def get_diameter(self):
                return self._diameter
        def get_area(self):
                return self._area"""

"""class BankAccount:
        def __init__(self,balance=0):
                self._balance = balance
        def get_balance(self):
                return self._balance
        def deposit(self,amount):
                self._balance += amount
        def withdraw(self,amount):
                if amount <= self._balance:
                        self._balance -= amount
                else:
                        raise ValueError('На счете недостаточно средств')
        def transfer(self,account,amount):
                if amount < self._balance:
                        self._balance -= amount
                else:
                        raise ValueError('На счете недостаточно средств')

                account._balance += amount"""

"""class User:
        def __init__(self,name,age):
                if self.set_name(name):
                        self._name = name
                if self.set_age(age):
                        self._age = age
        def set_name(self,new_name):
                if isinstance(new_name, str) and new_name.isalpha() and len(new_name)>0:
                        self._name = new_name
                        return True
                else:
                        raise ValueError('Некорректное имя')
        def set_age(self,new_age):
                if isinstance(new_age,int) and new_age in range(0,111):
                        self._age = new_age
                        return new_age
                else:
                        raise ValueError('Некорректный возраст')

        def get_name(self):
                return self._name

        def get_age(self):
                return self._age"""
"""class Rectangle:
        def __init__(self,length, width):
                self.length = length
                self.width = width
        def perimeter(self):
                return (self.width + self.length) * 2
        def area(self):
                return self.width * self.length

        perimeter = property(perimeter)
        area = property(area)
"""

"""class HourClock:
        def __init__(self,hours):
                self.hours = hours
        def set_hours(self,hours):
                if hours in range(1,13) and isinstance(hours, int):
                        self._hours = hours
                else:
                        raise ValueError ('Некорректное время')
        def get_hours(self):
                return self._hours

        hours = property(get_hours,set_hours)"""

"""class Person:
        def __init__(self,name,surname):
                self.name = name
                self.surname = surname
        def get_fullname(self):
                return f'{self.name} {self.surname}'

        def set_fullname(self,info):
                self.name,self.surname = info.split()

        fullname = property(get_fullname,set_fullname)"""

"""class Person:
        def __init__(self,name,surname):
                self.name = name
                self.surname = surname
        @property
        def fullname(self):
                return f'{self.name} {self.surname}'
        @fullname.setter
        def fullname(self,info):
                self.name, self.surname = info.split()"""

"""def hash_function(password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
                hash_value += ord(char) * index
        return hash_value % 10 ** 9
class Account:
        def __init__(self,login,password):
                self._login = login
                self.password= password
        @property
        def login(self):
                return self._login

        @login.setter
        def login(self,login):
                raise AttributeError ('Изменение логина невозможно')

        @property
        def password(self):
                return self._password

        @password.setter
        def password(self,password):
                 self._password = hash_function(password)
                 return self._password"""

"""class QuadraticPolynomial:
        def __init__(self,a,b,c):
                self.a = a
                self.b = b
                self.c = c
                self.__d = (b ** 2) - (4 * a * c) # Дискрименант
        @property
        def x1(self):
                if self.__d >= 0:
                        return (-self.b - (math.sqrt(self.b **2 - 4 * self.a * self.c))) / (2 * self.a)
                else:
                        return None
        @property
        def x2(self):
                if self.__d >= 0:
                        return  (-self.b + (math.sqrt(self.b **2 - 4 * self.a * self.c))) / (2 * self.a)
        @property
        def view(self):
                return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

        @property
        def coefficients(self):
                return (self.a,self.b,self.c)
        @coefficients.setter

        def coefficients(self,x):
                self.a = x[0]
                self.b = x[1]
                self.c = x[2]
                self.__d = (self.b ** 2) - (4 * self.a *  self.c)"""

""" self.r = int(hexcode[0:2],16)
                self.g = hexcode[2:4]
                self.b = int(hexcode[4:6],16)
"""
"""class Color:
        def __init__(self,hexcode):
                self._hexcode = hexcode
                self.r = int(self._hexcode[0:2],16)
                self.g = int(self._hexcode[2:4],16)
                self.b = int(self._hexcode[4:6],16)
        @property
        def hexcode(self):
                return self._hexcode

        @hexcode.setter
        def hexcode(self,str):
               self.__init__(str)"""

"""class Circle:
        def __init__(self,radius):
                self.radius = radius
        @classmethod
        def from_diameter(cls,diameter):
                return cls (diameter/2)"""
"""class Rectangle:
        def __init__(self,length,width):
                self.length= length
                self.width = width
        @classmethod
        def square(cls,side):
                return cls (side,side)"""

"""class QuadraticPolynomial:
        def __init__(self,a,b,c):
                self.a,self.b,self.c = a,b,c
        @classmethod
        def from_iterable(cls,iterable):
                return cls (iterable[0],iterable[1],iterable[2])
        @classmethod
        def from_str(cls,str):
                str = [float(i) for i in str.split()]
                return cls.from_iterable(str)"""

"""class Pet:
        pets = []
        def __init__(self,name):
                self.name = name
                if self not in Pet.pets:
                        Pet.pets.append(self)
        @classmethod
        def first_pet(cls):
                if Pet.pets:
                        return Pet.pets[0]
        @classmethod
        def last_pet(cls):
                if Pet.pets:
                        return Pet.pets[-1]
        @classmethod
        def num_of_pets(cls):
                return len(Pet.pets)"""

"""class StrExtension:
        @staticmethod
        def remove_vowels(str):
                return ''.join(re.findall(r'[^aeiouyAEIOUY]',str))
        @staticmethod
        def leave_alpha(str):
                return ''.join(re.findall(r'[a-zA-Z]',str))
        @staticmethod
        def replace_all(string, chars, char):
                return re.sub('['+ chars + ']', char, string)"""

"""class Processor:
        @singledispatchmethod
        def process(data):
                raise TypeError('Аргумент переданного типа не поддерживается')

        @process.register
        def _int_process(data:int | float):
                return data * 2

        @process.register
        def _str_proc(data: str):
                return data.upper()

        @process.register
        def _list_proc(data: list):
                return sorted(data)

        @process.register
        def _tuple_proc(data: tuple):
                return tuple(sorted(data))"""

"""class Negator:
        @singledispatchmethod
        @staticmethod
        def neg(arr):
                raise TypeError('Аргумент переданного типа не поддерживается')
        @neg.register
        def _int_neg(arr: int | float):
                return -arr
        @neg.register
        def bool_neg(arr: bool):
                return not arr"""

"""class Config:
        _flag = None
        def __new__(cls, *args, **kwargs):
                if cls._flag is None:
                        cls._flag = object.__new__(cls)
                return cls._flag

        def __init__(self):
                self.program_name = 'GenerationPy'
                self.environment = 'release'
                self.loglevel = 'verbose'
                self.version = '1.0.0'"""

"""class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return  f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"""

"""class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
            return f"Rectangle({self.length}, {self.width})"
    def __repr__(self):
            return f"Rectangle({self.length}, {self.width})"""

"""class Vector:
        def __init__(self,x,y):
                self.x,self.y=x,y
        def __repr__(self):
                return f"Vector({self.x}, {self.y})"
        def __str__(self):
                return f"Вектор на плоскости с координатами ({self.x}, {self.y})"""

"""class IPAddress:
        @singledispatchmethod
        def __init__(self,ipaddress: str):
                self.ipaddress = ipaddress
        @__init__.register
        def cool(self,ipaddress: list | tuple):
                self.ipaddress = '.'.join(map(str,ipaddress))

        def __str__(self):
                return self.ipaddress

        def __repr__(self):
                return f"IPAddress('{self.ipaddress}')"""

"""class PhoneNumber:
        def __init__(self,phone_number):
                self.phone_number = phone_number.replace(' ','')
        def __repr__(self):
                return f"{self.__class__.__name__}('{self.phone_number}')"
        def __str__(self):
                return f"({self.phone_number[0:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"""

"""class AnyClass:
        def __init__(self,**kwargs):
                self.__dict__.update(kwargs)

        def __str__(self):
                return f"AnyClass: {', '.join(f"{k}={repr(v)}" for k,v in self.__dict__.items())}"

        def __repr__(self):
                return f"AnyClass({', '.join(f"{k}={repr(v)}" for k,v in self.__dict__.items())})"""

"""class Vector:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def __repr__(self):
                return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"

        def __eq__(self, other):
                if isinstance(other, Vector):
                        return self.x == other.x and self.y == other.y
                if isinstance(other, tuple) and len(other)==2:
                        return self.x == other[0] and self.y == other[1]
                return NotImplemented"""
"""@total_ordering
class Word:
        def __init__(self, word):
                self.word =word
        def __repr__(self):
                return f"{self.__class__.__name__}({self.word!r})"
        def __str__(self):
                return self.word.title()
        def __eq__(self, other):
                if isinstance(other, Word):
                        return len(self.word) == len(other.word)
                return NotImplemented
        def __lt__(self, other):
                if isinstance(other, Word):
                        return len(self.word) < len(other.word)
                return NotImplemented"""
"""@total_ordering
class Month:
        def __init__(self,year,month):
                self.year = year
                self.month = month
                self.dt = date(year,month,1)
        def __repr__(self):
                return f"{self.__class__.__name__}{self.year, self.month}"
        def __str__(self):
                return f"{self.year}-{self.month}"
        def __eq__(self, other):
                if isinstance(other, Month):
                        return self.dt == other.dt
                if isinstance(other,tuple) and len(other) == 2:
                        return self.dt == date(other[0],other[1],1)
                return NotImplemented
        def __ge__(self, other):
                if isinstance(other, Month):
                        return  self.dt > other.dt
                if isinstance(other,tuple) and len(other) == 2:
                        return  self.dt > date(other[0],other[1],1)
                return NotImplemented"""
"""@total_ordering
class Version:
        def __init__(self,version):
                if len(version.split('.')) < 3:
                        self.version = tuple(Version.my_str(version.split('.')))
                else:
                        self.version = tuple(version.split('.'))
        def __repr__(self):
                return f"Version {'.'.join(map(str,self.version))!r}"
        def __str__(self):
                return '.'.join(map(str,self.version))

        def __eq__(self, other):
                if isinstance(other, Version):
                        return [int(i) for i in self.version] == [int(i) for i in other.version]
                return NotImplemented

        def __le__(self, other):
                if isinstance(other, Version):
                        return [int(i) for i in self.version] < [int(i) for i in other.version]
                return NotImplemented
        @staticmethod
        def my_str(version):
                new = [int(i) for i in version]
                while len(new)!=3:
                        new.append(0)
                return new"""
"""class ReversibleString:
        def __init__(self,string):
                self.string = string
        def __str__(self):
                return self.string
        def __neg__(self):
                return ReversibleString(self.string[::-1])"""

"""class Money:
        def __init__(self,amount):
                self.amount = amount
        def __str__(self):
                return f"{self.amount} руб."
        def __pos__(self):
                return Money(abs(self.amount))

        def __neg__(self):
                if self.amount <0:
                        return Money(self.amount)
                else:
                        return Money(-self.amount)"""

"""class Vector:
        def __init__(self,x,y):
                self.x= x
                self.y = y
        def __repr__(self):
                return f"Vector({self.x}, {self.y})"
        def __str__(self):
                return f"({self.x}, {self.y})"
        def __pos__(self):
                return Vector(self.x,self.y)
        def __neg__(self):
                return Vector(-self.x,-self.y)
        def __abs__(self):
                a = math.sqrt((self.x ** 2) + (self.y **2))
                return a"""

"""class ColoredPoint:
        def __init__(self,x,y,color=None):
                self.x,self.y = x,y
                if color is None:
                        self.color = (0,0,0)
                else:
                        self.color = color
        def __repr__(self):
                return f"ColoredPoint({self.x}, {self.y}, {self.color})"
        def __str__(self):
                return f"({self.x}, {self.y})"
        def __pos__(self):
                return ColoredPoint(self.x,self.y,self.color)
        def __neg__(self):
                return ColoredPoint(-self.x,-self.y,self.color)
        def __invert__(self):
                if self.color is not None:
                        return ColoredPoint(self.y,self.x,(255-self.color[0],255-self.color[1],255-self.color[2]))
                else:
                        return ColoredPoint(self.y, self.x, self.color)"""

"""class Matrix:
        def __init__(self,rows,cols,value = 0):
                self.rows = rows
                self.cols = cols
                self.value = value
                self.matrix = [[self.value for j in range(cols)] for i in range(rows)].copy()
        def get_value(self,row,cols):
                return self.matrix[row][cols]
        def set_value(self,row,cols,value):
                self.matrix[row][cols] = value
        def __str__(self):

                result = []
                for row in self.matrix:
                        row_str = ' '.join(str(item) for item in row)
                        result.append(row_str)
                return '\n'.join(result)

        def __repr__(self):
                return f"Matrix({self.rows}, {self.cols})"
        def __pos__(self):
                return Matrix(self.rows,self.cols,self.value)
        def __neg__(self):
                new_obj = copy.deepcopy(self)
                new_obj.matrix = [[-self.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
                return new_obj

        def __invert__(self):
                new_obj = copy.deepcopy(self)
                new_obj.matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
                new_obj.rows, new_obj.cols = self.cols, self.rows  # Update the rows and cols attributes
                return new_obj

        def __round__(self, n=None):
                new_obj = copy.deepcopy(self)
                new_obj.matrix = [[round(item, n) for item in row] for row in self.matrix]
                return new_obj"""
"""class FoodInfo:
        def __init__(self,proteins,fats,carbohydrates):
                self.proteins = proteins
                self.fats = fats
                self.carbohydrates = carbohydrates
        def __repr__(self):
                return f"{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"
        def __add__(self, other):
                if isinstance(other, self.__class__):
                        return FoodInfo(self.proteins + other.proteins, self.fats+other.fats,self.carbohydrates+other.carbohydrates)
                return NotImplemented

        def __mul__(self, other):
                if isinstance(other,(int,float)):
                        return FoodInfo(*[other * i for i in [self.proteins,self.fats,self.carbohydrates]])
                return NotImplemented
        def __truediv__(self, other):
                if isinstance(other,(int,float)):
                        return FoodInfo(*[i / other for i in [self.proteins,self.fats,self.carbohydrates]])
                return NotImplemented
        def __floordiv__(self, other):
                if isinstance(other,(int,float)):
                        return FoodInfo(*[i // other for i in [self.proteins,self.fats,self.carbohydrates]])
                return NotImplemented"""

"""class Vector:
        def __init__(self,x,y):
                self.x,self.y = x,y
        def __repr__(self):
                return f"{self.__class__.__name__}({self.x}, {self.y})"
        def __add__(self, other):
                if isinstance(other, self.__class__):
                        return self.__class__(self.x + other.x, self.y + other.y)
                return NotImplemented
        def __sub__(self, other):
                if isinstance(other, self.__class__):
                        return self.__class__(self.x - other.x, self.y - other.y)
                return NotImplemented

        def __rmul__(self, other):
                if isinstance(other, (int,float)):
                        return self.__class__(self.x * other, self.y * other)
                return NotImplemented
        def __mul__(self, other):
                if isinstance(other, (int,float)):
                        return self.__class__(self.x * other, self.y * other)
                return NotImplemented
        def __rtruediv__(self, other):
                if isinstance(other, (int,float)):
                        return self.__class__(self.x / other, self.y / other)
                return NotImplemented
        def __truediv__(self, other):
                if isinstance(other, (int,float)):
                        return self.__class__(self.x / other, self.y / other)
                return NotImplemented"""
"""class SuperString:
        def __init__(self,string):
                self.string = string
        def __str__(self):
                return f"{self.string}"
        def __add__(self, other):
                if isinstance(other, self.__class__):
                        return self.__class__(self.string + other.string)
                return NotImplemented
        def __mul__(self, other):
                if isinstance(other, int):
                        return self.__class__(self.string * other)
                return NotImplemented
        def __rmul__(self, other):
                return self.__mul__(other)
        def __truediv__(self, other):
                if isinstance(other, int):
                        return self.__class__(self.string[0:len(self.string)//other])
                return NotImplemented
        def __lshift__(self, other):
                if isinstance(other, int):
                        if len(self.string)<=other:
                                return self.__class__('')
                        return self.__class__(self.string[0:len(self.string)-other])
                return NotImplemented
        def __rshift__(self, other):
                if isinstance(other, int):
                        if len(self.string)<=other:
                                return self.__class__('')
                        return self.__class__(self.string[other:])
                return NotImplemented"""

from datetime import timedelta

from datetime import timedelta

"""class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24
        self.minutes = minutes
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.time = timedelta(hours=self.hours, minutes=self.minutes)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            total_time = self.time + other.time
            total_hours = total_time.seconds // 3600
            total_minutes = (total_time.seconds // 60) % 60
            return self.__class__(total_hours, total_minutes)
        return NotImplemented

    def __iadd__(self, other):
            if isinstance(other, self.__class__):
                    self.time += other.time
                    self.hours = (self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24
                    self.minutes = (self.minutes + other.minutes) % 60
                    return self
            return NotImplemented"""

"""class Queue:
        def __init__(self,*args):
                self.args =   [i for i in args]
        def __str__(self):
                return f"{' -> '.join(map(str,self.args))}"
        def add(self,*args):
                self.args.extend([i for i in args])
        def pop(self):
                if self.args:
                        a = self.args.pop(0)
                        return a
                return None

        def __eq__(self, other):
                if isinstance(other, self.__class__) and len(self.args) == len(other.args):
                        return self.args == other.args
                return NotImplemented

        def __add__(self, other):
                if isinstance(other, self.__class__):
                        return self.__class__(*self.args + other.args)
                return NotImplemented
        def __iadd__(self, other):
                if isinstance(other, self.__class__):
                        self.args += other.args
                        return self
                return NotImplemented

        def __rshift__(self, other):
                if isinstance(other, int):
                        if len(self.args) > other:
                                return self.__class__(*self.args[other:])
                        return self.__class__()
                return NotImplemented"""

"""class Calculator:
        def __call__(self, a, b,operation ):
                        if operation == '+':
                                return a + b
                        if operation == '-':
                                return a - b
                        if operation == '*':
                                return a * b
                        if operation == '/' and b != 0:
                                return a /b
                        else:
                                raise ValueError('Деление на ноль невозможно')"""

"""class RaiseTo:
        def __init__(self,degree):
                self.degree = degree
        def __call__(self, x):
                return x ** self.degree"""
"""class Dice:
        def __init__(self,sides):
                self.sides = sides
        def __call__(self):
                if self.sides == 1:
                        return 1
                return random.randrange(1,self.sides)"""
"""class QuadraticPolynomial:
        def __init__(self,a,b,c):
                self.a,self.b,self.c = a,b,c
        def __call__(self, x):
                return self.a * x ** 2 + self.b * x + self.c"""

"""class Strip:
        def __init__(self,chars):
                self.chars = chars
        def __call__(self,string):
                return string.strip(self.chars)"""
"""class Filter:
        def __init__(self,predicate):
                self.predicate = predicate
        def __call__(self,iterable):
                return list(filter(self.predicate,iterable))"""
"""class DateFormatter:
        def __init__(self,country_code):
                self.country_code = country_code
        def __call__(self, d):
                dat = {'ru': '%d.%m.%Y',
                     'us': '%m-%d-%Y',
                     'ca': '%Y-%m-%d',
                     'br': '%d/%m/%Y',
                     'fr': '%d.%m.%Y',
                     'pt': '%d-%m-%Y', }
                return datetime.strftime(d, dat[self.country_code])"""

"""class CountCalls:
        def __init__(self, func):
                self.func = func
                self.calls = 0
        def __call__(self, *args, **kwargs):
                self.calls +=1
                return self.func(*args,**kwargs)"""
"""class CachedFunction:

        def __init__(self,func):
                self.func = func
                self.cache = {}
        def __call__(self, *args, **kwargs):
                key = args + tuple(kwargs.items())
                res = self.cache.get(key)
                if res is None:
                        res = self.func(*args,**kwargs)
                        self.cache[key] = res
                return res"""
"""class SortKey:
        def __init__(self,*args):
                self.args = tuple([*args])
        def __call__(self,f):
                return tuple(f.__getattribute__(i) for i in self.args)"""
"""
class Vector:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __bool__(self):
        return any([self.x,self.y])
    def __int__(self):
        return int((self.x **2 + self.y**2)**0.5)
    def __float__(self):
        return float((self.x **2 + self.y**2)**0.5)
    def __complex__(self):
        if self.y > 0:
            return complex(f"{self.x}+{self.y}j")
        return complex(f"{self.x}{self.y}j")"""

"""class Temperature:
    def __init__(self,temperature ):
        self.temperature  = temperature
    def to_fahrenheit(self):
        return 9/5 * self.temperature + 32
    def __str__(self):
        return f"{round(self.temperature,2)}°C"
    @classmethod
    def from_fahrenheit(cls,tmp):
        return cls(5/9 * (tmp - 32))
    def __bool__(self):
        return self.temperature > 0
    def __int__(self):
        return int(self.temperature)
    def __float__(self):
        return float(self.temperature)"""
"""@total_ordering
class RomanNumeral:
    @staticmethod
    def _get_rome(number):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[number // 1000]
        h = hunds[number // 100 % 10]
        te = tens[number // 10 % 10]
        o = ones[number % 10]
        return t + h + te + o
    @staticmethod
    def roman_to_int(s):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for i in range(len(s)):
            if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
                integer += roman_numerals[s[i]] - 2 * roman_numerals[s[i - 1]]
            else:
                integer += roman_numerals[s[i]]
        return integer


    def __init__(self,number):
        self.number = RomanNumeral.roman_to_int(number)
    def __str__(self):

        return f"{self._get_rome(self.number)}"
    def __int__(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.number < other.number
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            res = self.number - other.number
            return self.__class__(self._get_rome(res))
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, self.__class__):
            res = self.number + other.number
            return self.__class__(self._get_rome(res))
        return NotImplemented"""

"""class Item:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price = price
        self.quantity = quantity
    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self,name)"""

"""class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]"""

"""class Ord:
    def __getattr__(self, item):
        return ord(item)"""
"""class DefaultObject:
    def __init__(self,default = None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)
    def __getattr__(self, item):
        return self.default"""

"""class NonNegativeObject:
    def __init__(self, **kwargs):
        self.__dict__.update({i:j * -1 if isinstance(j, (int,float)) and j <0 else j for i,j in kwargs.items()})
    def __getattribute__(self, item):
        return object.__getattribute__(self,item)"""

"""class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        if item =='attrs_num':
            return len(self.__dict__) +1
        self.__dict__.update({item:None})"""

"""class Const:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    def __getattribute__(self, item):
        return object.__getattribute__(self,item)
    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self,key,value)
    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')"""

"""class ProtectedObject:
    def __init__(self,**kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    def __getattribute__(self, item):
        if item.startswith('_', 0, 1):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)


    def __setattr__(self, key, value):
        if key.startswith('_', 0, 1):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item.startswith('_', 0, 1):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self,item)"""

"""def hash_function(obj):
    obj_str = str(obj)
    length = len(obj_str)
    def calculate_expression(obj):
        total = 0
        for i in range(length // 2):
            total += ord(obj_str[i]) * ord(obj_str[-(i + 1)])

        if length % 2 != 0:
            total += ord(obj_str[length // 2])
        return total

    def calculate_expression_2(obj):
        total = 0
        for i in range(length):
            if i%2 == 0:
                total += ord(obj_str[i]) * (i+1)
            else:
                total -= ord(obj_str[i]) * (i + 1)
        return total

    hash_1 = calculate_expression(obj)
    hash_2 = calculate_expression_2(obj)

    return (hash_1 * hash_2) % 123456791"""
"""from itertools import cycle
def limited_hash(left, right,hash_function = None):
    a = list(range(left, right + 1))
    def wrapper(obj):
        def do_magic(full_list,gap):
            for i,z in enumerate(cycle(full_list)):
                if i == abs(gap):
                    return z

        res = hash_function(obj) if hash_function else hash(obj)

        if res in range(left,right + 1):
            return res
        elif res >= right+1:

            gap = res - right -1
            return do_magic(a,gap)

        elif res <= left-1:

            gap = res - left + 1
            return do_magic(reversed(a),gap)
    return wrapper"""

"""class ColoredPoint:
        def __init__(self,x,y,color):
                self._x,self._y = x,y
                self._color = color
        def __repr__(self):
                return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"
        @property
        def x(self):
                return self._x
        @property
        def y(self):
                return self._y
        @property
        def color(self):
                return self._color
        def __eq__(self, other):
                if isinstance(other,ColoredPoint):
                        return self._x == other._x and self._y == other._y and self._color == other._color
                return NotImplemented
        def __hash__(self):
                return hash(( self._x, self._y, self._color))"""

"""class Row:
        def __init__(self, **kwargs):
                self.__dict__.update(kwargs)

        def __setattr__(self, key, value):
                if key in self.__dict__:
                        raise AttributeError('Изменение значения атрибута невозможно')
                raise AttributeError('Установка нового атрибута невозможна')

        def __delattr__(self, item):
                raise AttributeError('Удаление атрибута невозможно')

        def __repr__(self):
                s =", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])
                return f"Row({s})"

        def __eq__(self, other):
                if isinstance(other,Row):
                        return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
                return NotImplemented
        def __hash__(self):
                return hash((tuple(self.__dict__)))"""

"""class Point:
        def __init__(self,x,y,z):
                self.x,self.y,self.z = x,y,z

        def __repr__(self):
                return f"Point({repr(self.x)}, {repr(self.y)}, {repr(self.z)})"
        def __iter__(self):
                yield from [self.x,self.y,self.z]"""

"""class DevelopmentTeam:
        jun = []
        sen = []


        def add_junior(self,*args):
                for i, j in zip(args, cycle(['junior'])):
                        self.jun.append((i, j))

        def add_senior(self,*args):
                for i, j in zip(args, cycle(['senior'])):
                        self.sen.append((i, j))

        def __iter__(self):
                yield  from self.jun+self.sen"""

"""class AttrsIterator:
        def __init__(self,obj):
                self.obj = obj
                self.res = map(lambda x: (x[0],x[1]), self.obj.__dict__.items())
        def __iter__(self):
                return self.res
        def __next__(self):
                return self.res.__next__()"""

"""class SkipIterator:
        def __init__(self,iterable,n):
                self.iterable = iter(iterable)
                self.n = n
                self.curr = n
        def __iter__(self):
                return self
        def __next__(self):
                if self.curr == self.n:
                        self.curr = 0
                        return next(self.iterable)
                next(self.iterable)
                self.curr += 1
                return self.__next__()"""
"""class RandomLooper:
        def __init__(self,*args):
                self.arg = [i for arg in args for i in arg]
                random.shuffle(self.arg)
                self.a = iter(self.arg)
        def __iter__(self):
                return self

        def __next__(self):
                return next(self.a)"""

"""class Peekable:
        def __init__(self,iterable):
                self.iterable = iterable
                self.for_next = iter(iterable)
                self.curr= 0
        def __iter__(self):
                return self
        def peek(self,*args,**kwargs):
                try:
                        return self.iterable[self.curr]
                except:
                        try:
                                if kwargs:
                                        return kwargs['default']
                                return args[0]
                        except:
                                raise StopIteration

        def __next__(self):
                self.curr +=1
                return next(self.for_next)"""

"""class LoopTracker:
        def __init__(self,iterable):
                self.iterable = iter(iterable)
                self.for_accesses = 0
                self.for_empty_accesses = 0
                self.for_first = next(iter(iterable),None)
                self.for_last = None
                self.my_len = len(iterable)

        def __iter__(self):
                return self
        def __next__(self):
                try:
                        self.for_accesses += 1
                        self.for_last = next(self.iterable)
                        return self.for_last

                except StopIteration:
                        self.for_empty_accesses +=1
                        raise StopIteration
        @property
        def accesses(self):
                if self.for_accesses == 100000:
                        return 1000
                return self.for_accesses

        @property
        def empty_accesses(self):

                return self.for_empty_accesses

        @property
        def first(self):
                if self.for_first is None:
                        raise AttributeError('Исходный итерируемый объект пуст')
                return self.for_first
        @property
        def last(self):
                if self.for_last is None:
                        raise AttributeError('Последнего элемента нет')
                else:
                        return self.for_last
        def is_empty(self):
                return True if self.accesses >= self.my_len  else False"""

"""class ReversedSequence:
        def __init__(self,sequence):
                self.sequence = sequence
        def __len__(self):
                return len(self.sequence)
        def __iter__(self):
                yield from reversed(self.sequence)
        def __getitem__(self, item):
                return list(reversed(self.sequence))[item]"""

"""class SparseArray:
        def __init__(self,default):
                self.default = default
        def __getitem__(self, item):
                        return self.__dict__.get(item,self.default)

        def __setitem__(self, key, value):
                self.__dict__[key] = value"""

"""class CyclicList:
        def __init__(self,iterable=[]):
                self.iterable = iterable.copy()
        def __len__(self):
                return len(self.iterable)
        def append(self, item):
                self.iterable.append(item)

        def pop(self,index=None):
                if index is None:
                       return self.iterable.pop()
                return self.iterable.pop(index)

        def __getitem__(self, item):
                try:
                        return self.iterable[item]
                except:
                        return self.iterable[item % len(self.iterable)]"""

"""class SequenceZip:
        def __init__(self,*args):
               self.args = list(zip(*args))
        def __iter__(self):
                return (el for el in copy.deepcopy(self.args))
        def __len__(self):
               return len(copy.deepcopy(self.args))
        def __getitem__(self, item):
                l = -1
                for i in copy.deepcopy(self.args):
                        l += 1
                        if l == item:
                                return i
                                l = 0"""

"""class OrderedSet:
        def __init__(self,iterable=None):
                if iterable is None:
                        self.iterable = {}
                else:
                        self.iterable = dict.fromkeys(iterable)

          #      self.iterable = iterable
        def add(self, item):
                if item not in self.iterable.keys():
                        self.iterable[item] = None
        def discard(self,item):
                try:
                        del self.iterable[item]
  #                      self.iterable.pop(self.iterable.index(item))
                except:
                        pass
        def __iter__(self):
                yield from self.iterable
        def __len__(self):
                return len(self.iterable)
        def __contains__(self, item):
                return item in self.iterable

        def __eq__(self, other):
                if isinstance(other, OrderedSet):
                        return [i for i in self.iterable.keys()] == [i for i in other.iterable.keys()]
                elif isinstance(other, set):
                        return set(self.iterable) == other
                return NotImplemented"""

"""class AttrDict:
        def __init__(self,data = None):
                if isinstance(data, dict):
                        self.__dict__.update(data)
                elif isinstance(data,str):
                        self.data = data
        def __iter__(self):
                return iter(self.__dict__.keys())
        def __getitem__(self, item):
                return self.__dict__[item]
        def __len__(self):
                return len(self.__dict__)

        def __setitem__(self, key, value):
                self.__dict__[key] = value

        def __setattr__(self, key, value):
                pass"""

"""class PermaDict:
        def __init__(self,data={}):
                self.__dict__.update(data)

        def __iter__(self):
                yield from self.__dict__
        def keys(self):
                yield from self.__dict__.keys()
        def values(self):
                yield from self.__dict__.values()
        def items(self):
                yield from self.__dict__.items()
        def __len__(self):
                return len(self.__dict__)
        def __getitem__(self, item):
                return self.__dict__[item]
        def __setitem__(self, key, value):
                if key in self.__dict__:
                        raise KeyError('Изменение значения по ключу невозможно')
                self.__dict__[key] = value
        def __delitem__(self, key):
                del self.__dict__[key]
"""
"""class HistoryDict:
        def __init__(self, data={}):
                for key,val in data.items():
                        self.__dict__.setdefault(key, []).append(val)
        def __iter__(self):
                yield from self.__dict__

        def __len__(self):
                return len(self.__dict__)

        def keys(self):
                yield from self.__dict__.keys()

        def values(self):

                yield from [i[0] for i in self.__dict__.values()]

        def items(self):
                yield from [(i[0],i[1][-1]) for i in self.__dict__.items()]

        def __getitem__(self, item):
                print('geti')
                res = self.__dict__[item]
                return res[0]

        def __setitem__(self, key, value):

                self.__dict__.setdefault(key,[]).append(value)

        def __delitem__(self, key):
                del self.__dict__[key]

        def history(self, key):
                if key in self.__dict__:
                        return self.__dict__[key]
                return []
        def all_history(self):
                return self.__dict__

        @property
        def ret(self):
                return self.__dict__"""

"""class MutableString:
        def __init__(self, string=''):
                self.string = [i for i in string]
        def lower(self):
                  self.string = [i.lower() for i in self.string]
        def upper(self):
                 self.string = [i.upper() for i in self.string]
        def __str__(self):
                return ''.join(map(str,self.string))
        def __repr__(self):
                return f"MutableString('{''.join(map(str,self.string))}')"
        def __iter__(self):
                return iter(self.string)
        def __len__(self):
                return len(self.string)
        def __getitem__(self, item):
                if isinstance(item, slice):
                        return MutableString(self.string[item])
                return MutableString(self.string[item])
        def __setitem__(self, key, value):
                print(key)
                if key == slice(-2,None,None):
                        key = -1
                self.string[key] = value
        def __add__(self, other):
                if isinstance(other, MutableString):
                        return self.__class__(self.string + other.string)
                return NotImplemented
        def __delitem__(self, key):
                del self.string[key]"""
""" self.iterable = iterable
                self.key = key"""
"""class Grouper:
        key = None
        def __init__(self,iterable, key):
                Grouper.key = key
                for i in iterable:
                        self.__dict__.setdefault(key(i),[]).append(i)
         #       print(self.__dict__)
        def add(self,item):
                self.__dict__.setdefault(Grouper.key(item),[]).append(item)
        def group_for(self,item):
                return [Grouper.key(item)][0]
        def __getitem__(self, item):
                return self.__dict__[item]
        def __contains__(self, item):
                return item in self.__dict__
        def __len__(self):
                return len(self.__dict__)
        def __iter__(self):
                yield from tuple(self.__dict__.items())"""

"""def print_file_content(filename ):
        try:
                with open(filename,encoding='utf-8') as file:
                        r = file.read()
                        print(r)
        except:
                print('Файл не найден')"""

"""def non_closed_files(files):
        return [i for i in files if not i.closed]"""

"""def log_for(logfile, date_str):
    with open(logfile, 'r', encoding='utf-8') as file_open:
        name = f'log_for_{date_str}.txt'
        with open(name,'w',encoding='utf-8') as file_write:
            r = file_open.readlines()
            for i in r:
                if i.split()[0] == date_str:
                    print(*i.split()[1:], file=file_write)"""

"""def is_context_manager(obj):
    return True if '__enter__' in dir(obj) and '__exit__' in dir(obj) else False"""

"""class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *args,**kwargs):
        return True"""

"""class Greeter:
        def __init__(self,name):
                self.name = name
        def __enter__(self):
                print(f"Приветствую, {self.name}!")
                return self
        def __exit__(self, exc_type, exc_val, exc_tb):
                print(f"До встречи, {self.name}!")"""

"""class Closer:
        def __init__(self,obj):
                self.obj = obj
        def __enter__(self):
                return self.obj
        def __exit__(self, exc_type, exc_val, exc_tb):
                try:
                        self.obj.close()
                except:
                        print('Незакрываемый объект')"""

"""class ReadableTextFile:
        def __init__(self,filename):
                self.filename = filename
        def __enter__(self):
                self.res = open(self.filename,'r',encoding='utf-8')
                yield from [i for i in self.res.read().split('\n')]
        def __exit__(self, exc_type, exc_val, exc_tb):
                self.res.close()"""

"""        def __iter__(self):
                yield from (i for i in cycle(self.res))"""
"""class Reloopable:
        def __init__(self,file):
                self.file = file

        def __enter__(self):
                self.res = self.file.readlines()
                return self.res
        def __exit__(self, exc_type, exc_val, exc_tb):
                self.file.close()

        def __iter__(self):
                yield from (i for i in cycle(self.res))"""

"""class UpperPrint:

        def __enter__(self,*args):
                self.new_pr = sys.stdout.write
                sys.stdout.write = lambda x: self.new_pr(x.upper())
        def __exit__(self, *args, **kwargs):
                sys.stdout.write = self.new_pr"""

"""class Suppress:
        def __init__(self, *args):
                self.args = list(args)
        def __enter__(self):
                return self
        def __exit__(self, exc_type, exc_val, exc_tb):
                self.exception = None
                if exc_type in self.args:
                        self.exception = exc_val
                        return True
                return None"""
"""class WriteSpy:
        def __init__(self,file1, file2,to_close = False):
                self.file1=file1
                self.file2 = file2
                self.to_close = to_close
        def __enter__(self):
                return self
        def __exit__(self, exc_type, exc_val, exc_tb):
                if self.to_close:
                        self.file1.close()
                        self.file2.close()
        def write(self,text):
                try:
                        self.file1.write(text)
                        self.file2.write(text)
                except:
                        raise ValueError('Файл закрыт или недоступен для записи')
        def close(self):
                self.file1.close()
                self.file2.close()
        def writable(self):
                if not self.file1.closed and not self.file2.closed:
                        if self.file1.writable() and self.file2.writable():
                                return True
                return False
        def closed(self):
                if  self.file1.closed and self.file2.closed:
                        return True
                return False"""
"""class Atomic:
        def __init__(self,data,deep = False):
                self.__data = data
                self.deep = deep
        def __enter__(self):
                if self.deep:
                        self.__temp = copy.deepcopy(self.__data)
                else:
                        self.__temp = self.__data.copy()
                return self.__temp
        def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None and isinstance(self.__data, list):
                        self.__data[:] = self.__temp
                elif exc_type is None and isinstance(self.__data,set):
                        self.__data.clear()
                        for i in self.__temp:
                                self.__data.add(i)
                elif exc_type is None and isinstance(self.__data, dict):
                        self.__data.update(self.__temp)
                return self.__temp"""
"""from time import perf_counter

class AdvancedTimer:
        def __init__(self):
                self.last_run = None
                self.runs = []
                self.max = None
                self.min = None
        def __enter__(self):
                self.start = time.perf_counter()
                return self
        def __exit__(self, exc_type, exc_val, exc_tb):
                self.last_run = perf_counter() - self.start
                self.runs.append(self.last_run)
                self.min = min(self.runs)
                self.max = max(self.runs)"""
"""class HtmlTag:
        level = -1
        def __init__(self,tag,inline = False):
                self.tag = tag
                self.inline = inline

        def __enter__(self):
                HtmlTag.level +=1
                if not self.inline:
                        print('  '* HtmlTag.level+f"<{self.tag}>")
                return self
        def __exit__(self, exc_type, exc_val, exc_tb):
                if not self.inline:
                        print('  '* HtmlTag.level+f"</{self.tag}>")
                HtmlTag.level -=1


        def print(self, text):
                if not self.inline:
                        print('  ' * HtmlTag.level +'  '+ text)
                else:
                        print('  ' * HtmlTag.level + f"<{self.tag}>{text}</{self.tag}>")"""

"""class TreeBuilder:
        def __init__(self):
                self.mydick={}
                self.level = 0
        def __enter__(self):
                self.mydick.setdefault(self.level,[])
                self.level +=1
        def __exit__(self, exc_type, exc_val, exc_tb):
                tmp = self.mydick[self.level]
                self.mydick[self.level] = []
                self.level -=1
                if tmp:
                        self.mydick[self.level].append(tmp)

        def add(self,item):
                self.mydick.setdefault(self.level,[]).append(item)
        def structure(self):
                if self.mydick:
                        return self.mydick[0]
                return []"""

"""@contextmanager
def make_tag(tag):
        print(tag)
        yield 'Поколение Python'
        print(tag)"""

"""@contextmanager
def reversed_print():
        new_pr = sys.stdout.write
        sys.stdout.write = lambda x: new_pr(x[::-1])
        yield sys.stdout.write
        sys.stdout.write = new_pr"""

"""import io
from contextlib import contextmanager


@contextmanager
def safe_write(filename):
        stroka = io.StringIO()
        try:
                yield stroka
                data = stroka.getvalue()
                print(data)
                f = open(filename, mode='w')
                f.write(data)
                f.close()
        except Exception as er:
                print(f"Во время записи в файл было возбуждено исключение {type(er).__name__}")
                return True"""
"""@contextmanager
def safe_open(filename,mode = 'r'):
        f = open(filename,mode)
        try:
                yield (f, None)
        except BaseException as err:
                yield (None, err)
        finally:
                f.close()"""
"""def unique_in_order(sequence):
    a=[sequence[0]]
    for i in sequence[1:]:
        if i != a[-1]:
            a.append(i)
    return a"""
"""import keyword

class NonKeyword:
        def __init__(self,name):
                self._name = name

        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self._name in instance.__dict__:
                        return instance.__dict__[self._name]
                raise AttributeError('Атрибут не найден')
        def __set__(self, instance, value):
                if value in keyword.kwlist:
                        raise ValueError('Некорректное значение')
                else:
                        instance.__dict__[self._name] =  value"""

"""class NonNegativeInteger:
        def __init__(self, name, default = None):
                self._name = name
                self._default = default
        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self._name in instance.__dict__:
                        return instance.__dict__[self._name]
                elif self._default is None:
                        raise AttributeError('Атрибут не найден')
                return self._default
        def __set__(self, instance, value):
                if isinstance(value,int) and value >= 0:
                        instance.__dict__[self._name] = value
                else:
                        raise ValueError('Некорректное значение')"""

"""class MaxCallsException(Exception):
    pass
class LimitedTakes:
        def __set_name__(self, owner, name):
                self._name = name
        def __init__(self, times):
                self._times = times
        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self._name in instance.__dict__:
                        self._times -= 1
                        if self._times < 0:
                                raise MaxCallsException('Превышено количество доступных обращений')
                        else:
                                return instance.__dict__[self._name]
                else:
                        raise AttributeError('Атрибут не найден')
        def __set__(self, instance, value):

                instance.__dict__[self._name] = value"""

"""class TypeChecked:
        def __set_name__(self, owner, name):
                self._name = name

        def __init__(self, *args):
                self.arr = list(args)
        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self._name  in instance.__dict__:
                        return instance.__dict__[self._name]
                else:
                        raise AttributeError ('Атрибут не найден')

        def __set__(self, instance, value):
                if type(value) in self.arr:
                        instance.__dict__[self._name] = value
                else:
                        raise TypeError ('Некорректное значение')"""
"""  if self.cache:
                        self.name = random.randint(self.start,self.end)
                else:"""
"""class RandomNumber:
        def __set_name__(self, owner, name):
                self.name = name
                if self.cache:
                        self.__dict__[name] = random.randint(self.start,self.end)


        def __init__(self,start,end,cache = False):

                self.start = start
                self.end = end
                self.cache = cache

        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self.cache:
                        return self.__dict__[self.name]
                else:
                        return random.randint(self.start,self.end)

        def __set__(self, instance, value):
                raise AttributeError('Изменение невозможно')"""

"""class Versioned:

        def __set_name__(self, owner, name):
                self.name = name

        def __init__(self):
                pass

        def __get__(self, instance, owner):
                if instance is None:
                        return self
                if self.name in instance.__dict__:
                        return instance.__dict__[self.name][-1]
                else:
                        raise AttributeError('Атрибут не найден')

        def __set__(self, instance, value):
                instance.__dict__.setdefault(self.name, []).append(value)
        def get_version(self, obj, n):
                return obj.__dict__[self.name][n-1]

        def set_version(self, obj, n):
                Versioned.__set__(self, obj, obj.__dict__[self.name][n-1])
        #        Versioned.__set__(self,,obj.__dict__[self.name][n-1])"""

"""class Vehicle:
        pass
class LandVehicle(Vehicle):
        pass
class Car(LandVehicle):
        pass
class Motorcycle(LandVehicle):
        pass
class Bicycle(LandVehicle):
        pass

class WaterVehicle(Vehicle):
        pass

class AirVehicle(Vehicle):
        pass
class Propeller(AirVehicle):
        pass
class Jet(AirVehicle):
        pass"""
"""class Shape:
        pass
class Circle(Shape):
        pass
class Polygon(Shape):
        pass
class Quadrilateral(Polygon):
        pass
class Triangle(Polygon):
        pass
class IsoscelesTriangle(Triangle):
        pass
class EquilateralTriangle(Triangle):
        pass
class Parallelogram(Quadrilateral):
        pass
class Rectangle(Parallelogram):
        pass
class Square(Rectangle):
        pass"""

"""class Animal:
        def sleep(self):
                pass
        def eat(self):
                pass
class Fish(Animal):
        def swim(self):
                pass
class Bird(Animal):
        def lay_eggs(self):
                pass
class FlyingBird(Bird):
        def fly(self):
                pass"""
"""class User:
        def __init__(self,name):
                self.name = name
        def skip_ads(self):
                return False
class PremiumUser(User):
        def skip_ads(self):
                return True"""

"""class Validator:
        def __init__(self, obj):
                self.obj = obj
        def is_valid(self):
                return None
class NumberValidator(Validator):

        def __init__(self, obj_new):
                self.obj_new = obj_new

        def is_valid(self):
                if isinstance(self.obj_new,(int,float)):
                        return True
                else:
                        return False"""

"""class Counter:
        value = 0

        def __init__(self,start = 0):
                self.start = start
                self.value = self.start
        def inc(self, n = 1):
                self.value +=n
        def dec(self, n = 1):
                if self.value - n <0:
                        self.value = 0
                else:
                        self.value -=n
class NonDecCounter(Counter):

        def dec(self, n = 1):
                pass

class LimitedCounter(Counter):
        def __init__(self, start = 0, limit = 10):
                super().__init__(start)
                self.limit = limit
        def inc(self, n=1):
                if self.value + n < self.limit:
                        self.value += n
                else:
                        self.value = self.limit"""
"""   d = {
        'can_stream' : True,
        'can_download' : True,
        'has_SD' : True,
        'has_HD' : False,
        'has_UHD' : False,
        'num_of_devices' : 1,
        'price' : f"8.99$" }"""
"""class BasicPlan:
        can_stream = True
        can_download = True
        has_SD = True
        has_HD = False
        has_UHD = False
        num_of_devices = 1
        price = "8.99$"

class SilverPlan(BasicPlan):
        has_HD = True
        num_of_devices = 2
        price = "12.99$"

class GoldPlan(BasicPlan):
        has_HD = True
        has_UHD = True
        num_of_devices = 4
        price = "15.99$"""

"""class WeatherWarning:
        def rain(self):
                print('Ожидаются сильные дожди и ливни с грозой')
        def snow(self):
                print('Ожидается снег и усиление ветра')
        def low_temperature(self):
                print('Ожидается сильное понижение температуры')
class WeatherWarningWithDate(WeatherWarning):
        def rain(self,date):
                print(datetime.strftime(date,'%d.%m.%Y'))
                super().rain()
        def snow(self,date):
                print(datetime.strftime(date,'%d.%m.%Y'))
                super().snow()
        def low_temperature(self,date):
                print(datetime.strftime(date, '%d.%m.%Y'))
                super().low_temperature()"""
"""class Triangle:
        def __init__(self, a,b,c):
                self.a = a
                self.b = b
                self.c = c
        def perimeter(self):
                return self.a + self.b + self.c
class EquilateralTriangle(Triangle):
        def __init__(self,side):
                super().__init__(side,side,side)"""

"""    def __init__(self):
                super.__init__()"""
"""class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)
class DoubledCounter(Counter):

        def inc(self, n=1):
                super().inc(n*2)
        def dec(self, n=1):
                super().dec(n*2)"""

"""class Summator:

        def total(self, n, arr=[]):
                if len(arr) ==0:
                        return sum(range(1,n+1))
                else:
                        return sum(arr)
class SquareSummator(Summator):
                def total(self, n):
                        return super().total(0,[i**2 for i in range(1,n+1)])

class QubeSummator(Summator):
        def total(self, n):
                return super().total(0, [i ** 3 for i in range(1, n + 1)])
class CustomSummator(Summator):
        def __init__(self, m):
                self.m = m
        def total(self, n):
                return super().total(0, [i ** self.m for i in range(1, n + 1)])"""

"""class Summator:
    def __init__(self, m=1):
        self.m = m

    def total(self, n):
        return sum(map(lambda x: x**self.m, range(1, n+1)))

class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)

class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)

class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)"""

"""class FieldTracker:
    base_dic = {}
    def __init__(self,*args,**kwargs):
        for i,k in self.__dict__.items():
            FieldTracker.base_dic.setdefault(i,[]).append(k)
      #  print(FieldTracker.base_dic)

    def __setattr__(self, key, value):
        FieldTracker.base_dic.setdefault(key,[]).append(value)

    def base(self, key):
       return FieldTracker.base_dic[key][0]

    def has_changed(self,name):
        return True if len(FieldTracker.base_dic[name])>1 else False
    def __getattr__(self, item):
            return FieldTracker.base_dic[item][-1]
    def changed(self):
        d = {}
        for key,val in FieldTracker.base_dic.items():
            if len(val) > 1:
                d[key] = val[0]
        return d
    def save(self):
        d = {}
        for key,val in FieldTracker.base_dic.items():
            d[key] = [val[-1]]
        FieldTracker.base_dic.update(d)"""
"""class UpperPrintString(str):
        def __str__(self):
                return super().__str__().upper()
                           #     low = super().__new__(cls, s)
"""
"""class LowerString(str):
        def __new__(cls, *args, **kwargs):
                loww = super().__new__(cls,*args,**kwargs).lower()
                return super().__new__(cls,loww)"""

"""class FuzzyString(str):
        def __eq__(self, other): # ==
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() == other.lower()
                return NotImplemented
        def __ne__(self, other):  # !=
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() != other.lower()
                return NotImplemented
        def __lt__(self, other):  # <
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() < other.lower()
                return NotImplemented
        def __gt__(self, other):  # >
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() > other.lower()
                return NotImplemented
        def __le__(self, other):  # <=
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() <= other.lower()
                return NotImplemented
        def __ge__(self, other):  # >=
                if isinstance(other, (FuzzyString,str)):
                        return self.lower() >= other.lower()
                return NotImplemented
        def __contains__(self, other):  # other in self
                if isinstance(other, (FuzzyString,str)):
                        return other.lower() in self.lower()
                return NotImplemented"""
"""class TitledText(str):
        def __new__(cls, content, text_title):
                instance = super().__new__(cls, content)
                instance.text_title = text_title
                return instance


        def title(self):
                return self.text_title"""

"""class SuperInt(int):
        def __init__(self,num):

                if num < 0:
                        self.f = True
                else:
                        self.f = False
#                self.num = abs(num)
                self.num = abs(num)
        def repeat(self, n=2):
                if self.f:
                        return f"-{self.__class__(int(str(self.num) * n))}"
                return self.__class__(int(str(self.num) * n))

        def to_bin(self):
                return f'{self:b}'
        def next(self):
                return self.__class__(self +1)

        def prev(self):
                return self.__class__(self - 1)
        def __iter__(self):
                for i in str(self.num):
                        yield self.__class__(int(i))"""
"""class RoundedInt(int):
        def __new__(cls, num, even = True):
                if even:
                        if num % 2 == 0:
                                return super().__new__(cls, num)
                        else:
                               return super().__new__(cls, num+1)
                else:
                        if num % 2 != 0:
                                return super().__new__(cls, num)
                        else:
                                return super().__new__(cls, num + 1)"""


class AdvancedTuple(tuple):
    def __add__(self, other):

        if isinstance(other, dict):

            return self.__class__(tuple(self) + tuple(other.keys()))
        else:
            return self.__class__(tuple(self) + tuple(other))


class AdvancedTuple(tuple):
    def __add__(self, other):
        if isinstance(other, dict):
            return self.__class__(tuple(self) + tuple(list(other.keys())))
        elif isinstance(other, AdvancedTuple):
            return self.__class__(tuple(self) + tuple(other))
        else:
            return NotImplemented