# Problem 3 (slightly harder): Given 
# use a list comprehension to create a list of the lengths of each word.
words = ["hi", "python", "ai", "engineer"]
lnt = []
for word in words:
    lnt.append(len(word))
print(lnt)
lnt = [len(word) for word in words]
print(lnt)
print()

words = ["hi", "ai"]
each = []
for word in words:
    for letter in word:
        each.append(letter)
print(each)
each = [letter for word in words for letter in word]
print(each)
print()

numbers = [1, 2, 3, 4, 5]
label = ['even' if num%2 == 0 else 'odd' for num in numbers]
print(label)
print()

#Write a recursive function count_down(n) that prints numbers from n down to 1, then prints "Liftoff!". 
#(Hint: base case is n == 0, recursive case calls count_down(n - 1).)

def count_down(n):
    if n == 0:
        print('Liftoff!')
    else:
        print(n)
        count_down(n - 1)
count_down(8)
print()

# write a nested list comprehension that flattens it into a single list: [1, 2, 3, 4, 5, 6].
matrix = [[1, 2], [3, 4], [5, 6]]
flat = []
for numbers in matrix:
    for number in numbers:
        flat.append(number)
print(flat)
flat = [number for numbers in matrix for number in numbers]
print(flat)
print()

#Write a recursive function sum_up_to(n) that returns the sum of all numbers from 1 to n.
#  E.g. sum_up_to(5) should return 15 (1+2+3+4+5). Identify your base case and recursive case.
def sum_up_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_up_to(n-1)
res = sum_up_to(5)
print(res)
print()

sentence = "I love coding"
new = sentence.split()
print(len(new))
print()

def is_even(number):
    return number % 2 == 0
dum = is_even(7)
print(dum)
print()

#write print_info(**kwargs) that prints each key-value pair on its own line, like name: Ada.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print_info(name= 'Bassey', club= 'Fulham')
print()

def outer():
    count = 0
    def inner():
        print(count)
    count = 5   # changed AFTER inner is defined, BEFORE inner is called
    return inner

greet = outer()
greet()  # prints 5, not 0 — proves it's a live reference, not a copy