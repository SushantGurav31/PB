class bankaccount:
    def __init__(self,balance):
        self.__balance=balance  #private variablrs 


    def deposit(self, amount):
        self.__balance +=amount


    def get_balance(self):
        return self.__balance
    

acc = bankaccount(1000)
acc.deposit(500)

print(acc.get_balance())  #output:1500
#print(acc.__balance)  #error:cannot access private variable