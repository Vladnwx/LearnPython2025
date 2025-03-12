# Названия файлов
INPUT_FILE = 'task7_input.txt'
OUTPUT_FILE = 'task7_output.txt'
print("На вход подается строка s и символ i. Необходимо найти количество символов i, расположенных в начале строки.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
count = 0
char =""
comma = False
for s in string:
    if s ==",":
        comma =True
        continue
    if comma:
        char =s
index = 0
for s in string:
    if index ==0 and s == char:
        count += 1
    elif index>0 and s == char:
        break
    index += 1
print(count)
# Запись результата в файл
fo = open(OUTPUT_FILE, 'w')
fo.write(str(count))
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Результат записан в файл {OUTPUT_FILE}.")