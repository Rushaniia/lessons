# задание 1:
from sys import argv


def salary(pay_rate, time_worked, bonus):
    wage = (pay_rate * time_worked) + bonus
    print(wage)


tasks, a, b, c = argv

salary(float(a), float(b), float(c))


# задание 2:
a = list(map(int, input('Enter numbers: ').split()))
result = [numbers for i, numbers in enumerate(a) if i > 0 and a[i] > a[i - 1]]
print(result)



# задание 3:
result = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(result)


# задание 4
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)


# задание 5
from functools import reduce

def my_func(pr_el, el):
    return pr_el * el


my_list = [el for el in range(99, 1001) if el % 2 ==0]
print(reduce(my_func, my_list)


задание 6
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

list1 = ['a', 'b', 'c', 'd']
c = 0
for el in cycle(list1):
    c += 1
    if c > 10:
        break
    else:
        print(el)



# задание 7
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr = pr*i
        yield pr

n = int(input('Enter number '))
for i in fact(n):
    print(i)