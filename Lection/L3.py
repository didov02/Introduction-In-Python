my_favourite_things = ['spam']*100
print(my_favourite_things) # print spam 100 times

numbers = set() # create set
numbers.add(5) # add number to set
numbers.add(4)
numbers.add(3)
numbers.discard(4) # remove number(if number isn't there, there won't be any error)
numbers.discard(4) # remove number(if number isn't there, there will be an error)
numbers.remove(3)
print(numbers)

if 4 in numbers: # check if number is available
    print('number is here.')
else:
    print('number is not here.')

numbers2 = {31,23,534,923} # create set with some numbers
print(numbers2)

numbers3 = [1,3,2,3,4,5,1,2,9,2,4,8,7]
print(set(numbers3)) # prints only the unique numbers

age = {   
    'John' : 43,
    'Betty' : 29,
    'Rose' : 19,
    'Dean' : 20,
} # create dict

print(age) # print dict
print(age['John']) # print value by key from dict

for person in age: 
    print(f"{person} is {age[person]}s old") # print key and value

age['Tony'] = 15 # add to dict

print(age['Tony'])

age2 = [('Tiffany',30),('Oliver',25),('Anton',25),('Peter',26)] # create dict (another way)

age3 = {} # create empty dict

for person,age in age2:
    if age == int(25):
        age3[person] = ['Wanted']
    else:
        age3[person] = ['Not wanted']


print(age3)

# usage of map
def double(x):
    return x * 2

numbers4 = [1,2,3,4,5]
result = map(double,numbers4)
double_numbers = list(result)
print(double_numbers)

# usage of filter
def even(x):
    return x % 2 == 0

numbers5 = [1,2,3,4,5,6,7]
result = filter(even,numbers5)
even_numbers=list(result)
print(even_numbers) 

# list comprehension
print([x * x for x in range(1,6)])
print([x for x in range(1,8) if x % 2 == 0])

# generator expression -> same idea but [] becomes ()

# set comprehension
print({x*x for x in range(0,10)})

# dict comprehension
print({i: chr(65 + i) for i in range(10)})

