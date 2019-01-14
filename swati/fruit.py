address=["Flat floor street","18","New York"]
pins={"Mike":1234,"Joe":1111,"Jack":2222}
print(address[0],address[1])

pin=int(input("enter your pin:"))

def find_in_file(f):
    myfile=open("sample.txt")
    fruits=myfile.read()
    fruits=fruits.splitlines()
    if f in fruits:
      return"that fruit is in the list"
    else:
       return"no such fruit found" 

if pin in pins.values():
    fruit=input("enter fruit:")
    print(find_in_file(fruit))
else:
   print("Incorrect pin!")
 
