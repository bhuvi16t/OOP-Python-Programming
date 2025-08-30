# Q-1: Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

# Eg. After making above classes and methods, on executing below code:-

# write your code here
class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def Create_Perimeter(self):
    return 'the rectangle Perimeter is :',2*(self.length+self.width)
  def Display(self):
    area = self.length*self.width
    return 'the area of rectangle is :',area
rect = Rectangle(3,4)
print(rect.Create_Perimeter())
print(rect.Display())
