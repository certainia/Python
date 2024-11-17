list1 = ['fan','heng','jia','niu','bi']
list1.insert(0,'feng')
list1.insert(3,'gong')
list1.append('zi')

print("Sorry,the table can only take two person of you,I will pop others later.")

leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")
leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")
leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")
leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")
leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")
leave = list1.pop()
print(f"Sorry {leave},I'd like you leave my house.")

print(f"{list1[0]} ,congratulations!")
print(f"{list1[1]} ,congratulations!")

del list1[0]
del list1[0]   # 递进一位

# if not list1:   # 判空
#     print("Nothing.")

print(list1)
