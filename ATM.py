class ATM:
    def __init__(self, cardNumber, pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self):
        print("balance is 10000000000000000000000000000000000000")
    def withdrawl(self, amount):
        newAmount=10000000000000000000000000000000000000-amount
        print("balance remaining", newAmount)
def main():
    cardNumber=input("please enter your card number")
    pin=input("please enter pin")
    newUser=ATM(cardNumber, pin)
    print("choose you activity")
    print("1.balance enquery, 2.withdrawl")
    activity=int(input("enter activity number"))
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input("enter the amount")) 
        newUser.withdrawl(amount)
    else:
        print("enter a valid number")
if __name__=='__main__':
    main()