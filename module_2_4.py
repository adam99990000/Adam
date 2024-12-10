numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number_ in numbers:
    is_prime = True
    if number_ > 1:
        for i in range(2, number_):
            if number_ % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number_)
        else:
            not_primes.append(number_)
print('Primes', primes)
print('Not Primes', not_primes)
