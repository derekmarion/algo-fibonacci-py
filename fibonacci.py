def fibonacci(n):
    fib = [0, 1] # seed first two numbers in fibonacci sequence
    if n <= 1:  # handle cases where n is 0 or 1
        return fib[n]
    i = 2
    while i <= n:  # build fib sequence up to place n
        current_value = fib[i - 2] + fib[i - 1]
        fib.append(current_value)
        i += 1
    return fib[-1]  # return last value of fib sequence
