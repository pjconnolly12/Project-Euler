def f(num):
    first = 0
    second = 1
    for i in range(0,num):
        first, second = second, first + second
        if first > 1000:
            break
    return i + 1
