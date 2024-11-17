list1 = [number for number in range(10)]
for item in list1:
    if(item > 3 and item <= 9):
        print(f"{item}th")     
    elif item == 1 :
        print("1st") 
    elif item == 2:
        print("2nd")
    elif item == 3 :
        print("3rd")
    else:
        print("false result !")        