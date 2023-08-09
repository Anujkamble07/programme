class calculator:
    # num1=int(input("enter the value of num1 :"))
    # num2=int(input("enter the value of num2 :"))
    def __init__(self,num1,mun2):
        self.num1=num1
        self.num2=num2
    # def add(self):
    #     a=int("enter ")
    #     b=y
#     #     sum=a+b
    def add(self):
        print(num1 + num2)
    def subtract(self):
        print(num1 * num2)
    def multiply(self):
        print(num1 - num2)
    def divide(self):
        print(num1/num2)
num1=float(input("enter the value of num1 :"))
num2=float(input("enter the value of num2 :"))
obj=calculator(num1,num2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())
