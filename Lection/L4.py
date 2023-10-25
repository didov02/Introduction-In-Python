#използване на декоратор
def spam(n): # дефиниране на функция spam
    spams = ("spam", ) * (n - 1)
    return "I would like {} and spam".format(", ".join(spams))


def eggs(n): # дефиниране на фунцкия eggs
    return "I would like {} eggs".format(n)


def served_by(func, server): # дефиниране на декоратора, който приема функция и обръщение
    def cached_server(n):
        return "{}, dear {}".format(func(n), server)
    return cached_server


eggs = served_by(eggs, "sir") # предефиниране на функцията eggs с добавяне на обръщение
spam = served_by(spam, "sir") # предефиниране на фунцкията spam с добавяне на обръщение

print(eggs(10)) # принтиране на функцията eggs с 10 яйца
print(spam(10)) # принтиране на функцията spam с 10 пъти написано spam


def memoize(func): # декоратор, който пази dict с информация относно предишните промени, които са се осъществили
    memory = {}
    def memoized(*args):
        if args in memory:
            return memory[args]
        result = func(*args)
        memory[args] = result
        return result
    return memoized

#1
def fibonacci(x): # тази версия на фибоначи е много бавна
    if x in (0, 1):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

fibonacci = memoize(fibonacci)


# Е същото като

#2
@memoize
def fibonacci(x):
    if x in (0, 1):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

print(fibonacci(10))

# Още един пример
def notifyme(f):
    def logged(*args, **kwargs):
        print(f.__name__, ' called with ', args, ' and ', kwargs)
        return f(*args, **kwargs)
    return logged

@notifyme
def square(x):
    return x * x

result = square(25)
print(result)

# обединение на примерите

def served_by(server):
    def decorator(func):
        def cached_server(n):
            return "{}, dear {}".format(func(n), server)
        return cached_server
    return decorator


def thank_you(func):
    def with_thanks(n):
        return "{}. Thank you very much!".format(func(n))
    return with_thanks


@served_by("sir")
def spam(n):
    spams = ("spam",) * (n - 1)
    return "I would like {} and spam".format(", ".join(spams))

@thank_you
@served_by("sir")
def eggs(n):
    return "I would like {} eggs".format(n)

print(eggs(10))



