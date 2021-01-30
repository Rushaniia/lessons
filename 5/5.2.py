my_file = open("222.txt", "r", encoding='utf-8')
text1 = my_file.read()
print(f'Введенный текст: \n{text1}')

lines = 0
words = 0
symbols = 0

for line in open("222.txt", "r", encoding='utf-8'):
    lines += 1
    words += len(line.split())
    symbols += len(line)
print(f'Количество строк в тексте: {lines}')
print(f'Количество слов в тексте: {words}')
print(f'Количество букв в тексте: {symbols}')
my_file.close()