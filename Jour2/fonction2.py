

def add(a,b):
    return a+b
    
def multi(a,b):
    return a*b
    
def div(a,b):
    if b==0:
        print("opp is not possible !!")
        return -1
    return a/b
    
def sous(a,b):
    return a-b

a = int(input("please insert the first value :\n"))
b = int(input("please insert the second value :\n"))

print("add => ",add(a,b),"\nmulti => ",multi(a,b),"\ndiv => ",div(a,b),"\nsous => ",sous(a,b))