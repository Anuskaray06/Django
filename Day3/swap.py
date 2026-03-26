a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("before swapping a={} and b={}".format(a,b))
a=a+b
b=a-b
a=a-b
print("after swapping a={} and b={}".format(a,b))
