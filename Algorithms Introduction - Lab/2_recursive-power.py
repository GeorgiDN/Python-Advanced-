def recursive_power(n):
    if n == 1:
        return n

    return n * recursive_power(n-1)


num = int(input())
print(recursive_power(num))
