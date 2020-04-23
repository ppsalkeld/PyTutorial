def if_statement():
    x = int(input("Enter an integer: "))    # input returns a str; made an int
    if x < 0:
        x = 0
        print("Negative and changed to zero.")
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')