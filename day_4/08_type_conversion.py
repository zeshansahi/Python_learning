x=10
y=10.2
z="zeshan"


# implicit type conversion
x=x*y
print(type(x))

# explicit type conversion
age=input("what is yor age")
print("Age type",type(age))
# above will show the type string

age=int(age)
print("Age type",type(age))
