# Названия файлов
INPUT_FILE = 'task3_input.txt'
OUTPUT_FILE = 'task3_output.txt'
print("Выведите число, которое будет стоять между двумя другими после упорядочивания.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
a = b = c = start = finish = count = 0
for s in string:
    if finish>0 :
        if count ==0 and s == " ":
            a =  int(string[:finish])
            count = count+1
            start = finish
        elif count == 1 and s == " ":
            b =  int(string[start:finish])
            count = count+1
            start = finish
            if b>a:
                temp =a
                a=b
                b=temp
        elif count == 2:
            c = int(string[start:])
            if c > b:
                temp = b
                b = c
                c = temp
            if b > a:
                temp = a
                a = b
                b = temp
    finish=finish+1
print(b)
# Запись результата в файл
fo = open(OUTPUT_FILE, 'w')
fo.write(str(b))
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Остаток записан в файл {OUTPUT_FILE}.")