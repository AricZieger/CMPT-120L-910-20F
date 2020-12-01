def prime_or_composite(number):
   
    from math import sqrt
    from math import ceil

    number = int(number)
    is_prime = True
    if number <= 1:  
        is_prime = False
    else:
        for divisor in range(2, ceil(sqrt(number))):
            if number % divisor == 0:
                is_prime = False
                break
    return("Prime" if is_prime else "Composite")

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201, -7, 47055833459]

    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)