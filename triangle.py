# Create a program to work out the area and perimeter of a triangle
import math
import time

def ask_sides():
    global height               #set global variables so that they can be recalled
    global length
    global width
    height=float(input("\nWhat is the length of side a? "))
    length=float(input("What is the length of side b? "))
    width=float(input("What is the length of side c? "))
    print()

def find_perimeter():
    perimeter = height + length + width
    print("\nThe perimeter of your triangle is " + str(perimeter) + "\n")
    time.sleep(2)

def find_area():
    perimeter = height + length + width
    semi_perimeter = perimeter / 2
    semi_perimeter = float(semi_perimeter)          # set as same data type so it can be more easily calculated later
    a = semi_perimeter - height
    b = semi_perimeter - length
    c = semi_perimeter - width
    area = math.sqrt(semi_perimeter*(a*b*c))
    area = round(area, 2)
    print("\nThe area of your triangle is " + str(area) + "\n")
    time.sleep(2)


# Calculate the perimeter and/or area of a triangle
selection=input("\nHi, thanks for coming to Pythag-4-Us, please follow the instructions below. \n\n If you would like to calculate the perimeter of a triangle, please press P, \n to calculate the area of a triangle, please press A: ")

if selection.lower() == "p":
    ask_sides()
    find_perimeter() 
    next_step = input("Would you also like to find out the area of your triangle? Y/N ")
    if next_step.lower() == "y":
        find_area()
    print("\nHope this helped, let me know when you next have a yearning for a learning!\n")
          
elif selection.lower() == "a":
    ask_sides()
    find_area()
    next_step_2 = input("\nWould you also like to find out the perimeter of your triangle? Y/N ")
    if next_step_2.lower() == "y":
        find_perimeter()
    print("\nHope this helped, let me know when you next have a yearning for a learning!\n")

else: print("\nNeither option? Ok, let me know when you have a yearning for a learning!\n")

