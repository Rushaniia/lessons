
#задание 1
def my_func(*args):
    try:
        arg1 = int(input("Enter first number: "))
        arg2 = int(input("Enter second number: "))
        result = arg1 / arg2

    except ZeroDivisionError:
        return 'Error. Division by zero'
    except ValueError:
        return 'Value error'

    return result


print(my_func())



#задание 2
def my_func(**kwargs):
    print(kwargs)


my_func(name='Ru', surname='Sak', b_day='01/01/2001', city='Perm', email='aaa@gmail.com',
        telephone='+7111111111')



#задание 3
def my_func(arg1, arg2, arg3):
    list1 = [arg1, arg2, arg3]
    list1.remove(min(arg1, arg2, arg3))
    return sum(list1)


print(my_func(1, 2, 3))


#задание 4
def my_func(x,y):
    z = x ** abs(y)
    return z
print(my_func(2,-3))

def my_func1(a,b):
    num = 1
    for i in range(abs(b)):
        num = num*a
    return num
print(my_func1(5,-4))



#задание 5
def my_func ():
    result = 0
    while True:
        num = input('Enter list of number or Q to exit: ').split()
        for i in num:
            try:
                if i == 'Q' or i == 'q':
                    print(f'Sum is {result}. Exit')
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Enter number or Q')
        print(f'Sum is {result}')

my_func ()



#задание 6
string = input().split()
list1 = []
for i in string:
    list1.append(i.capitalize())
print(' '.join(list1))