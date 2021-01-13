#inheriting all of the methods from the superclass List
class SuperList(list):

    # def __init__(self):
    #     super().__init__()

    def __len__(self):
        return 1000

super_list1 = SuperList()
super_list1.append(5)
print(len(super_list1))
print(super_list1)
print(issubclass(SuperList, list))