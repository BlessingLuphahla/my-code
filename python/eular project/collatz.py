stopping_time = 0


def conjecture(x):
    global stopping_time
    stopping_time += 1
    if x <= 0:
        print('invalid input number must be greater than 1')
        return 0
    elif x == 1:
        print(1)
        return 1
    else:

        if x % 2 == 0:
            x /= 2
            print('| {:^70} | '.format(round(x)))
        else:
            x = 3 * x + 1
            print('| {:^70} | '.format(round(x)))

    return conjecture(x) if x != 1 else 1


def main():
    number = 26
    width = 70
    print(f'here are the collatz numbers for < {number} >'.center(width, '_'))
    print()
    conjecture(number)
    print('_'*width)
    print('stopping time: ', stopping_time)
    print('_'*width)


if __name__ == '__main__':
    main()
