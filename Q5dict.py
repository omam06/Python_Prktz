# # forehand knowledge
# def check_positive(n):
#     if n < 0:
#         raise ValueError('Must be positive')
#     return n 
# # print(check_positive(5))  call if twil pass

# try:
#     check_positive(-3)
#     assert False, 'ValueError was not raised for a negative number'
# except ValueError:
#     # 'ValueErrors packed up, the code caught the issue'
#     pass
# print()
#5 proper
def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if item not in stock:
            raise ValueError('Item NOT in stock!')
        
        elif quantity <= 0:
            raise ValueError('Order quantity must NOT be of negative value or ZERO')

        elif quantity > remaining[item]:
            raise ValueError("Insufficient stock")
        
        remaining[item] = remaining[item] - quantity
    return remaining   #since all errors are raised, nothing is returned to remaining upon failre
stock = {"pen": 5}
order = []

assert reserve_stock({"pen": 8}, [("pen", 3), ("pen", 3)]) == {'pen': 2}
try:
    reserve_stock(stock, [("pen", 3), ("pen", 3)])
    assert False, 'Didnt catch ValueError for insufficient stock'
except ValueError:
    pass
assert stock == {'pen': 5}

