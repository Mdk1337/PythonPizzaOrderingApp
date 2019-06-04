import socket
import pickle
import random
import threading
import time
from tkinter import *

from pizzaService import Pizza


pizzas1 = []
pizzas2 = []

def acceptRequests():
    """
    this function accepts requests, handles them and adds them to the undelivered pizzas listBox
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((socket.gethostname(), 13337))
    sock.listen(5)
    while True:
        print("Waiting for a connection")
        client, addr = sock.accept()
        print(f"Client {addr} -> connected!")
        msg = client.recv(1024)  # accepting binary representation of an object
        pizza = pickle.loads(msg)  # using pickle module to convert it into an object
        timeToDeliver = random.randint(10, 50)  # generating random time to deliver
        pizza.setTime(timeToDeliver)
        client.send(str(timeToDeliver).encode("utf-8"))  # sending the time to deliver back to client
        client.close()
        pizzas2.append(pizza)  # adding our accepted pizza object to a list
        pizzaList2.insert(END, pizza.__str__())


def decreaseTime(delay=1):
    """
    this function decreases timeToDeliver to everyundelivered pizza and calls the updateListBoxes function
    :param delay: time for refresh delay (default 1 second)
    """
    while True:
        for i in range(len(pizzas2)):
            if pizzas2[i].getTime() > 0:
                pizzas2[i].decreaseTime()
        time.sleep(delay)
        updateListBoxes()


def updateListBoxes():
    """
    deleting listbox contents and re-adding it according to the timeToDeliver left
    """
    pizzaList1.delete(0, END)
    pizzaList2.delete(0, END)

    for i in range(len(pizzas2)):
        if i ==len(pizzas2):
            break
        if pizzas2[i].getTime() > 0:
            pizzaList2.insert(END, pizzas2[i])
        else:
            pizzas1.append(pizzas2[i])
            pizzas2.pop(i)
            i -= 1

    for i in range(len(pizzas1)):
        pizzaList1.insert(END, pizzas1[i])


serverThread = threading.Thread(target=acceptRequests, args=())
serverThread.start()

timeUpdateThread = threading.Thread(target=decreaseTime, args=(1,))
timeUpdateThread.start()


root = Tk()  # actual window object
root.title("Server")  # naming the window object
root.geometry("740x700")  # screen resolution

deliveredPizzas = LabelFrame(root, text="Delivered Pizzas")  # delivered pizzas labelframe start
pizzaList1 = Listbox(deliveredPizzas, selectmode=SINGLE)  # listBox for all the pizzas that have been delivered
pizzaList1.place(x=5, y=5, height=260, width=640)
deliveredPizzas.place(x=40, y=40, height=300, width=660)  # delivered pizzas labelframe end

undeliveredPizzas = LabelFrame(root, text="Undelivered Pizzas")  # undelivered pizzas labelframe start
pizzaList2 = Listbox(undeliveredPizzas, selectmode=SINGLE)  # listBox for all the pizzas that are still to be delivered
pizzaList2.place(x=5, y=5, height=260, width=640)
undeliveredPizzas.place(x=40, y=380, height=300, width=660)  # undelivered pizzas labelframe end
root.mainloop()
