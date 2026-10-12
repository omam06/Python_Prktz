# File handling is specifically the set of tools for writing data from RAM out to a file on disk, so it survives after the program ends, and reading it back in from disk into RAM the next time the program runs. is the process of opening, reading, writing, and closing files on disk, using the built-in open() function.
file = open("notes.txt", "w")
file.write("Wagwan")
file.close()

# pr1
file = open("greeting.txt", "w")
file.write("Hello, world!")
file.close()

#pr 2
file = open("greeting.txt", "r")   #.read() ull file content from disk to RAM
content = file.read()
print(content)
file.close()

#append mode
file = open("notes.txt", "a")
file.write("\nMy gee")
file.close()

file =  open("notes.txt", "r")
con = file.read()
print(con)       #my gee on nxt line
file.close()

print()

with open("greeting.txt", "a") as file:
    file.write("\nHow yall doing?")

with open("greeting.txt", "r") as file:
    akan = file.read()
    print(akan)
print()

#loop through a file line by line
with open("notes.txt", "r") as file:
    for lines in file:
        print(lines.strip())   #to remove newline @ front
print()

#checking if a file exists before taking action
import os
if os.path.exists("greeting.txt"):
    with open("greeting.txt", "a") as file:
        file.write("\nHope yo good")
    with open("greeting.txt", "r") as file:
        dav = file.read()
        print(dav)