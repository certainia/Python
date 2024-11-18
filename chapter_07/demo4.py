item = 'nothing'
while True:
    message = input("what would you like: ")
    if message != 'quit':
        print(f"Ok,I will take{message}.")
    else:
        print("Ok,I will take all of them.")
        break
    