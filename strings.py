name = input("What is your name?  " )
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}! This was using legacy format".format(name,color,animal))

print(f"{name} you like a {color} {animal}! This is using f-strings")

print(f"{type(name)} you like a {type(color)} {type(animal)}")


