contacts = [("Ada Lovelace", "08012345678", "ada@email.com"), ("David Guetta", "08011223344", "vidgue@gmail.com"), ("Chan BlaQ", "0815t374364", "chanblaq@yawuu.com")]
def find_contact(contacts, name):
    for each_contact in contacts:
        if name == each_contact[0]:
            return each_contact
        
def display_contact(contact):
    name, phone, email = contact
    print('Name: ', name)
    print('Phone: ', phone)
    print('Email: ', email)
display_contact(["Chan BlaQ", "0815t374364", "chanblaq@yawuu.com"])
print()

for all_contact in contacts:
    display_contact(all_contact)
print()
print(find_contact(contacts, 'David Guetta'))
print()

#gpsTracker
route = (("Ikeja", 6.6018, 3.3515, "08:00"), ("Berlin", 1.3245, 7.2683, '17:38'), ('Otukpo', 9.6782, 4.2873, '11:11'), ('Akwanga', 3.1420, 5.2314, '15:07'))
def total_checkpoints(route):
    return len(route)
print(total_checkpoints(route))
print()

def find_checkpoint(route, location_name):
    for each_route in route:
        if location_name == each_route[0]:
            return each_route
    else:
        return 'None'                                                                                                                                                 
print(find_checkpoint(route, 'Akwanga'))
print()

def display_route(route):
    for every_checkpoint in route:
        city, lat, lon, time = every_checkpoint
        print(f'{city} @ {time} - ({lat}, {lon})')

#Write a function first_and_last(route) that uses * extended unpacking to grab the first checkpoint, 
# the last checkpoint, and everything in between, then returns first and last as a tuple — i.e. return first, last. 
# (This combines extended unpacking and multi-value returns — both things you learned.)
def first_and_last(route):
    first, *between, last = route
    return first, last 

display_route(route)
print(first_and_last(route))