class MadWifeException(Exception):
    """Exception raised by a mad wife."""

    def __init__(self, message = 'Ядоасана съм и ти си знаеш защо'):
        self._message = message
        super.__init__(self._message)

    def __str__(self):
        return f'Глупак, простак, мръсник, циник! {self._message}'


#raise MadWifeException() -> Ядосана съм ти и ти си знаеш защо
#raise MadWifeException('Вече не ме обичаш!') -> Вече не ме обичаш!

# ако извикаме MadWifeException() след създаването на __str__
#raise MadWifeException() -> Глупак, простак, мръсник, циник! Ядоасана съм и ти си знаеш защо

def homework(text):
    try:
        return text.split()
    except AttributeError:
        return None
    
print(homework(666)) # None

def homework(text):
    return text.split()

print(homework(666)) # AttributeError : 'int' object has no attribute 'split'

src = 'source.txt'
target = 'target.txt'

# Да опитаме да обърнем реда на редовете на файл
try:
    source_file = open(src, 'r') # src is file
    buffer = []
    try:
        buffer = source_file.readlines()
    finally:
        source_file.close()
    target_file = open(target, 'w') # target is file
    try:
        for line in reversed(buffer):
            target_file.write(line)
    finally:
        target_file.close()
except IOError:
    print("Something bad happend.")


# друг начин за извършване на действието е:
try:
    with open(src) as source_file:
        buffer = source_file.readlines()
    with open(target) as target_file:
        for line in reversed(buffer):
            target_file.write(line)
except IOError:
    print('Something went wrong')

# with гарантира, че файлът ще бъде затворен автоматично

class Recipient:
    def __init__(self, name):
        self.name = name

    def await_response(self):
        return f'Тук {self.name}. Прието. Край.'
    

class AlloAlloConversation:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Ало-ало, тук {self.name}.')
        return Recipient("Лондон")
    
    def __exit__(self, type, value, traceback):
        print('И точка.')

class AlloAlloMessage:
    def __init__(self, recipient_name):
        self.recipient_name = recipient_name

    def __enter__(self):
        print(f'{self.recipient_name},'
              'предавам закодирано съобщение:')
        
    def __exit__(self, type, value, traceback):
        print('Край.')


with AlloAlloConversation("Нощен ястреб") as recipient: # Ало-ало, тук Нощен ястрб
    with AlloAlloMessage(recipient.name): # Лондон, предавам закодирано съобщение:
        print('Английските летци са на лекция във ФМИ.') 
    print(recipient.await_response()) # Край \n Тук Лондон. Прието. Край.
    with AlloAlloMessage(recipient.name): # Лондон, предавам закодирано съобщение:
        print('Никой от тях не е гледал сериала и не разбират за какво говоря.')
# Край
# И точка.
