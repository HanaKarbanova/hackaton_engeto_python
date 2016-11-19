def faktorial(number):
    if number <= 1:
        return 1
    else:
        return(number*faktorial(number-1))

print (faktorial(5))
