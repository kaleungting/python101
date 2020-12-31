# global

a = 1


def parent():
    a = 10  # parent_variable

    def child():
        return a
    return child()


print(parent())
print(a)

# Scoping Hierachy
# 1 - start with local
# 2 - check parent
# 3 - check global
# 4 - built in python functions


