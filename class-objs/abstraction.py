from abc import ABC,abstractmethod

class Manager(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def work_2(self):
        pass

class Employee(Manager):
    def work(self):
        print("Work 1")
    def work_2(self):
        print("Work 2")

e= Employee()
e.work()