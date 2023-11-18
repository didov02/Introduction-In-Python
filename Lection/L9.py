# iterable -> __iter__
# iterator -> __next__

answers = ['a','a','b','c','d']

for answer in answers:
    print(answer) # a a b c d, и можем в следващ цикъл отново да ги принтираме използвайки iterable

# какво всъщност прави for
iterator = iter(answers)
try:
    while True:
        answer = next(iterator)
        print(answer)
except StopIteration:
    pass

answers_iterator = iter(answers)
print(answers_iterator) # returns address
print(next(answers_iterator)) # a
print(next(answers_iterator)) # a
print(next(answers_iterator)) # b
print(next(answers_iterator)) # c
print(next(answers_iterator)) # d
print(next(answers_iterator)) # will return an error

# заради мързеливостта си използвайки iterator можем да направим следното нещо
# в случай, че все още не сме обходили answers
answers[0] = 'e'
print(next(answers_iterator)) # e, вместо a

# Пример при работа с клас
class Squarer:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if self.num <= self.max:
            result = self.num ** 2
            self.num += 1
            return result
        else:
            raise StopIteration
        

numbers = Squarer(3)
squares_iter = iter(numbers)

print(next(squares_iter)) # 0
print(next(squares_iter)) # 1
print(next(squares_iter)) # 4
print(next(squares_iter)) # 9
print(next(squares_iter)) # error

class Squarer2:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        result = self.num ** 2
        self.num += 1
        return result 
    
    __call__ = __next__


numbers2 = iter(Squarer2(1), 100) # задаваме до кое число да работи
for n in numbers:
    print(n) # 1 4 9 16 25 36 49 64 81

# използвайки yield можем да създадем функция, която извършва същата дейност като Squarer2

def squarer3(start, limit):
    current = start
    while current ** 2 < limit:
        yield current ** 2
        current += 1

numbers3 = squarer3(1, 100)
for n in numbers:
    print(n) # 1 4 9 16 25 36 49 64 81

# enumerate 
neccessities = ['Beer', 'Football']
for index, necessity in enumerate(neccessities, 1):
    print(f'{index}.{necessity}')

# 1. Beer
# 2. Football

# използване на zip & zip_longest
from itertools import zip_longest

numbers4 = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)

zipped_normal = zip(numbers, letters, longest)
zipped_longest = zip_longest(numbers, letters, longest, fillvalue='?')

print(zipped_normal)
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2)]
print(zipped_longest)
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

# използване на itertools.accumulate
from itertools import accumulate
sums = accumulate(range(1, 101), lambda a, b: a + b)
print(sums)
# <itertools.accumulate object at 0x1076d27c0>
print(next(sums))
# 1
print(next(sums))
# 3
print(list(sums))
# [6, 10, 15, ..., 4950, 5050]

# използване на itertools.cycle
from itertools import cycle
final_grading_system = cycle([3, 4, 5, 6])
for i in final_grading_system:
    print(i)
# 3
# 4
# 5
# 6
# 3
# 4
# 5
# ...

# използване на itertools.count
from itertools import count
i = iter(count(firstval=5, step=3))
print(next(i)) # 5
print(next(i)) # 8
print(next(i)) # 11
# ...

# използване на itertools.repeat
from itertools import repeat
print(list(repeat('Берое!', 3)))
# ['Берое!', 'Берое!', 'Берое!']
