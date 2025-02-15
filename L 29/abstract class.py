from abc import ABC, abstractmethod

class ABsc(ABC):
    def print(self,x):
        print("Pased value : ", x)

    @abstractmethod
    def task(self):
        print("we are inside Abscclass task")


class test_class(ABsc):
    def task(self):
        print("we are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)