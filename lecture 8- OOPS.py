#create a student class that takes name and marks of 3 subjects as arguments in constructurs.then create a method to print the avg.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
       sum=0
       for val in self.marks:
           sum+=val
       print("hi",self.name,"your avg score is:",sum/3)

s1=Student("ayan",[99,98,90])
s1.get_avg()



#create account class with 2 atrr-balance and account no.
#create methods for debit ,credit and printing the balance.


class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self, amount):
        self.balance -=amount
    print("Rs.", amount, "was debited")
    print("total balance =", self.get_balance())
     
    def credit(self, amount):
        self.balance +=amount
    print("Rs.", amount, "was credited")
    print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(20000,12344)
acc1.debit(800)
acc1.credit(1900)
