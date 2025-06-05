# class Grandfather: #Multilevle inheritance
#     def car(self):
#         print("Its a red car")

class Dad:
    def house(self):
        print("I am from Dad house")

class Mom:
    def shop(self):
        print("Moms shop")
    def house(self):
        print("I am from Mom house")

class Son(Dad, Mom):
    def factory(self):
        print("I am from factory")
    def house(self):
        print("I am from Son Dad")

class Daughter(Dad, Mom): # Multiple inheritance
    def school(self):
        print("Its a school from daughter")

# d= Dad()
# d.house()

s= Son()
s.house()

d=Daughter()
d.house()
