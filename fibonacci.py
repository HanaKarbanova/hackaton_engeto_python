def fibonacci (iters, number1= 0, number2 = 1, ):
    print(number1 , number2)
    if iters <1:
        return
    else:
        return (fibonacci( iters-1,number2, number1+number2))



print(fibonacci(10))
