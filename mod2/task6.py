# Названия файлов
INPUT_FILE = 'task6_input.txt'
OUTPUT_FILE = 'task6_output.txt'
print("Строка состоит из 0 и 1. Выведите ‘yes’, если количество единиц совпадает с количеством нулей. И ‘no’ в противном случае.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))

count_one = count_zero = 0

for s in string:
    if s =="1":
        count_one =count_one+1
    else:
        count_zero = count_zero+1
print(f"count_zero = {count_zero}")
print(f"count_one = {count_one}")

fo = open(OUTPUT_FILE, 'w')
if count_zero == count_one:
    print("yes")
    fo.write(str("yes"))
else:
    print("no")
    fo.write(str("no"))

fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Остаток записан в файл {OUTPUT_FILE}.")