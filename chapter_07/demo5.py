message = int(input("how old are you : "))
if message > 0:
    if(message<3):
        print("free of charge.")
    elif(message<12):
        print("10 dollors.")
    else:
        print("15 dollors.")
else:
    print("Sorry,run away.")
