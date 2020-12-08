numero1 = input("Please enter the first number :\n")
numero2 = input("Please enter the first number :\n")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)

    assert (numero1%2==0),"number 1 is odd !"
    assert (numero2!=0),"number 2 equals zero ! division is not possible"

    print("results =>  {} / {} = {}".format(numero1,numero2,numero1/numero2))
except AssertionError as e:
    print(e)
except:
    print("please enter a correct form of numbers")

