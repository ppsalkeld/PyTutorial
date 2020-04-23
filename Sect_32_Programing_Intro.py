def fibonacci(self):  # self: the maximum value calculated.
    a, b = 0, 1
    print('\nFibonacci numbers less than', self, end=": ")
    while a < self:
        print(a, end=',')   # 'end' replaces the default new line after print() executes
        a, b = b, a + b  # Example of multiple assignment, values assigned to a & b
    print("that's all folks!")
