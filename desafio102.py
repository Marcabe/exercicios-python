def factorial(n, show=False):
    f = 1

    if show:
        print(f'{n}! = ', end='')

    for i in range(n, 0, -1):
        f *= i

        if show:
            print(i, end='')

            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

    return f


print(factorial(5, False))