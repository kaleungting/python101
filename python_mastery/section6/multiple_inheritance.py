class User():

    def __init__(self, name):
        self.name = name

    def sign_in(self):
        print("You are logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} has magical powers of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.name} has {self.arrows} arrows in his quiver.')

    def run(self):
        print('ran really fast')

class Hybrid(Wizard, Archer):
    def __init__(self,name,power,arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = Hybrid("Borgie", 50, 100)
print(hb1.sign_in())
