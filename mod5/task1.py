# Названия файлов
INPUT_FILE = 'task1_input.txt'
OUTPUT_FILE = 'task1_output.txt'
print("Найдите остаток при делении числа a на b.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
# Преобразование строки в список строк с регулярным выражением " "
c=0
for count in string:
    if count == ",":
        break
    c=c+1
print(f"c = {c}")
print(type(c))
# Присваивание переменным значений из списка
a = int(string[:c])
b = int(string[c+1:])
# Вывод значений полученных переменных в консоль
print(f"a = {a}")
print(type(a))
print(f"b = {b}")
print(type(b))
# Нахождение остатка
result = a % b
# Вывод остатка в консоль
print(f"Остаток: {result}")
# Запись результата в файл
fo = open(OUTPUT_FILE, 'w')
fo.write(str(result))
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Остаток записан в файл {OUTPUT_FILE}.")