import tkinter
from tkinter import *


def makeAnObject():
    from pizzaService.Pizza import Pizza
    toppings = []
    if varKetchup.get():
        toppings.append("Ketchup")
    if varMayonnaise.get():
        toppings.append("Mayonnaise")
    if varOregano.get():
        toppings.append("Oregano")

    paymentSelected = "Cash"
    if varPayment.get() == 1:
        paymentSelected = "Check"
    elif varPayment.get() == 2:
        paymentSelected = "Credit Card"
    else:
        paymentSelected = "PayPal"
    pizza = Pizza(varSize.get(), pizzaTypeList.get(ACTIVE), toppings, paymentSelected, address.get(), phone.get(), noteTextBox.get(1.0,END))



root = Tk()  # actual window object
root.geometry("740x700")  # screen resolution

topLabel = Label(root, text="Order your pizza!", font=("Verdana", "20"))  # top label config

pizzaSize = LabelFrame(root, text="Choose your desired pizza size")  # pizza size labelframe start

varSize = IntVar()
radioPizza25 = Radiobutton(pizzaSize, text="25 cm", variable=varSize, value=25)
radioPizza32 = Radiobutton(pizzaSize, text="32 cm", variable=varSize, value=32)
radioPizza50 = Radiobutton(pizzaSize, text="50 cm", variable=varSize, value=50)

radioPizza25.select() # setting the first pizza size option as default

radioPizza25.grid(row=0, column=0, padx=30, pady=5)
radioPizza32.grid(row=1, column=0, padx=30, pady=5)
radioPizza50.grid(row=2, column=0, padx=30, pady=5)

pizzaSize.place(x=20, y=70, height=150, width=180)  # pizza size labelframe end

pizzaType = LabelFrame(root, text="Choose your desired pizza type")  # pizza type labelframe start

pizzaTypeList = Listbox(pizzaType, selectmode=SINGLE)  # listBox for pizza type
pizzaTypeList.insert(0, "Margarita")
pizzaTypeList.insert(END, "Funghi")
pizzaTypeList.insert(END, "Quatro Stagione")
pizzaTypeList.insert(END, "Vegeteriana")

pizzaTypeList.activate(0) # setting the first pizza type option as default

pizzaTypeList.pack(pady=10, padx=5)
pizzaType.place(x=250, y=70, height=150, width=200)  # pizza type labelframe end

pizzaToppings = LabelFrame(root, text="Choose your desired pizza toppings")  # pizza toppings labelframe start

varKetchup = IntVar()
toppingKetchup = Checkbutton(pizzaToppings, text="Ketchup", variable=varKetchup)  # checkbutton for ketchup

varMayonnaise = IntVar()
toppingMayonnaise = Checkbutton(pizzaToppings, text="Mayonnaise", variable=varMayonnaise,
                                justify=RIGHT)  # checkbutton for mayonnaise

varOregano = IntVar()
toppingOregano = Checkbutton(pizzaToppings, text="Oregano", variable=varOregano)  # checkbutton for orageno

toppingKetchup.grid(row=0, column=0, padx=30, pady=5)
toppingMayonnaise.grid(row=1, column=0, padx=30, pady=5)
toppingOregano.grid(row=2, column=0, padx=30, pady=5)

pizzaToppings.place(x=500, y=70, height=150, width=220)  # pizza toppings labelframe end

personalInfo = LabelFrame(root, text="Please input your information")  # personal info labelframe start

paymentLabel = Label(personalInfo, text="Choose your payment option!",
                     font=("Verdana", "10"))  # label above payment radiobuttons

paymentOption = Frame(personalInfo)  # payment option subframe initialization

varPayment = IntVar()
radioCash = Radiobutton(paymentOption, text="Cash", variable=varPayment, value=0)
radioCheck = Radiobutton(paymentOption, text="Check", variable=varPayment, value=1)
radioCard = Radiobutton(paymentOption, text="Credit Card", variable=varPayment, value=2)
radioPayPal = Radiobutton(paymentOption, text="PayPal", variable=varPayment, value=3)

radioCash.grid(row=0, column=0, padx=10, pady=5)
radioCheck.grid(row=1, column=0, padx=10, pady=5)
radioCard.grid(row=2, column=0, padx=10, pady=5)
radioPayPal.grid(row=3, column=0, padx=10, pady=5)

paymentOption.place(x=20, y=40)  # payment option subframe placement [end]
paymentLabel.place(x=5, y=10)

informationLabel = Label(personalInfo, text="Where should we deliver your pizza?", font=("Verdana", "10"))
informationLabel.place(x=250, y=10)

informationFrame = Frame(personalInfo)  # address, phone and note subframe

addressLabel = Label(informationFrame, text="Address:")  # address Label
address = StringVar()
addressTextBox = Entry(informationFrame, textvariable=address, width=30)  # address TextBox

phoneLabel = Label(informationFrame, text="Phone number:")  # phone Label
phone = StringVar()
phoneTextBox = Entry(informationFrame, textvariable=phone, width=30)  # phone TextBox

noteLabel = Label(informationFrame, text="Note:")  # note Label
noteTextBox = Text(informationFrame, height=4, width=30)  # note multiline TextBox

addressLabel.pack(side=TOP)
addressTextBox.pack(side=TOP)

phoneLabel.pack(side=TOP)
phoneTextBox.pack(side=TOP)

noteLabel.pack(side=TOP)
noteTextBox.pack(side=TOP)
informationFrame.place(x=270, y=40)  # address, phone and note subframe placement [end]

personalInfo.place(x=90, y=280, height=255, width=570)  # personal info labelframe end

orderButton = Button(root, text="Send your order    ", compound=RIGHT, bitmap="warning", command=makeAnObject) # order button initialization.
orderButton.pack(side=BOTTOM,pady=70) # order button placement

topLabel.pack(side=TOP, pady=10)  # top label packing
root.mainloop()  # displaying tkinter mainloop
