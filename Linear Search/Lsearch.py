e=input("enter the element to be searched")
#L is the list

for i in range(len(L)):
    if e==i:
         print("found")
         break
else:
    print("not found")
