balance = 1000.00
opt = 0

def checkBal():
    global balance
    print ("Your current balance: Rs.", balance)
    
def withdraw():
    global balance
    amount = float(input("Enter amount you want to withdraw: Rs."))
    if (amount<balance):
        balance -= amount
        print ("Your current balance: Rs.", balance)
    else:
        print ("Insufficient balance to complete transaction")

def deposit():
    global balance
    amount = float(input("Enter amount you want to deposit: Rs."))
    if (amount>0):
        balance += amount
        print ("Your current balance: Rs.", balance)
    else:
        print ("Invalid amount")

while (opt!=4):
    print ("====================================")
    print ("\tWelcome to ABC bank")
    print ("1. Check balance")
    print ("2. Withdraw money")
    print ("3. Deposit money")
    print ("4. Exit")
    print ("====================================")

    opt = int(input("Enter your option: "))

    if (opt==1):
        checkBal()
    elif (opt==2):
        withdraw()
    elif (opt==3):
        deposit()
    elif (opt==4):
        print ("Exiting system!\nHave a nice day!");
    else:
        print ("Invalid input, try again")
    



