def fizz_buzz(num):
    all_num = []
    for i in num:
        if ((i % 3) == 0) & ((i % 5) == 0):
            i = 'BuzzFizz'

        elif (i % 3) == 0:
            i = 'Fizz'

        elif (i % 5) == 0:
            i = 'Buzz'

        all_num.append(i)
    for i in all_num:
        print(i)


fizz_buzz(range(1, 51))
