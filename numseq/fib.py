fib_array = [0,1]

def fib(n):
    if n<0:
        print("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fib(n-1)+fib(n-2)
        fib_array.append(temp_fib)
        return temp_fib