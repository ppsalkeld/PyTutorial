def math_examples():
    """
    There are two types of numbers discussed here, integer and
    floating point. Python also supports decimal, fraction, and
    complex.  Complex numbers use the j or J suffix to indicate
    imaginary part(e.g. 3+5j).

    The math in these examples are built-in.
    """
    ex_1 = 2 + 2
    print("\n2 + 2 =", ex_1, 'The result is an integer')

    ex_2 = 17 / 5
    print('\n17 divided by 5 = ', ex_2, 'Division always results in a floating point.')

    ex_3a = 17 // 3  # Floor division discards the fractional part.
    ex_3b = 17 % 3  # The modulo operator # gives the remainder.
    print('\n17 divided by 3 equals', ex_3a, 'with a remainder of', ex_3b,
          '. \nThis an example of floor division and the modulo operator.')

    """
    There is full support for floating point; 
    operations with mixed type operands convert the 
    integer operand to floating point.
    """
    ex_4 = 4 * 3.75 - 1
    print("\nMixed operand expression '4 * 3.75 - 1 '",
          "\nreturns a floating point: ", ex_4)

    ex_5 = 0
    print('\nFibonacci Numbers less than ten:')
    (a,b) = [ex_5,1]

    while a<10:
        print(a)
        (a, b) = [b, a + b]



