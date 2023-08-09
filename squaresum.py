class Point:
    def __init__(self,x,y,z):
        self.x= x
        self.y=y
        self.z=z

    def sqsum(self):
        # squaresum= x*x + y*y +z*z
        # return squaresum 
        n1=int(input("enter value of x :"))
        n2=int(input("enter value of y :"))
        n3=int(input("enter value of z :"))
        a=pow(n1,2)
        b=pow(n2,2)
        c=pow(n3,2)
        result=a+b+c
        print(result)
        return result
Point.sqsum(self="")

        