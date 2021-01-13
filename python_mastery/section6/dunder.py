#Dunder methods allow us to overwrite built-in methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name" : "Kennet",
            "has_pets" : False
        }

    def __str__(self):  # modifying dunder method of STR
        return f'{self.color}'

    def __len__(self):
        return 5

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure["name"])
