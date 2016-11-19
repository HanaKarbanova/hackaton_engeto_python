def convert (number, base):

    decimal = 0
    for digit in number:
        decimal= decimal * int(base) + int(digit, base)
    return(decimal)

print(convert(input('Input number:'), int(input('Input base:'))))

#def test_converts():
    #assert convert('10', 10) == 10
    #assert convert('1010', 2) == 10
    #assert convert('FF', 16) == 255
