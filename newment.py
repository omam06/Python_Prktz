resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}  
borrow_records = []
borrow_log = []           #logs every successful borowwing

# add resources
def add_resource(resource_id, name, category, total):
    available = total
    for each_resource in resources:
        if each_resource['id'] == resource_id:
            raise ValueError("ID already exists!")         
    new_resource = {'id': resource_id, 'name': name, 'category': category, 'total': total, 'available': available}
    resources.append(new_resource)
    

#list resources
def list_resources():
    for each_resource in resources:
        print(each_resource)

#subsequent requirements will need
def find_resource(resource_id):
    for each_resource in resources:
        if each_resource['id'] == resource_id:
            return each_resource
    return None

# borrow
def borrow_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        raise ValueError("Rejected: Fellow NOT in our list")
    resource = find_resource(resource_id)
    if resource is None:
        raise ValueError("Rejected: Resource NOT in stock")
    if isinstance(quantity, int) is False:
        raise ValueError("Rejected: Quantity requested is NOT a valid number")
    if quantity <= 0:
        raise ValueError("Rejected: Quantity requested MUST be greater than Zero")
    if quantity > resource['available']:
        raise ValueError("Rejected: Sorry, Insufficient Quantity!")
    resource['available'] -= quantity              #reduce availability, runs when borrowing pass all checks

    found = False                               #update borrow record, original available reduces
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            record["quantity"] += quantity
            found = True
    if found == False:
        new_record = {"fellow_id": fellow_id, "resource_id": resource_id, "quantity": quantity}
        borrow_records.append(new_record)
       
    borrow_log.append({'fellow_id': fellow_id, "resource_id": resource_id, "quantity": quantity})


#returns 
def return_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        raise ValueError("Rejected: Fellow NOT in our list")
    resource = find_resource(resource_id)
    if resource is None:
        raise ValueError("Rejected: Resource NOT in stock")
    if isinstance(quantity, int) is False:
        raise ValueError("Rejected: Quantity requested is NOT a valid number")
    if quantity <= 0:
        raise ValueError("Rejected: Quantity requested MUST be greater than Zero")
    
    matching_record = None
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            matching_record = record

    if matching_record is None or matching_record["quantity"] < quantity:
        raise ValueError(f"Rejected: cannot return more than {fellow_id} has on loan")
    matching_record['quantity'] -= quantity
    resource['available'] += quantity
    if matching_record['quantity'] == 0:
        borrow_records.remove(matching_record)
           

#search/filter
def search_resources(search_name, filter_category):
    found_resources = []
    for each_resource in resources:
        if search_name != "":
            if search_name.lower() not in each_resource['name'].lower():
                continue
        if filter_category != "":
            if filter_category.lower() not in each_resource['category'].lower():
                continue
        found_resources.append(each_resource)
    return found_resources

#report
def generate_report():
    total_units = 0
    available_units = 0
    low_stock_items = []
    
    for each_resource in resources:
        total_units = total_units + each_resource["total"]
        available_units = available_units + each_resource["available"]
        
        if each_resource["available"] < 3:
            low_stock_items.append(f"{each_resource['name']} ({each_resource['available']})")
            
    borrowed_units = total_units - available_units     

    #using simple tally dictionary to count borrowed items
    borrow_tallies = {}
    for each_resource in resources:
        borrow_tallies[each_resource["id"]] = 0 
        
    for record in borrow_records:
        item_id = record["resource_id"]
        borrow_tallies[item_id] = borrow_tallies[item_id] + record["quantity"]
        
    highest_borrow_count = 0
    for item_id in borrow_tallies:
        if borrow_tallies[item_id] > highest_borrow_count:
            highest_borrow_count = borrow_tallies[item_id]

    
    most_borrowed_items = []
    if highest_borrow_count > 0:
        for item_id in borrow_tallies:
            if borrow_tallies[item_id] == highest_borrow_count:
                matched_resource = find_resource(item_id)
                if matched_resource is not None:
                    most_borrowed_items.append(matched_resource["name"])
    print("--- INVENTORY REPORT ---")                
    print("Total units:", total_units)
    print("Available units:", available_units)
    print("Borrowed units:", borrowed_units)
    if low_stock_items:
        print("Low stock:", ", ".join(low_stock_items))
    else:
        print("Low stock: None")
    if most_borrowed_items:
        print("Most borrowed:", ", ".join(most_borrowed_items), f"({highest_borrow_count})")
    else:
        print("Most borrowed: No resources currently borrowed")

#Required Demonstration in Order
list_resources()                          # starting inventory

borrow_resource("F001", "R001", 2)        # step 1
print(find_resource("R001"))

borrow_resource("F002", "R002", 3)        # step 2
print(find_resource("R002"))

return_resource("F001", "R001", 1)        # step 3
print(find_resource("R001"))

try:                                      # step 4
    borrow_resource("F003", "R003", 4)
except ValueError as e:
    print(e)
print(find_resource("R003"))

try:                                      # step 5
    return_resource("F002", "R002", 4)
except ValueError as e:
    print(e)
print(find_resource("R002"))

print(search_resources("LAPtop", ""))     # step 6

print()
generate_report()                         # step 7
print()

#EXTRA TESTS
print(search_resources("", "accessories"))        # category filter

try:                                              # invalid input test
    borrow_resource("F001", "R001", 2.5)
except ValueError as e:
    print(e)

add_resource("R004", "Mouse", "Electronics", 7)   # to add new resource
list_resources()

try:                                              # to reject duplicate ID 
    add_resource("R001", "Tablet", "Electronics", 2)
except ValueError as e:
    print(e)


#to put the program in a menu
def menu():
    while True:
        print()
        print("Select an operation from the following")
        print("1. Add Resource")
        print("2. List Resources")
        print("3. Borrow Resource")
        print("4. Return Resource")
        print("5. Search For a Resource")
        print("6. See Report")
        print("0. Exit")
        choice = input("Choose an Option: ")
        if choice == "1":
            try:
                resource_id = input("Resource ID: ")
                name = input("Resource Name: ")
                category = input("Category: ")
                total = int(input("Total: "))
                add_resource(resource_id, name, category, total)
                print("Resource Added")
            except ValueError as e:
                print(e)
        elif choice == "2":
            print("Here's a List of All Resources:")
            try:
                list_resources()
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                fellow_id = input("Fellow ID: ")
                resource_id = input("Resource ID: ")
                quantity = int(input("Quantity: "))
                borrow_resource(fellow_id, resource_id, quantity)
                print("Borrowed successfully.")
            except ValueError as e:
                print(e)
        elif choice == "4":
            try:
                fellow_id = input("Fellow ID: ")
                resource_id = input("Resource ID: ")
                quantity = int(input("Quantity: "))
                return_resource(fellow_id, resource_id, quantity)
                print("Returned successfully.")
            except ValueError as e:
                print(e)
        elif choice == "5":
            try:
                search_name = input("Resource Name: ")
                filter_category = input("Resource Category: ")
                search_result = search_resources(search_name, filter_category)
                if search_result:
                    print(search_result)
                else:
                    print("No matches found")
                
            except ValueError as e:
                print(e)
        elif choice == "6":
            generate_report()
        elif choice == "0":
            break
        else:
            print("Invalid Option. Try Again!")
menu()