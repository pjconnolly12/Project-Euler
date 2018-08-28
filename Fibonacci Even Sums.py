def f(num):
    first = 0
    second = 1
    counter = 0
    for i in range(0,int(num/2)):
        first += second
        second += first
        if first > 4000000 or second > 4000000:
            break
        if first % 2 == 0:
            counter += first
        if second % 2 == 0:
            counter += second
    return counter

