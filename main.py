# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def plus(a, b):
    if type(a) is not int or type(b) is not int:
        return a + b
    else:
        return None

def minus(a, b):
    if type(a) is not int or type(b) is not int:
        return a - b
    else:
        return None

def times(a, b):
    if type(a) is not int or type(b) is not int:
        return a * b
    else:
        return None

def division(a, b):
    if type(a) is not int or type(b) is not int:
        return a / b
    else:
        return None

def power(a, b):
    if type(a) is not int or type(b) is not int:
        return a ** b
    else:
        return None

def negation(a):
    if type(a) is not int:
        return -a
    else:
        return None
def reminder(a, b):
    if type(a) is not int or type(b) is not int:
        return a % b
    else:
        return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = "10"
    b = 27.2

    print(plus(a, b))
    print(minus(a, b))
    print(times(a, b))
    print(division(a, b))
    print(power(a, b))
    print(negation(a))
    print(reminder(a, b))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
