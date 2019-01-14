thislist=["apple","banana","cherry"]
print(thislist)
thislist[1]="grapes"
print(thislist)
if "apple" in thislist:
  print("yes")
print(len(thislist))
thislist.append("orange")
thislist.insert(1,"banana")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
print(thislist[0:2])
