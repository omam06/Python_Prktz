route = (
    ("Zagreb", 6.6018, 3.3515, "11:11"),
    ("Minsk", 6.6018, 3.3515, "08:00"),
    ("Tel Aviv", 6.5096, 3.3711, "08:30"),
    ("Budapest", 6.4500, 3.5500, "09:15")
)
def total_checkpoints(route):
    return len(route)
def find_checkpoint(route, location_name):
    for each_route in route:
        if each_route[0] == location_name:
            return each_route
    return None
def display_route(route):
    for each_route in route:
        place, latitude, longitude, time = each_route
        print(f'{place} @ {time} - ({latitude}, {longitude})')
print()
def first_and_last(route):
    first, *middle, last = route
    return first, last
total = total_checkpoints(route)
print(total)
print()
find = find_checkpoint(route, 'Budapest')
print(find)
print()
display_route(route)
print()
firstlast = first_and_last(route)
print(firstlast) 