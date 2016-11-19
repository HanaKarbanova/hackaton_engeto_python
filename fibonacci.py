def fibonacci (n):
    if n==1:
        return 1
    if n==0:
        return 0
    return (fibonacci(n-1) + fibonacci(n-2))


#print(fibonacci(10))


def fib_gen(n=None):
    now, last = 0, 1
    while True:
        yield last
        now, last = last, now+last

def fib_print():
    for i in fib_gen():
        print(i)
        if i > 1000:
            break
