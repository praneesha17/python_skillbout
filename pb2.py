li=[]
for i in range(5):
    a=int(input("Enter a number:"))
    li.append(a)
print("Reverse: ",li[::-1])
print("Sum:",sum(li))
print("Avg:",sum(li)//5)