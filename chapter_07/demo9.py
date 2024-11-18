sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
     
# 可如下，但不可用for修改迭代器   
# sandwich_orders = [item for item in sandwich_orders if item != 'pastrami']  

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    print(f"I made your {current_sandwich} sandwich.")  
    finished_sandwiches.append(current_sandwich)  

print("\nAll the sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
