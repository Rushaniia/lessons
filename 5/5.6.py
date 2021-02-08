dct1 = {}
with open('666.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        sub, lec, prac, lab = line.split()
        dct1[sub] = int(lec) + int(prac) + int(lab)

print(dct1)



