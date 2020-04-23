def List_Examples():
    # Example 1
    squares = [1, 4, 9, 16, 25]
    print("\nThe list square is initialized as", squares)
    print('\nThe value at index squares[0] is', squares[0])
    print('\nThe value at index squares[-1] is', squares[-1])
    print('\nList "slice operations" are shown next.\n'
          'The value at index squares[-3:] is', squares[-3:])
    print('\nThe value at index squares[2:4] is', squares[2:4])
    print('\nConcatenation of a list like "squares + [36, 49, 65, 81, 100]" '
          '\nresults in:', squares + [36, 49, 65, 81, 100])
    print('\nNOTE: This does not alter the list, it simply adds to the displayed values.')
    squares = squares + [36, 49, 65, 81, 100]
    print('\nTo add the new list by "squares = squares + [36, 49, 65, 81, 100]"'
          '\nwhich results in squares equaling', squares)
    print('\nLists are "mutable" so they may be changed. \n'
          'To change an element like "squares[5] = 64., '
          '\nNow the list squares is corrected to read', squares)
    squares.append(11**2)
    print('\nYou can append an element to a list by using the append method, \nfor example:'
          '"squares.append(11**2)" results in the flllowing:', squares)

    cubes = []
    i = 0
    while i < 7:
        i = i + 1
        cubes.append(str(i) + ' cubed is ' + str(i ** 3))
    print("\nYou can populate a list using the append method "
          "in a while statement. \nShown in the cubes list.\n", cubes)

    cubes[2:5] = []
    print('\nYou can remove items from a list by splicing, for example'
          '\n"cubes[2:5]=[] will result in:\n',
          cubes)
    print("\nNOTE: It removed the index 2, 3, and 4 items "
          "i.e. cubes for 3, 4,& 5.  \n\tIncluding index 2 but excluding index 5.")




