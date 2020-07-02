def gen_fibonacci(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

for no in gen_fibonacci(5):
    print(no)