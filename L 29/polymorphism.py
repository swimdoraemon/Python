from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class snake(Animal):
    def move(self):
        print("i can crawl")

class dog(Animal):
    def move(self):
        print("i can bark")

class Lion(Animal):
    def move(self):
        print("i can roar")

R = Human()
R.move()

K = snake()
K.move()

R = dog()
R.move()

K = Lion()
K.move()



