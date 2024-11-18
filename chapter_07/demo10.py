vacation_poll = {}

polling_active = True

while polling_active:
    
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    vacation_poll[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ").lower()
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")    # 调查结果
for name, place in vacation_poll.items():
    print(f"{name} would like to visit {place}.")
