
while True:
    try:
        age = int(input("What is your age?"))
        print(age)
    except ValueError:
        print("Please enter a number")
    except ValueError:  # this will not run because the ValueError is caught up top already
        print("!!!!")
    except ZeroDivisionError:
        print("Please enter a number that is not zero")
    else:
        print("Thank you!")


def sum(num1/num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err: #catches both types of errors and set it as a variable
        print(err)

