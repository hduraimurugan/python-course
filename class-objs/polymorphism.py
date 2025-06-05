
class Dad:
    def house(self):
        print("I am from Dad house")
class Son(Dad):
    def factory(self):
        print("I am from factory")
    def house(self):
        print("I am from Son Dad's house")  #Polymorphism- overriding

s=Son()
s.house()
