import math

class Shape:

    def area(self):
        raise NotImplementedError

 # Create a class that inherits area() from shape class and 
 # calculates the rectangle's area
  
class Rectangle(Shape):
    def __init__ (self,length,width):
        self.length = length
        self.width = width

    def area(self):
       return self.length * self.width

# Create a class that inherits area() from shape class and 
 # calculates the circle's area
  
class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
       return math.pi * self.radius ** 2

