with open('333.txt', 'r', encoding='utf-8') as fail_1:
    salary = []
    low_sal = []
    a = fail_1.read().split('\n')
    for i in a:
        i = i.split()
        if int(i[1]) < 20000:
            low_sal.append(i[0])
        salary.append(i[1])
    middle = sum(map(int,salary)) / len(salary)
    s = ', '.join(low_sal)
print(f'Salary is less 20000 from: {s}; middle salary {round(middle)}')