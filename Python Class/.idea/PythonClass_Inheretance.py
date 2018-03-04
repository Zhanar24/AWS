# # Inheritance – Is-A relation
# # Class Mammals
# # Class Man
#
# # Aggregation – Has-A relation
# # Aggregation implies a relationship where the
# # child can exist independently of the parent.
# # Example: Class (parent) and Student (child).
# # Delete the Class and the Students still exist.
#
# # Composition – Has-A relation
# # Composition implies a relationship where the
# # child cannot exist independent of the parent.
# # Example: House (parent) and Room (child).
# # Rooms don't exist separate to a House.
#
# # Polymorphism – overriding
# # Polymorphism is based on the greek words Poly (many) and morphism (forms).
# # We will create a structure that can take or use many forms of objects.
# # Sometimes an object comes in many types or forms.
# # If we have a button, there are many different draw outputs
# # (round button, check button, square button, button with image)
# # but they do share the same logic: onClick().
# # We access them using the same method.
# # This idea is called Polymorphism.
#
# # class SimpleCalc:
# #     def subtraction(self, a, b):
# #         print("Result of subtraction is: {}".format(a - b))
# #
# #     def addition(self, a, b):
# #         print("Result of addition is: {}".format(a + b))
# #
# #
# # class AdvCalc:
# #     def __init__(self):
# #         self.calc1 = SimpleCalc()
# #
# #     def subtraction(self, a, b):
# #         self.calc1.subtraction(a, b)
# #
# #     def multiplication(self, a, b):
# #         print("Result of multiplication is: {}".format(a * b))
# #
# #     def division(self, a, b):
# #         print("Result of division is: {}".format(a / b))
# #
# #
# # calx = AdvCalc()
# # calx.subtraction(8, 7)
# # This line is going to fail, because of aggregation
# # del calx.calc1
# # calx.subtraction(8, 7)

#Example
# class Vehicle:
#     def drive_forward(self):
#         print("Yes, I do drive forward")
#
#     def drive_backward(self):
#         print("Yes, I do drive backward")
#
# class Car(Vehicle):
#     def __init__(self, cylinder):
#         self.cylinder = cylinder
#
#     def engine(self):
#         print("I have {} cylinder engine.".format(self.cylinder))
#
#
# class Truck(Car):
#     def __init__(self, cylinder):
#         Car.__init__(self, cylinder)
#
#
# truck1 = Truck(8)
# truck1.engine()
# truck1.drive_forward()
#

# class Mammals:
#     def eat(self):
#         print("I drink milk")
#
# class Human(Mammals):
#     def walk(self):
#         print("Yes, we do walk")
#
# timboo = Human()
# timboo.eat()
# timboo.walk()

class Mammal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("{} likes drinking milk".format(self.name))

class Human(Mammal):
    def walk(self):
        print("Yes, I can walk on 2 legs")

class Wolf(Mammal):
    def hunt(self):
        print("Yes, we do hunt")

AkTosh = Wolf("Hatiko")
AkTosh.eat()

timboo = Human("Timboo")
timboo.eat()