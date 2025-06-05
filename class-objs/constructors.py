class Student:
    def __init__(self,name,age,grade): # init - constructor
        self.name=name
        self.age=age
        self.grade=grade

    def display(self):
        print(f"{self.name} is aged {self.age} has a grade of {self.grade}")

#Multiple objs
s1= Student("Durai",24, "A")
s2= Student("Kannan", 62, "B")
s3= Student("Sachin",26, "O")

s1.display()
s2.display()
s3.display()