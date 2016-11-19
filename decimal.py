""" convert binary to decimal"""

def convert (binary):
    decimal=0
    for digit in binary:
        decimal= decimal * 2 + int(digit)
    print(decimal)

convert('10110')
