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
            raise ValueError("ID already exists!")      #reject duplicate IDs
    
    new_resource = {'id': resource_id, 'name': name, 'category': category, 'total': total, 'available': available}
    resources.append(new_resource)
    return resources
print(add_resource('R004', 'Mouse', 'Electronics', 7))
print()

try:
    add_resource("R001", "Tablet", "Electronics", 2)
except ValueError:
    print('Rejected: ID alrready exists!')

print()

#list resources
def list_resources():
    for each_resource in resources:
        print(each_resource)
list_resources()

print()

#subsequent requirements will need
def find_resource(resource_id):
    for each_resource in resources:
        if each_resource['id'] == resource_id:
            return each_resource
    return None
print(find_resource('R004'))
print(find_resource('R007'))

print()

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

borrow_resource("F001", "R001", 2)       # required demonstration 1
print(find_resource("R001"))
print(borrow_records)
print(borrow_log)
try:                                             #to prove that rejected attempts dont mutate state
    borrow_resource("F003", "R002", 6)
except ValueError:
    print('Rejected: Sorry, Insufficient Quantity')   
print(find_resource('R002'))         
print(borrow_records)                #all remain same
print(borrow_log)

print()

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
        raise ValueError("Rejected: Sorry, Insufficient stock!")
    #in place of insuffucuent stock

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
borrow_resource("F002", "R002", 3)           # required demonstration 2
try:
    borrow_resource("F003", "R003", 4)
except ValueError:
    print()
print(find_resource("R002"))       

return_resource("F001", "R001", 1)               # required demonstration 3
print(find_resource("R001"))     
print(borrow_records)              

try:            # required demonstration 5
    return_resource("F002", "R002", 4)
except ValueError:
    print('Rejected: Sorry, Insufficient stock!')
print(find_resource("R002"))
print(borrow_records)              

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
print(search_resources('LAPtop', ''))    #required demonstration 6

print()

#report
def generate_report():
    total_units = 0
    available_units = 0
    low_stock_items = []
    
    for each_resource in resources:
        total_units = total_units + each_resource["total"]
        available_units = available_units + each_resource["available"]
        
        if each_resource["available"] < 3:
            low_stock_items.append(each_resource["name"])
            
    borrowed_units = total_units - available_units      # Calculate currently borrowed units

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
print()
generate_report()

    #  Print out the final compiled metrics simply
print("--- SYSTEM SUMMARY REPORT ---")
print("Total Portfolio Inventory Units:", total_units)
print("Total Units Available in Stock :", available_units)
print("Total Units Currently Borrowed :", borrowed_units)
print("Low Stock Resources (<3 units) :", low_stock_items)
print("Most Borrowed Resource(s)      :", most_borrowed_items)
