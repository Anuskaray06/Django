age=int(input("Enter your age: "))
if age>=0 and age<5:
    print("You are a kid")
elif age>=6 and age<=12:
    print("You are a child")
elif age>=13 and age<=19:
    print("You are a teenager")
elif age>=20 and age<=64:
    print("You are an adult")
elif age>=65:
    print("You are a senior citizen")
else:   
    print("Invalid age")
