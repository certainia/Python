names = ['John','admin','Joe','Mary','lufei']
if not names:
    print("We need to find some users.")
    
for i in range(len(names)): 
    names.pop()
    
if not names:
    print("We need to find some users.")