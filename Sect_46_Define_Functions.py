def fibonacci_series(n):  # 'def' means define, fib is the function name, n is the argument
    """The first statement of the function body can optionally be a string literal;
    this string literal is the function’s documentation string, or docstring. . """
    result = []     # Declares an empty list
    a, b = 0, 1     # Declares two variables and assigns them initial
    # values, a == 0 and b == 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    print[result]
    return result



f = fibonacci_series  #You can assign the method name to variable, and then say f(n).

"""
    * The 'return' statement returns with a value from a function. 
        'return' without an expression argument returns 'None'. 
        Falling off the end of a function also returns 'None'.

    *The statement 'result.append(a)' calls a method of the list object 'result'. 
        A method is a function that ‘belongs’ to an object and is 
        named 'obj.methodname', where 'obj' is some object (this may be an expression),
        and 'methodname' is the name of a method that is defined by the object’s type. 
        Different types define different methods. Methods of different types may 
        have the same name without causing ambiguity. 
        (It is possible to define your own object types and methods, 
        using classes, see Classes) 
        
    *The method 'append()' shown in the example is defined for list objects; 
        it adds a new element at the end of the list. In this example it is 
        equivalent to 'result = result + [a]', but more efficient.
"""

