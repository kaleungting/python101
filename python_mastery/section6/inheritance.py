class User():

    def __init__(self, name):
        self.name = name

    def sign_in(self):
        print("You are logged in")


class Wizard(User):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def attack(self):
        print(f'{self.name} has magical powers of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        super().__init__(name)
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} has {self.arrows} arrows in his quiver.')


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

print(wizard1.name)
print(archer1.name)

#isinstance(instance, Class)

# print(isinstance(wizard1, Wizard))  # True
# print(isinstance(wizard1, User))  # True

#super().__init__(name, email) - gives the children class access to attributes