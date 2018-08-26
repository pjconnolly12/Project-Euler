#Largest Prime Factor

def largest(num):
    number = num
    divisor = 2
    answer = 0
    while divisor <= number:
        if number % divisor != 0:
            divisor += 1
        else:
            answer = divisor
            number /= divisor
            divisor = 2
    return answer

print(largest(600851475143))
