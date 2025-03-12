# Названия файлов
INPUT_FILE = 'task9_input.txt'
OUTPUT_FILE = 'task9_output.txt'
print("Человек вводит на сайте номер телефона, "
      "ему позволено для удобства использовать кроме плюса и "
      "цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r', encoding='utf-8')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
fo = open(OUTPUT_FILE, 'w')
fo.close()
fo = open(OUTPUT_FILE, 'a')
for c in string:
    temp = ord(c)
    if 58 > temp > 47 or temp==43:
        print(c, end="")
        fo.write(c)
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"\nРезультат записан в файл {OUTPUT_FILE}.")