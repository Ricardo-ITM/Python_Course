Notes from:
[Python Full Course for free 🐍 (2024) by Bro Code](https://youtu.be/ix9cRaBkVe0?si=qv3AoAIY4MvS0bBv)

# 1. Variables
A container for a value (string, integer, float, boolean). A variable behaves as if it was the value it contains.

```py
# String
food = "Bro123@fake.com"

# Integer
age = 25

# Float
price = 10.99

# boolean
is_student = True
``` 

# 2. Type Casting
The process of converting a variable from one data type to another <br />
&emsp;&emsp;**str( ), int( ), float( ), bool( )**

```py
name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

type(is_student) # returns a string of data type

# str()
str(age) # returns a string

# int()
int(gpa) # returns a integer | float values gets truncated

# float()
float(age) # returns a float

# bool()
bool(name) # returns a boolean | "": False , "some text": True
``` 

# 3. User Input
A function that prompts the user to enter data. <br />
Returns the entered data as a string

```py
# Input
product = "Soda"
price = float(input(f"Enter a price for {product}: ")) # input returns a string so we typecast to an float
``` 

# 4. Arithmetic and Math

```py
# Arithmetic operators
# +: addition
# -: substraction
# *: multiplication
# /: division
# **: power
# %: modulus

# Augmented assignment operator
# +=
# -=
# *=
# /=
# **=

x = 5.21
y = -1.34
z = 20

# Built-in Math functions
round(x) # rounding
abs(y) # aboslute
pow(base, exponent) # power
max(x, y, z) # maximum value
min (x, y, z) # minimum value

# math module Constants
math.pi # 3.14159265...
math.e # 2.718281...

# math module functions
math.sqrt(x)
math.ceil(x)
math.floor(x)
```

# 5. If Statements
Do some code only IF some condition is True. <br />
Else do something Else.

```py
# if condition:
#     <-- do this -->
# elif other_condition:
#     <-- do this -->
# elif some_other_condition:
#     <-- do this -->
# else:
#     <-- do this -->

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

temp < 28 and temp > 0 | 28 > temp > 0

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("Its is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp <= 0 and not is_sunny:
    print("Its is COLD outside")
    print("It is CLOUDY")

``` 

# 6. Logical Operators
Evaluate multiple conditions (or, and, not) <br />
&emsp;&emsp;&emsp;&emsp;**or** = at least one condition must be True <br />
&emsp;&emsp;&emsp;&emsp;**and** = both conditions must be True <br />
&emsp;&emsp;&emsp;&emsp;**not** = inverts the condition (not False, not True)

```py
# if condition1 and (condition2 or not condition3):
#     <-- do this -->
# else:
#     <-- do this -->
```

# 7. Conditional Expressions (ternary operator)
A one-line shortcut for the if-else statement (ternary operator). <br />
Print or assign one of the two values based on a condition X if condition else y

```py
# print(<-- print this --> if condition else <-- print this -->)
# result = <-- assign this --> if condition else <-- assign this -->

num = 4
a = 13
b = 20
age = 27
temperature = 20
user_role = "invited"

result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
```

# 8. String Methods

```py
name = "Ricardo Telles"

len(name) # Returns integer

name.find("e") # Returns integer the first item index
name.rfind("e") # Returns integer the last item index
name.capitalize() # Returns string with the first character uppercase
name.upper() # Returns string with all characters uppercase
name.lower() # Returns string with all characters lowercase
name.isdigit() # Returns boolean if all characters are numbers
name.isalpha() # Returns boolean if all characters are alphabetical characters, excluding spaces
name.count("e") # Returns integer count how many character given the parameter are in the string
name.replace("s", "z") # Returns string with replaced character

print(help(str)) # See all string methods
```

# 9. String Indexing
Accessing elements of a sequence using [ ] (indexing operator) <br />
&emsp;&emsp;**[start : end : step]**

```py
credit_number = "1234-5678-9012-3456"
# String  "| 1 | 2 | 3 | 4 | - | 5 | 6 | 7 | 8 | - | 9 | 0 | 1 | 2 | - | 3 | 4 | 5 | 6 |"
# index    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |

# index
credit_number[0] # 1

# negative index
credit_number[-1] # 6
credit_number[-2] # 5
credit_number[-3] # 4
credit_number[-4] # 3

# start index
credit_number[5:] # 5678-9012-3456
credit_number[-4:] # 3456

# end index
credit_number[:4] # 1234

# start and end index
credit_number[5:9] # 5678-

# step
credit_number[::2] # 13-6891-46
credit_number[::3] # 146-136

# reverse step
credit_number[::-1] # 6543-2109-8765-4321
```

# 10. Format Specifiers
**{value:flags}** format a value based on what flags are inserted

```py
price1 = 3.14159
price2 = -987.65
price3 = 3000.14159

# |:.(number)f| = decimal places
f"{price1:.2f}" # 3.14
f"{price1:.3f}" # 3.141

# |:(number)| = allocate spaces
f"{price1:10}"# string:            3   .   1   4   1   5   9
                # index: 1   2   3   4   5   6   7   8   9  10

# |:0(number)| = allocate and zero pad that many spaces
f"{price1:010}"# string: 0   0   0   3   .   1   4   1   5   9
                 # index:  1   2   3   4   5   6   7   8   9  10

# |:<| = left Justify
f"{price1:<10}"# string: 3   .   1   4   1   5   9
                 # index:  1   2   3   4   5   6   7   8   9  10

# |:>| = right Justify
f"{price1:>10}"# string:            3   .   1   4   1   5   9
                 # index: 1   2   3   4   5   6   7   8   9  10

# |:^| = center align
f"{price1:^10}"# string:    3   .   1   4   1   5   9
                 # index: 1   2   3   4   5   6   7   8   9  10

# |:+| = use a plus sign to indicate positive value
f"{price1:+}" # +3.14159
f"{price2:+}" # -987.65

# |:=| = place sign to leftmost position


# |: | = insert a space before for positive numbers
f"{price1: }" # |space|3|.|1|4|1|5|9
f"{price2: }" # |  -  |9|8|7|.|6|5|

# |:,| = comma separator
f"{price3:,}" # 3,000.14159

# Combine flags
# flags = |+||,||.2f|
f"{price3:+,.2f}" # +3,000.14
```

# 11. While Loops
Execute some code WHILE some condition remains true

```py
num = int(input("Enter a # between 1 - 10; "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10; "))

print(f"Your number is {num}")

# use "break" to escape from the loop
principle = 0
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break
```

# 12. For Loops
Execute a block of code a fixed number of times. <br />
You can iterate over a **range, string, sequence,** etc.

```py
# range(start, end)
for x in range(1, 11):
    print(x) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# range(start, end, step)
for x in range(1, 11, 3):
    print(x) # 1, 4, 7, 10

# reverse range
for x in reversed(range(1, 11)):
    print(x) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# iterate over a string
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# continue
for x in range(1, 21):
    if x == 13:
        continue # skip 13
    else:
        print(x)

# break
for x in range(1, 21):
    if x == 13:
        break # end loop at 13
    else:
        print(x)
```

# 13. Sleep function

```py
import time

for x in reversed(range(1, 21)):
    print(x)
    time.sleep(1) # 1 second
```

# 14. Nested Loops
A loop within another loop (outer, inner) <br />
outer loop: <br />
&emsp;&emsp;&emsp;**inner loop:**

```py
for x in range(3): 
    for y in range(1, 10):
        print(y, end="") 
    print()
# 123456789, 123456789, 123456789

# use "break" to escape from the inner loop
for x in range(3): 
    for y in range(1, 10):
        print(y, end="")
        break
    print()
# 1, 1, 1
```

# 15. Collections
Single "variable" used to store multiple values <br />
&emsp;&emsp;**List = [ ]** ordered and changeable. Duplicates OK. <br />
&emsp;&emsp;**Set = { }** unordered and inmutable, but Add/Remove OK. NO Duplicates, better for constants. <br />
&emsp;&emsp;**Tuple = ( )** ordered and unchangeable. Duplicates OK. FASTER

List = [ ]
```py
fruits = ["apple", "orange", "banana", "coconut"]

# Replace item
fruits[0] = "pineapple"

# Add item at the end of list
fruits.append("pineapple")

# Remove item
fruits.remove("apple")

# Insert item with given index
fruits.insert(0, "pineapple")

# Order items in reference to alphabetical order
fruits.sort()

# Reverse items
fruits.reverse()

# Remove all items
fruits.clear()

# Remove and return last item (default) or item given index
fruits.pop()
fruits.pop(2)

# Return the item index
fruits.index("coconut")

# Return number of times the item in list
fruits.count("banana")
```
Set = { }
```py
fruits = {"apple", "orange", "banana", "coconut"}

# Check if the item is in set, returns boolean
"pineapple" in fruits

# Add item
fruits.add("pineapple")

# Remove item
fruits.remove("apple")

.pop() behaves randomly

# Remove all items
fruits.clear()
```
Tuple = ( )
```py
fruits = ("apple", "orange", "banana", "coconut")

# Check if the item is in tuple, returns boolean
"pineapple" in fruits

# Return the item index
fruits.index("coconut")

# Return number of times the item in list
fruits.count("banana")

# Help commands
print(dir(list|tuple|set))
print(help(list|tuple|set))
```

# 16. 2D Collections

```py
fruits      =    ["apple", "orange", "banana"]
vegetables  =    ["pumpkin", "carrot", "tomato"]
meats       =    ["ham", "chop", "beef", "beacon"]

groceries = [fruits, vegetables, meats]

groceries[0] # Access Fruits list
groceries[0][0] # Access Item from Fruits list

# Print all list
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
```

# 17. Dictionary
A collection of **{key:value}** pairs ordered and changeable. No duplicates

```py
capitals = {
       "USA": "Washington D.C.",
       "India": "New Delhi",
       "China": "Beijing",
       "Russia": "Moscow"
}

# Help Functions
dir(capitals)
help(capitals)

# Return value given a Key, if Key doesn't exist, return None
capitals.get("USA")

# As a Condition
"That capital exists" if capitals.get("Japan") else "That capital doesn't exist"

# Update Dictionary
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

# Remove and return value given a key
capitals.pop("China")

# Remove and return latest value as tuple of key and value
capitals.popitem()

# Clear Dictionary
capitals.clear()

# Return all the keys
capitals.keys()

# Return all the values
capitals.values()

# Retuns a 2d list of tuples [(),(),()]
capitals.items()


# Print keys
for country in capitals:
       print(country)

# Print values
for capital in capitals.values():
       print(capital)

# Print key and values
for key, value in capitals.items():
       print(f"{key}: {value}")
```

# 18. Random

```py
import random
print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Return random int between low and high
random.randint(low, high)

# Return random float between 0 and 1
random.random()

# Return random element from collection
random.choice(options)

# Shuffle a list
random.shuffle(cards)
```

# 19. Function
A block of reusable code <br />
place **( )** after the function name to invoke it

```py
def happy_birthday(name, age):
       print(f"Happy birthday to {name}!")
       print(f"You are {age} years old!")
       print("Happy birthday to you!")
       print()

happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)

return
statement used to end a function and send a result back to the caller

def add(x, y):
       z = x + y
       return z

def subtract(x, y):
       z = x - y
       return z

def multiply(x, y):
       z = x * y
       return z

def divide(x, y):
       z = x / y
       return z

print(add(4, 6))
print(subtract(4, 2))
print(multiply(5, 5))
print(divide(10, 2))
```

# 20. Default arguments
A default value for certain parameters, default is used when that argument is omitted, make your functions more flexible, reduces # of arguments. 
1. positional
2. **DEFAULT**
3. keyword
4. arbitrary

```py
# Default arguments should place after non-default arguments
def net_price(list_price, discount=0, tax=0.05):
       return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))
```

# 21. Keyword arguments
An argument preceded by an identifier, helps with readability, order of arguments doesn't matter
1. positional
2. default
3. **KEYWORD**
4. arbitrary

```py
# Keyword arguments should place after positional arguments
def hello(greeting, title, first, last):
       print(f"{greeting} {title}{first} {last}")

hello("Hello", first="Spongebob", title="Mr.", last="Squarepants")

# Helps with readability
def get_phone(country, area, first, last):
       return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
```

# 22. Arbitrary arguments
*args = allows you to pass multiple non-key arguments | packing to a tuple <br />
**kwargs = allows you to pass multiple keyword-arguments | packing to a dictionary <br />
\* unpacking operator
1. positional
2. default
3. keyword
4. **ARBITRARY**

```py
def add(*args):
       total = 0
       for arg in args:
              total += arg
       return total

print(add(1, 2, 3, 4, 5))

def print_address(**kwargs):
       for key, value in kwargs.items():
              print(f"{key}: {value}")

print_address(street="Miguel Hidalgo", 
              num="831"
              city="Mexicali", 
              state="Baja California", 
              zip="21214")

def shipping_label(*args, **kwargs):
       for arg in args:
              print(arg, end=" ")
       print()

       if "apt" in kwargs:
              print(f"{kwargs.get('street')} {kwargs.get('apt')}")
       elif "pobox" in kwargs:
              print(f"{kwargs.get('street')}")
              print(f"{kwargs.get('pobox')}")
       else:
              print(f"{kwargs.get('street')}")

       print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
              street="123 Fake St.",
              apt="#100",
              city="Detroit",
              state="MI",
              zip="54321")
```

# 23. Iterables
An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

```py
numbers = [1, 2, 3, 4, 5]
numbers = (1, 2, 3, 4, 5)
fruits = {"apple", "orange", "banana", "coconut"} # Cannot be reversed
name = "Bro Code"
my_dictionary = {"A": 1, "B": 2, "C": 3} # .values() for values and .items() for both keys and values

for number in numbers:
       print(number)

for number in reversed(numbers):
       print(number, end=" - ")
```

# 24. Membership operators
Used to test whether a value or variable is found in a sequence
(string, list, tuple, set or dictionary)
1. **in**
2. **not in**

```py
#Strings
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
       print(f"There is a {letter}")
else:
       print(f"{letter} was not found")

#Sets
students = {"Spongebo", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
       print(f"{student} is a student")
else:
       print(f"{student} was not found")

# Dictionary
grades = {"Sandy": "A", 
              "Squidward": "B", 
              "Spongebob": "C", 
              "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
       print(f"{student}'s grade is {grades[student]}")
else:
       print(f"{student} was not found")


email = "BroCode@gmail.com"

if "@" in email and "." in email:
       print("Valid email")
else:
       print("Invalid email")
```

# 25. List comprehension
A concise way to create lists in Python, Compact and easier to read than traditional loops <br />
&emsp;&emsp;**[expression for value in iterable if condition]**

```py
# Slower way
doubles = []
for x in range(1, 11):
       doubles.append(x * 2)

# Faster way
doubles = [x * 2 for x in range(1, 11)]

# Add first letter of each item
fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# Add only positive numbers
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
```

# 26. Match-case statements (switch) | Python 3.10
An alternative to using many 'elif' statements <br />
Execute some code if a value matches a 'case' <br />
Benefits: Cleaner and syntax is more readable

```py
# Less readable
def day_of_week(day):
       if day == 1:
              return "It is Sunday"
       elif day == 2:
              return "It is Monday"
       elif day == 3:
              return "It is Tuesday"
       elif day == 4:
              return "It is Wednesday"
       elif day == 5:
              return "It is Thursday"
       elif day == 6:
              return "It is Friday"
       elif day == 7:
              return "Is is Saturday"
       else:
              return "Not a valid day"

# More readable
def day_of_week(day):
       match day:
              case 1:
                     return "It is Sunday"
              case 2:
                     return "It is Monday"
              case 3:
                     return "It is Tuesday"
              case 4:
                     return "It is Wednesday"
              case 5:
                     return "It is Thursday"
              case 6:
                     return "It is Friday"
              case 7:
                     return "Is is Saturday"
              case _: # _ = Wildcard
                     return "Not a valid day" 

# Slow way
def is_weekend(day):
       match day:
              case "Sunday":
                     return True
              case "Monday":
                     return False
              case "Tuesday":
                     return False
              case "Wednesday":
                     return False
              case "Thursday":
                     return False
              case "Friday":
                     return False
              case "Saturday":
                     return True
              case _:
                     return False

# Fast way
def is_weekend(day):
       match day:
              case "Sunday" | "Saturday":
                     return True
              case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                     return False
              case _:
                     return False
```

# 27. Module
A file containing code you want to include in your program <br />
use "import" to include a module (built-in or your own) <br />
useful to break up a large program reusable separate files

```py
# Help
print(help("modules")) # Print all modules
print(help("math")) # Print functions and constants of module

# Using an alias
import math as m

# Single function or constant
from math import pi
```

# 28. Scope resolution
Where a variable is visible and accesible <br />
&emsp;&emsp;**Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in**

```py
# Local
def func1():
       x = 1 # Enclosed scope
       def func2():
              x = 2 # local scope
              print(x) # This will print the local scope
       func2()

# Enclosed
def func1():
       x = 1 # Enclosed scope
       def func2():
              print(x) # This will print the enclosed scope
       func2()

# Global
def func1():
       print(x) # This will print the global scope

x = 2 # Global scope
func1()

#Built-in
from math import e #Built-in scope

def func1():
       print(e) # This will print the built-in scope

func1()

#Global vs Built-in
from math import e #Built-in scope

def func1():
       print(e) # This will print the global scope

e = 3 # This global variable will replace the built-in scope

func1()
```

# 29. if \_\_name\_\_ == \_\_main\_\_:
(this script can be imported or run standalone)<br />
Functions and classes in this module can be reused without the main block of code executing.<br />
&emsp;&emsp;&emsp;&emsp;Good practice (code is modular, <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; help readability, <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; leaves no global variables, <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; avoid unintended execution)

&emsp;&emsp;&emsp;&emsp;Ex. library = import library for funcionality <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; when running library directly, display a help page. <br />

**script1.py**
```py
# script1.py
def favorite_food(food):
       print(f"Your favorite food is {food}")

def main():
       print("This is script1")
       favorite_food("pizza")
       print("Goodbye!")

if __name__ == '__main__': # script2 won't execute this code
       main()
```
**script2.py**
```py
# script2.py
from script1 import *

def favorite_drink(drink):
       print(f"Your favorite drink is {drink}")

def main():
       print("This is script2")
       favorite_food("sushi")
       favorite_drink("coffee")
       print("Goodbye!")

if __name__ == "__main__":
       main()
```

# 30. Python Object-Oriented Programming
**object** = A "bundle" of related attributes (variables) and methods (functions) <br />
&emsp;&emsp;&emsp;&emsp;Ex. phone, cup, book <br />
&emsp;&emsp;&emsp;&emsp;You need a "class" to create many objects

**class** = (blueprint) used to design the structure and layout of an object

```py
> car.py
class Car:
       def __init__(self, model, year, color, for_sale):
              self.model = model
              self.year = year
              self.color = color
              self.for_sale = for_sale

       def drive(self):
              print(f"You drive the {self.color} {self.model}")
       
       def stop(self):
              print(f"You stop the {self.color} {self.model}")
       
       def describe(self):
              print(f"{self.year} {self.color} {self.model}")

> main.py
from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1) # Print the memory address

# Attribute access
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()
```

# 31. Class Variables
Shared among all instances of a Class <br />
Defined outside the constructor <br />
Allow you yo share data among all objects created from that Class

```py
class Car:
    
    wheels = 4 # Class Variable

    def __init__(self, model, year):
        self.model = model
        self.year = year

print(Car.wheels)
```

# 32. Inheritance
Allows a class to inherit attributes and methods from another class <br />
Help with code reusability and extensibility <br />

&emsp;&emsp;**class Child(Parent)**

```py
class Animal:
       def __init__(self, name):
              self.name = name
              self.is_alive = True

       def eat(self):
              print(f"{self.name} is eating")
       
       def sleep(self):
              print(f"{self.name} is sleeping")

class Dog(Animal):
       def speak(self):
              print("WOOF!")

class Cat(Animal):
       def speak(self):
              print("MEOW!")

class Mouse(Animal):
       def speak(self):
              print("SQUEAK!")

dog = Dog("Scooby")


dog.eat()
dog.sleep()
print(dog.is_alive)
print(dog.name)
```

# 33. Multiple and Multilevel

Multiple Inheritance <br />
Inherit from more than one parent class <br />
&emsp;&emsp;**C(A, B)**

Multilevel Inheritance <br />
Inherit from a parent which inherits from another parent <br />
&emsp;&emsp;**C(B) <- B(A) <- A**

```py
class Animal:

       def __init__(self, name):
              self.name = name

       def eat(self):
              print(f"{name} is eating")
       
       def sleep(self):
              print(f"{name} is sleeping")

class Prey(Animal):
       def flee(self):
              print(f"{name} is fleeing")

class Predator(Animal):
       def hunt(self):
              print(f"{name} is hunting")

class Rabbit(Prey):
       pass

class Hawk(Predator):
       pass

class Fish(Prey, Predator):
       pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()

fish.eat()
fish.sleep()
```

# 34. super()
Function used in a child class to call methods from a parent class (superclass). <br />
Allows you to extend the functionality of the inherited methods.

```py
class Shape:
       def __init__(self, color, is_filled):
              self.color = color
              self.is_filled = is_filled

       def describe(self):
              print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
       def __init__(self, color, is_filled, radius):
              super().__init__(color, is_filled)
              self.radius = radius

       def describe(self):
              super().describe()
              print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")

class Square(Shape):
       def __init__(self, color, is_filled, width):
              super().__init__(color, is_filled)
              self.width = width

       def describe(self):
              super().describe()
              print(f"It is a square with an area of {self.width ** 2}cm^2")

class Triangle(Shape):
       def __init__(self, color, is_filled, width, height):
              super().__init__(color, is_filled)
              self.width = width
              self.height = height
       
       def describe(self):
              super().describe()
              print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=5)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=10)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe()
```

# 35. Polymorphism
Greek word that means to "have many forms or faces" <br />
Poly = Many <br />
Morphe = Form

TWO WAYS TO ARCHIVE POLYMORPHISM
1. **Inheritance** = An object could be treated of the same type as a parent class
2. **Duck typing** = Object must have necessary attributes/methods

```py
from abc import ABC, abstractmethod

class Shape:
       
       @abstractmethod
       def area(self):
              pass


class Circle(Shape):
       def __init__(self, radius):
              self.radius = radius
       
       def area(self):
              return  3.14 * self.radius ** 2

class Square(Shape):
       def __init__(self, side):
              self.side = side
       
       def area(self):
              return  self.side ** 2

class Triangle(Shape):
       def __init__(self, base, height):
              self.base = base
              self.height = height

       def area(self):
              return  self.base * self.height / 2

class Pizza(Circle):
       def __init__(self, topping, radius):
              super().__init__(radius)
              self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
       print(f"{shape.area()}cm^2")
```

# 36. Duck typing
Another way to archive polymorphism besides inheritance <br />
Object must have the minimum necessary attributes/methods <br />
"If it looks like a duck and quacks like a duck, it must be a duck"

```py
class Animal:
	alive = True

class Dog(Animal):
	def speak(self):
		print("WOOF!")

class Cat(Animal):
	def speak(self):
		print("MEOW!")

class Car:
	alive = False

	def speak(self): #duck typing
	print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
	animal.speak()
	print(animal.alive)
```

# 37. Static methods
A method that belong to a class rather than any object from that class (instance) <br />
Usually used for general utility functions

**Instance methods** = Best for operations on instances of the class (objects). <br />
**Static methods** = Best for utility functions that do not need access to class data. <br />
**Class methods** = Best for class-level data or require access to the class itself <br />

**Instance Methods**
```py
# Instance methods
class Employee:
	
	def __init__(self, name, position):
		self.name = name
		self.position = position
	
	def get_info(self):
		return f"{self.name} = {self.position}"

employee1 = Employee("Eugune", "Manager")
print(employee1.get_info())
```
**Static methods**
```py
# Static methods
class Employee:

	@staticmethod
	def is_valid_position(position):
		valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
		return position in valid_positions


print(Employee.is_valid_position("Manager"))
```

# 38. Class methods
Allow operations related to the class itself <br />
Take (**cls**) as the first parameter, which represents the class itself.

**Instance methods** = Best for operations on instances of the class (objects). <br />
**Static methods** = Best for utility functions that do not need access to class data. <br />
**Class methods** = Best for class-level data or require access to the class itself <br />

```py
class Student:
	count = 0
	total_gpa = 0

	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa
		Student.count += 1
		Student.total_gpa += gpa

	#INSTANCE METHOD
	def get_info(self):
		return f"{self.name} {self.gpa}"

	@classmethod
	def get_count(cls):
		return f"Total # of students: (cls.count)"

	@classmethod
	def get_average_gpa(cls):
		if cls.count == 0:
			return 0
		else:
			return f"{cls.total_gpa / cls.count}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())
```

# 39. Magic methods
Dunder methods (double underscore) \_\_init\_\_, \_\_str\_\_, \_\_eq\_\_<br />
They are automatically called by many of Pyhton's built-in operations.<br />
They allow developers to define or customize the behavior of objects

```py
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}" # Replace the object memory address with a Custom String

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(slef, other):
        return self.num_pages < other.num_pages

    def __gt__(slef, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages} + {other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1) # str

print(book1 == book2) # eq

print(book2 < book3) # lt

print(book2 > book3) # gt

print(book2 + book3) # add

print("Lion" in book3) # contains

# getitem
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["description"])
```

# 40. @property
Decorator used to define a method as a property (it can be accessed like an attribute) <br />
Benefit: Add additional logic when read, write, or delete attributes <br />
Gives you getter, setter, and deleter method

```py
class Rectangle:
    def __init__(self, width, height):
        # _(underscore) means its a protected attribute
        self._width = width
        self._height = height
    
    # getter
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # setter
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # Deleter
    @width.deleter
    def width(self):
        del self._width
        print(Width has been deleted)

    @height.deleter
    def height(self):
        del self._height
        print(Height has been deleted)

rectangle = Rectangle(3, 4)

# Setter
rectangle.width = 5
rectangle.height = 6

# Getter
print(rectantle.width)
print(rectantle.height)

# Deleter
del rectangle.width
del rectangle.height
```

# 41. Decorators
A function that extends the behaviour of another function w/o modifying the base function
Pass the base function as an argument to the decorator

```py
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("chocolate")
```

# 42. Exception Handling
An event that interrupts the flow of a program <br />(ZeroDivisionError, TypeError, ValueError)
1. try
2. except
3. finally

```py

try:
    number = int(input("Enter a number")) # ValueError
    print(1 / number) # ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please!")
finally: # Execute regardless if theres an excption or not
    print("Do some cleanup here")
```

# 43. File Detection
```py
import os

file_path = "stuff/test.txt" # Relative path
# file_path = "C:/Users/HP/Desktop/test.txt" # Absolute path

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That location doesn't exist")
```
# 44. Writing Files

**output.txt**
```py
txt_data = "I like Pizza!"

file_path = "output.txt" # Relative path

# with statement
# For resource management and exception handling
# Simplifies working with resource like files, network connections and database connections by ensuring they are properly acquired and released.
# open(file, mode)

# Overwrite
with open(file=file_path, mode="w") as file:
       file.write(txt_data)
       print(f"txt file '{file_path}' was created")

# Write if this file doesn't exist
try:
       with open(file_path, "x") as file:
              file.write(txt_data)
              print(f"txt file '{file_path}' was created")
except FileExistError:
       print("That file already exist!")

# Append
try:
       with open(file_path, "a") as file:
              file.write("\n" + txt_data)
              print(f"txt file '{file_path}' was created")
except FileExistError:
       print("That file already exist!")
```
**output.txt | write a collection**
```py
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt"

try:
       with open(file_path, "w") as file:
              for employee in employees:
                     file.write(employee + "\n")
              print(f"txt file '{file_path}' was created")
except FileExistError:
       print("That file already exist!")
```
**output.json**
```py

import json

employee = {
       "name": "Spongebob"
       "age": 30,
       "job": "cook"
}

file_path = "output.json"

try:
       with open(file_path, "w") as file:
              json.dump(employee, file, indent=4) # Convert dictionary to a JSON String
              print(f"json file '{file_path}' was created")
except FileExistError:
       print("That file already exist!")
```
**output.csv**
```py

employees = [["Name", "Age", "Job"],
              ["Spongebob", 30, "Cook"],
              ["Patrick", 37, "Unemployed"],
              ["Snady", 27, "Scientist"]]

file_path = "output.json"

try:
       with open(file_path, "w", newline="") as file:
              writer = csv.writer(file)
              for row in employees:
                     writer.writerow(row)
              print(f"csv file '{file_path}' was created")
except FileExistError:
       print("That file already exist!")
```

# 44. Reading Files
**input.txt**
```py
file_path = "C:/Users/HP/Desktop/input.txt"

try:
       with open(file_path, "r") as file:
              content = file.read()
              print(content)
except FileNotFoundError:
       print("That file was not found")
except PermissionError:
       print("You do not have permission to read that file")
```
**input.json**
```py
import json

file_path = "C:/Users/HP/Desktop/input.json"

try:
       with open(file_path, "r") as file:
              content = json.load(file)
              print(content["job"])
except FileNotFoundError:
       print("That file was not found")
except PermissionError:
       print("You do not have permission to read that file")
```
**input.csv**
```py
import csv

file_path = "C:/Users/HP/Desktop/input.csv"

try:
       with open(file_path, "r") as file:
              content = csv.reader(file)
              for line in content:
                     print(line[0])
except FileNotFoundError:
       print("That file was not found")
except PermissionError:
       print("You do not have permission to read that file")
```

# 45. Datetime Module
```py
import datetime

date = datetime.date(2025, 1, 2) # 2025-01-02
today = datetime.date.today() # 2024-07-14

time = datetime.time(12, 30, 0) # 12:30:00
now = datetime.datetime.now() # 2024-07-14 09:41:55.409676

# Custom datetime string
now = now.strftime("%H:%M:%S %d-%m-%Y") # 09:44:10 07-14-2024

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
       print("Target date has passed")
else:
       print("Target has NOT passed")
```

# 46. Multithreading
Used to perform multiple tasks concurrently (multitasking)<br />
Good for I/O bound tasks like reading files or fetching data from APIs threading. <br />
Thread(target=my_function)
```py
import threading
import time

def walk_dog(first, last):
       time.sleep(8)
       print(f"You finish walking {first} {last}")

def take_out_trash():
       time.sleep(2)
       print("You take out the trash")

def get_mail():
       time.sleep(4)
       print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # passing arguments as tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=gat_mail)
chore3.start()

# Finish all chores
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
```

# 47. Request API data
```py
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
       url = f"{base_url}/pokemon/{name}"
       response = requests.get(url)

       if response.status_code == 200:
              pokemon_data = response.json()
              return pokemon_data
       else:
              print(f"Failed to retrive data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
       print(f"Name: {pokemon_info["name"].capitalize()}")
       print(f"Id: {pokemon_info["id"]}")
       print(f"Height: {pokemon_info["height"]}")
       print(f"Weight: {pokemon_info["weight"]}")
```
