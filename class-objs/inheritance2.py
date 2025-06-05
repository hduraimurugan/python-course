from inheritance import Dad

class Son(Dad):
    def factory(self):
        print("I am from factory")
    # def house(self):
    #     print("I am from Son Dad")

s= Son()
s.house()