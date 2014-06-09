def is_prime(number):
    factors = range(2, number)
    if number == 1 or number == 0:
        return False
    for i in factors:
        if number == i:
            pass
        elif number % i == 0:
            return False
    return True

def prime_list(num):
    numbers = range(2, num)
    prime_numbers = []
    for i in numbers:
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

print "This is a program that generates prime numbers until you stop."
print "To stop generating numbers, press CTRL-D"
start = 3
other = 0
try:
    while True:
        x = prime_list(start)
        start += 1
        if other == x[-1]:
            continue
        else:
            print x[-1]
            other = x[-1]
            raw_input()
except EOFError:
    print "\nStopped printing. Goodbye!"

