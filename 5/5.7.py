import json

profit = {}
y = {}
x = 0
middle = 0
i = 0
with open("777.txt", "r") as file:
    for line in file:
        name, form, income, loss = line.split()
        profit[name] = int(income) - int(loss)
        if profit.setdefault(name) >= 0:
            x += profit.setdefault(name)
            i += 1
        else:
            print(f'Company incurs losses: {name}')
    if i != 0:
        middle = x / i
        print(f'Middle income: {round(middle)}')

    y = {'Middle income': round(middle)}
    profit.update(y)
    print(f'Income company: {profit}')

with open('777.json', 'w') as my_file:
    json.dump(profit, my_file)

    file1 = json.dumps(profit)
    print(file1)