#calculator
class calculator():
    def __init__ (self,a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c
    def add(self):
        print(self.num1+self.num2+self.num3)
    def mul(self):
        print(self.num1*self.num2*self.num3)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
cal = calculator(a,b,c)
cal.add()
cal.mul()

    