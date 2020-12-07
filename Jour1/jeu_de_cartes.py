#coding:utf-8

defined_Cards = ('1','2','3','4','5','6','7','8','9','10','J','Q','K','A')
set_card = []
while True:
    number = str(input("Enter card number: (zero to exit) "))
    if number == '0':
        break
    elif number not in defined_Cards:
        print('Please enter a correct number')
    else:
        set_card.append(number)


print('Here is your list ==> ',set_card)   