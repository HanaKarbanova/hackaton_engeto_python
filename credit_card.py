"""valid credit card number"""
card_number = '4012888888881881'
#int(input('credit card number:'))
"""reverse number ccn"""
reverse = card_number[::-1]
#print(reverse)
"""odd number from reverse ccn"""
odd = reverse[::2]
""" total odd number"""
total=0
for i in odd:
    total += int(i)


#print(odd)
"""total of multiple even number ccn by two"""
multiple=0

even=reverse[1::2]
for i in even:
    multiple= int(i)*2
    if multiple >9:
        total += (multiple - 9)
    else:
        total+=multiple


""" valid ccn by divisible by 10"""
if total%10 == 0 :
    print("credit card is valid!")
else:
    print("Credit card is'n valid!")
