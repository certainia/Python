sandwich_orders = ['tuna', 'chicken', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # So good!If you take it ,just pop and remove it.
    print(f"I made your {current_sandwich} sandwich.")  
    finished_sandwiches.append(current_sandwich) 

print("\nAll the sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
