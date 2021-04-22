
# arguments & keyword arguments
def plus(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b

# plus(1, 1, 1, 12, 2,3,  4, 5,6 ,7, 8, 8, helli=True, dsafkdlsa=False, fkasldf=True)

# OOP - Class
class Car():
    # method : function inside class
    def start(potato):            # python's every methods are given first argument 'self' by python
        print(potato.color)       # self -> potato
        print("I started")
    def __str__(self):
        return f"Car with {self.wheels} wheels"
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")    # get (key, default)
        self.price = kwargs.get("price", "$20")

# porche = Car()
# porche.color = "Red"
# print(porche.color)
# porche.start()

# dir : list of strings of the class
# print(dir(Car))
# porche = Car(color="green", price="$40")
# print(porche)   # porche 객체를 string으로 바꿈. (Call porche.__str__)
#
# print(porche.color, porche.price)
# mini = Car()
# print(mini.color, mini.price)

class Convertible(Car):         # extends Car class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)              # super : parent class
        self.time = kwargs.get("time", 10)
    def take_off(self):
        return "taking off"
    def __str__(self):
        return f"Car with {self.wheels} wheels with no loop"

BMW = Convertible(color="Blue", price="$100", time=100)
print(BMW)