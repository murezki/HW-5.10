class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, passengers):
        if self.current_passengers + passengers <= self.max_passengers:
            self.current_passengers += passengers
        else:
            print("слишком много пассажиров")

    def __iadd__(self, passengers):
        if self.current_passengers + passengers <= self.max_passengers:
            self.current_passengers += passengers
        else:
            print("слишком много пассажиров")
        return self

    def __sub__(self, passengers):
        if self.current_passengers - passengers >= 0:
            self.current_passengers -= passengers
        else:
            print("удаляешь слишком много")

    def __isub__(self, passengers):
        if self.current_passengers - passengers >= 0:
            self.current_passengers -= passengers
        else:
            print("удаляешь слишком много")
        return self

    def __str__(self):
        return self.current_passengers


a1 = Airplane("боинг", 220, 120)
a2 = Airplane("боинг2", 190, 160)
print(a1 == a2)  
print(a1 > a2)  
a1 += 50 
print(a1.current_passengers)
a2 -= 100 
print(a2.current_passengers)
