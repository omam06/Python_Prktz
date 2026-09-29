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
print()

#Write a recursive function count_down_list(lst) that takes a list and returns the total count of items in it — 
# basically reimplementing len() yourself, recursively, without using len().
#E.g. count_down_list([10, 20, 30, 40]) should return 4
def count_down_list(lst):
    if lst == []:
        return 0
    else:
        return 1 + count_down_list(lst[1:])
print(count_down_list([10, 20, 30, 40])) 
print()

#Write a recursive function count_evens(lst) that returns how many even numbers are in a list.
#  E.g. count_evens([1, 2, 3, 4]) returns 2.
# This one has a twist: an item contributes 1 only if it's even, and 0 otherwise. 
# Start with the base case, then think about what lst[0] contributes in each situation.
# An if/else in the recursive branch will help.
def count_evens(lst):
    if lst == []:
        return 0
    elif lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:]) # If lst[0] is even, it adds 1, plus the count of evens in the rest.
    else:
        return 0 + count_evens(lst[1:])  # If lst[0] is odd, it adds 0, so the answer is just the count of evens in the rest. 
print(count_evens([1, 2, 3, 4, 5, 6]))
print()

# Write a recursive function count_word(words, target) that returns how many times target appears in a list of strings. 
# For example, count_word(["hi", "yo", "hi"], "hi") returns 2
def count_word(words, target):
    if words == []:
        return 0
    elif words[0] == target:
        return 1 + count_word(words[1:], target)
    else:
        return 0 + count_word(words[1:], target)
print(count_word(["hi", "yo", "hi"], "hi"))
print()

#Write a recursive count_long(words) that returns how many words in a list have more than 3 letters. 
# For example, count_long(["hi", "python", "cat", "engineer"]) returns 2
def count_long(words):
    if words == []:
        return 0
    elif len(words[0]) > 3:
        return 1 + count_long(words[1:])
    else:
        return 0 + count_long(words[1:])
print(count_long(["hi", "python", "cat", "engineer"]))
print()

#write a list comprehension that 
# returns only the words longer than 4 characters.
words = ["apple", "kiwi", "banana", "fig"]
longer = []
for word in words:
    if len(word) > 4:
        longer.append(word)
print(longer)
jabor = [word for word in words if len(word) > 4]
print(jabor)
print()

#given ,
#  write code that uses .index() to find the position of "two" in the tuple, and print it.
data = (1, "two", 3.0, True)
print(data.index('two'))
print()

#write a function describe(**kwargs) that returns True if the keyword argument status was passed with the value "active", and False otherwise.
# That includes the case where status wasn't passed at all.

def describe(**kwargs):
    return kwargs.get('status') == 'active'

print(describe(status="active"))
print(describe(status='offline'))
print(describe(city= 'bueno aires'))
print(describe(club= 'active'))