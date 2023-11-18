import math # вкарване на библиотека

def addition(a, b):
     return Vector(a.x + b.x, a.y + b.y)

class Vector: # създаване на клас

    _count = 0 # създаване на protected променлива

    def __init__(self, x, y): # добавяне на инициализатор
         self.x = x # задаване на стойности
         self.y = y

    def length(self): # създаване на метод
         return math.sqrt(self.x**2 + self.y**2)
    
    def _coords(self): # създаване на protected метод
         return (self.x, self.y) 
    
    def __diference(self): # създаване на private метод
         return self.x - self.y
    
    def normalize(self): # mutation method
         length = self.length()
         self.x /= length
         self.y /= length

    def normalized(self): # non - mutating method
         length = self.length()
         return Vector(self.x / length, self.y / length)
    
    def __eq__(self, other):
         return self.x == other.x and self.y == other.y
    
    def __call__(self, name):
         print(f"This vector name is {name}")

    @staticmethod # създаване на статичен метод
    def check_len(numbers):
         if len(numbers) != 2:
              print("error")

    @classmethod # създаване на класови метод
    def increase_count(cls):
         cls._count += 1

    @classmethod
    def decrease_count(cls):
         cls._count -= 1

    def __del__(self): # създаване на констурктор
         type(self).decrease_count

    @property # създаване на метод, който да се държи като property
    def length2(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # променяне на стойност на метод, който се преструва на атрибут
    @property
    def get_x(self):
         return self.x

    @get_x.setter
    def get_x(self, value):
         self.x = value

    __add__ = addition # дефиниране на класова функция като външна функция

spam = Vector(1,1) # създаване на инстанция на класа

print(spam.x) # взимане на дадена променлива
print(spam.length()) # използване на метод на клас

x = getattr(spam,'x') # използване на get-ър
print(x)

setattr(spam, 'x', 2) # използване на set-ър
x = getattr(spam, 'x')
print(x)