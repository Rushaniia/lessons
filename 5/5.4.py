d = (('One', 'Один'), ('Two', 'Два'), ('Three', 'Три'), ('Four', 'Четыре'))
# list_2 = []
with open('444.txt', 'r') as file_1:
    with open('new_333.txt', 'w') as fail_2:
        for line in file_1:
            for k, v in d:
                line = line.replace(k, v)
            fail_2.write(line)
