""" convert integer to string"""

def convert(integer):
    binary=''

    while integer >0:
        rest = integer % 2
        integer = integer // 2
        #print(integer)
        if rest == 0:
            binary ='0' + binary
        elif rest ==1:
            binary = '1' + binary
    print(binary)


convert(22)
