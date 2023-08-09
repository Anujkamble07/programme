class car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
c4 = car ('uttam',2020,209281)
c1 = car ('anuj',2022,2345)
print(c1.model)
print(c1.name)
print(c4.name)


class vehicle:
    def __init__(self,number,color,seating_capacity=50):
        self.number=number
        self.color=color
        self.seating_capacity =50


class bus(vehicle):
  pass  
c3 = bus (234,"red","seating_capacity")
c4 = bus (4556,"green","seating_capacity")

print(c4.seating_capacity)


