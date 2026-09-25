#3: flatten 
# into [1, 2, 3, 4, 5, 6] using a nested list comprehension.
matrix = [[1, 2], [3, 4], [5, 6]] 
flat = []
for numbers in matrix:
    for number in numbers:
        flat.append(number)
print(flat)
flat = [number for numbers in matrix for number in numbers]
print(flat)
print()

#Write a recursive function count_down(n) that prints numbers from n down to 1, then prints "Liftoff!". 
# (Hint: base case is n == 0, recursive case calls count_down(n - 1).)
def count_down(n):
    if n == 0:
        print('Liftoff!')
    else:
        print(n)
        count_down(n-1)
count_down(17)
print()

#factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))
print()

#Write a recursive function sum_up_to(n) that returns the sum of all numbers from 1 to n.
#E.g. sum_up_to(5) should return 15 (1+2+3+4+5). Identify your base case and recursive case.
def sum_up_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_up_to(n-1)
print(sum_up_to(5))
print()
sentence = "I love coding"
jabo = sentence.split(' ')
print(len(jabo))
print()

#Write a function add_all(*args) that returns the sum of however many numbers are passed in.
#(Hint: you can loop through args like any tuple, or think about a built-in that sums iterables.)
def add_all(*args):
    return sum(args)
print(add_all(12, 7, 21))
print()

#Write a function print_info(**kwargs) that prints each key-value pair on its own line, like name: Ada.
#  (Hint: think about how you'd loop through a dictionary's key-value pairs.)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print_info(name= 'Bassey', club= 'Fulham')
print_info()

count = 0
def increment():
    count = 7
    count = count + 1
    print(count)
increment()
print(count)
print()

#lmbdaXfilter
numbers = [1, 2, 3, 4, 5]
ogbeee = map(lambda x: x ** 2, numbers)
print(list(ogbeee))
iyooo = filter(lambda x: x > 10, map(lambda x: x ** 2, numbers))
print(list(iyooo))
print()

#Tuples are commonly used when a function needs to return more than one value. Write a function min_max(numbers) that takes a list of numbers 
# and returns both the minimum and maximum as a tuple. E.g. min_max([3, 7, 1, 9, 4]) should return (1, 9).
#  (Hint: you can use the built-ins min() and max() — just return both together separated by a comma.)
def min_max(anambers):
    return min(anambers), max(anambers)
print(min_max([3, 7, 1, 9, 4]))
print()

#Write a recursive function power(base, exp) that calculates base raised to exp (like base ** exp), without using the ** operator. 
# E.g. power(2, 4) should return 16. Identify your base case first.
def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)
print(power(2, 4))