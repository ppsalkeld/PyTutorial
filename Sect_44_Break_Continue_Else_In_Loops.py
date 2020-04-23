def prime_numbers(start, stop):
    b = start
    e = stop
    for n in range(b, e):  # each loop generates an n starting from b to (1-e)
        for x in range(b, n):  # each loop generates an x starting from b to (1-n)
            # thus n would be excluded on the first loop when n = b thus the 'for' statement fails
            # and n goes directly to 'else' statement on the first loop. A loop’s else clause runs
            # when no break occurs.
            if n % x == 0:
                print('\n\t', n, 'equals', x, '*', n // x)  # Using // keeps the results an integer
                break
        else:
            # loops fell through without finding a factor
            print('\n\t', n, 'is a prime number')

def loop_continue(start, stop):
    a = start
    b = stop
    for num in range(a, b):
        if num % 2 == 0:
            print(num, "is an EVEN number.")
            continue
        print(num, 'is an ODD number')
