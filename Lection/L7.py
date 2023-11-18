from typing import Any


class Statue: # създаване на клас
    def __init__(self): # създаване на инициализатор
        self.left_hand = "Generic left hand."
        self.right_hand = "Generic right hand."


venus_de_milo = Statue() 
print(f"I have {venus_de_milo.left_hand} and {venus_de_milo.right_hand}")
del venus_de_milo.left_hand # премахване на атрибута лява ръка
print(venus_de_milo.left_hand) # опитът ще бъде неуспешен

class FirstHand:

    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'

    def __getitem__(self, index): # по този начин класът ни поддържа достъп от вида object[index]
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    def __setitem__(self, index, value): # работи по обратния на __getitem__ начин
        if index == 0:
            self.thumb = value
        elif index == 1:
            self.index_finger = value
        else: # и така присвояваме и за останалите
            print("Others")

    def __getattr__(self, name): # механизъм, чрез който ако търсен атрибут не съществува се връща тази функция
        return f"Това е ръка v1.0. Все още няма {name}."
    
    def __setattr__ (self, name, value): 
        print(f"Нова стойност за {name} - {value}")
        object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        print(f"Някой ми бърка по пръстите и иска {name}")
        return object.__getattribute__(self, name)


hand = FirstHand() 
print(hand.middle_finger) 
print(hand[4]) # заради __getitem__ това работи
hand[1] = 'кебапче' # заради __setitem__ това работи
print(hand.sixth_finger) # ще задейства __getattr__
print(hand.pinkie) # ще задейства __getattribute__
print(hand.__dict__) # връща речник съдържащ атрибутите на обекта 
print(hand.__class__) # връзка към класа на обекта

class Limb:

    name = "Limb"

    def __init__(self, name):
        print("Executing parent constructor.")
        self.name = name

    def introduce(self):
        return f"I am a {self.name}"
    

class Hand(Limb): # наследяване

    name = "Hand" # присвояване на стойности на класа родител

    def __init__(self,name):
        super().__init__(name) # извикване на конструктора на родителя
        print("Executing child constructor.") 
        self.name = name

    def introduce(self): # overriding
        return f"I am THE {self.name}"