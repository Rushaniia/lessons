try:
    with open('555.txt', 'w+') as fail_1:
        enter = input('Enter numbers: \n')
        fail_1.writelines(enter)
        a = [int(x) for x in enter.split()]
        print(sum(a))

except IOError:
    print('Error')