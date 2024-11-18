details = {'fan':'yes','ding':'yes','hu':'yes','zhu':'yes'}
list1 = ['ding','hu','zhu']
for item in details.keys():
    if item in list1:
        print(f"{item},thanks!") 
    else:
        print(f"{item},please take it!")
    
