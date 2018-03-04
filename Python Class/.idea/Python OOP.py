#def result = m1 + m2
    #def class_math(a, b):
    #Local variable
   # result = a + b
   # print(message)
   # return result
#Global variable
#message = "Additon"
#print(class_math(7, 8))
#print(class_print("Hello ", "Jamboo"))

#def test_func(fruit = 'mellon'):
    #Local variable
 #   print("I like " + fruit)
#Global variable
#test_func()
#test_func("apple")
#class Car:
    #Method is function defined in a class
   # def __init__(self, name):
     #   print("This is a new car, " + name)

# Class is a template to create objects
# Object: an instance of a class
# Instantiate: create an instance of a class
# Method: function defined in a class
# The difference between function and a method is that it uses a self parameter
# Attribute: a variable bound to an instance of a class
# It is suggested to use uppercase names for classes

#sienna = Car("Sienna")
#accord = Car("Accord")

#class Car:
  #  wheels = 4
  #  def __init__(self, name):
   #     print("This is a new car, " + name + ", it has {} wheels".format(self.wheels))

#camry = Car("Camry")
#sienna = Car("Sienna")

class Car:
    # Attribute
    wheels = 4
    #Special initializer method
    #__init__ is a special method which is automatically called
    # every time when you create a new object off of a class
    #def __init__(self, name):
     #   print("This is a new car, " + name)
    # Regular method
    #def get_wheels(self):
    #    print("This is a new car, " + name)

    # Regular method
   # def get_wheels(self):
    #    print("This car has {} wheels".format(self.wheels))

#car1 = Car("Camry")
#car1.get_wheels()

class Car:
    def __init__(self, name):
        print("This is a new car," + name)
    def __str__(self):
        return "This is a Car object"
    def __del__(self):
        print("Please don't kill me")
car1 = Car("Camry")
print(car1)
del car1