class Pizza:
    def __init__(self, size=25, type="Margarita", toppings=[], payment="Cash", address="", phoneNum="", note=""):
        self.size = size
        self.type = type
        self.toppings = toppings
        self.payment = payment
        self.address = address
        self.phoneNum = phoneNum
        self.note = note

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def decreaseTime(self):
        self.time -= 1

    def __str__(self):
        return f"Time:{self.time}, Size:{self.size}, Type:{self.type}, Toppings:{self.toppings}, Payment: {self.payment}, " \
            f"Address:{self.address}, Phone:{self.phoneNum}, Note:{self.note}"
