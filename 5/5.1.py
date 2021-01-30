my_file = open("111.txt", "w")
a = input('Enter a string \n')
while True:
    my_file.writelines(a)
    a = input('Enter a string \n')
    if a =='':
        break

my_file.close()