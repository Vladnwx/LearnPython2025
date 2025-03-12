# Названия файлов
INPUT_FILE = 'task5_input.txt'
OUTPUT_FILE = 'task5_output.txt'
print("На вход подается доменное имя сайта. Необходимо вывести все домены по порядку начиная с домена первого уровня.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))

start = finish = count =0

count_dot =0
for c in string:
    if c == '.':
        count_dot = count_dot+1

fo = open(OUTPUT_FILE, 'w')
for c in string[::-1]:
    if start<0:
        if c == '.':
            if finish ==0:
                print(string[start:])
                # Запись результата в файл
                fo.write(string[start:])
                fo.write(str("\n"))
                fo.close()
                finish = start-1
                count_dot = count_dot - 1
            elif count_dot>0:
                print(string[start:finish])
                fo = open(OUTPUT_FILE, 'a')
                fo.write(string[start:finish])
                fo.write(str("\n"))
                finish = start - 1
                count_dot = count_dot - 1
        elif count_dot == 0 :
                print(string[:finish])
                fo.write(string[:finish])
                break
    start=start-1
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Остаток записан в файл {OUTPUT_FILE}.")