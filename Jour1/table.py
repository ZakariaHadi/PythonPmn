

for j in range(1, 11):
    print("********** table de ",j," ********")
    for i in range(1, 11):
        print(j, 'x', i, '=', j*i)

def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        res = Fibonacci(n-1)+Fibonacci(n-2)
        print(n)
        return res
  
Fibonacci(10)