import os
def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {phone}\n")
add_contact("21 Savage", "0801622382")
add_contact("Roddy Ricch", "0701276212")
add_contact("Guiseppe", "08196697382")

def show_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt") as file:
            for each_line in file:
                print(each_line.strip())
    else:
        print("No contacts yet")
show_contacts()

# open(filename, "w").close()  to clean append file(clear jammed data)
