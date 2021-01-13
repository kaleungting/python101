# CLASS
# INSTANCES

class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')

    @classmethod  # class methods means you can do it on the Class and would not need to instantiate it
    # whereas instance method, you put self as the arg, classmethods need to put CLS
    def adding_things(cls, num1, num2):
        return cls("Tom", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Sam", 29)
player2 = PlayerCharacter("Ken", 27)

print(player1.run().run().run())
# since adding_things is a class method, i can just call it on PlayerCharacter
player3 = (PlayerCharacter.adding_things(2, 3))
print(player3._age)

#FOUR PILLARS OF OBJECT ORIENTED PROGRAMMING
#ENCAPSULATION - binding of data and functions that manipulate the data
#ABSTRACTION - hiding of information and only giving access to the info that needs
    #public and private variables
    #NO TRUE PRIVACY IN PYTHON
    #use underscore before variables to indicate that the variables should not be modified
#INHERITANCE - objects take on existing property of other objects
#POLYMORPHISM - different object classes and have different names - ability to redefine methods
