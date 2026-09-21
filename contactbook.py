contacts = [('21 Savage', '8011223344', '21savage@glenwood.com'), ('Tay Keith', '8161427133', 'taykeith@yawuu.com'), ('Metro Boomin', '7021638125', 'yungmetro@gmail.com')]
def find_contact(contacts, name):
    for each_contact in contacts:
        if each_contact[0] == name:
            return each_contact
def display_contact(contact):
        name, phone, email = contact
        print(name)
        print(phone)
        print(email)
display_contact(('Tay Keith', '8161427133', 'taykeith@yawuu.com'))
print()
for contact in contacts:
    display_contact(contact)
print()
result = find_contact(contacts, 'Metro Boomin')
print(result)