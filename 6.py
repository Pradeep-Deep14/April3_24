def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))


#step wise movement
#finally returns 8
