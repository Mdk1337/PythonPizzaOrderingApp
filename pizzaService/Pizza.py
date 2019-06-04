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

    def getSize(self):
        return self.size

    def getType(self):
        return self.type

    def getToppings(self):
        if len(self.toppings) > 0:
            return self.toppings
        else:
            return "No toppings"

    def getPayment(self):
        return self.payment

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phoneNum

    def getNote(self):
        if len(self.note) > 1:
            return self.note
        else:
            return "None"

    def getTime(self):
        return self.time

    def decreaseTime(self):
        self.time -= 1

    def __str__(self):
        return f"Time:{self.time}, Size:{self.size}, Type:{self.type}, Toppings:{self.toppings}, Payment: {self.payment}, " \
            f"Address:{self.address}, Phone:{self.phoneNum}, Note:{self.note}"
