# funcation without prams
def printCodanics():
    text="we are learing with ammar"
    print(text)
 
 #  funcation with prams
def ageCalculator(age,text):
    if age==5:
        print("Hammad can join the school")
    elif age>5:
        print("hammad should go to heigher school")
    else:
        print("Hammad is still a baby")

# here is the funcation with return
def future_age(age):
    newAge=age+12
    return newAge
    
printCodanics()
 

ageCalculator(5,"text")
print(future_age(30))