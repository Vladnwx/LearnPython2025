# Названия файлов
INPUT_FILE = 'task8_input.txt'
OUTPUT_FILE = 'task8_output.txt'
print("Дан список слов. Составить из последних букв каждого слова новое.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r', encoding='utf-8')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
count = 0
char =" "
index = 0
for s in string:
    if s == char:
        count+=1
fo = open(OUTPUT_FILE, 'w', encoding='utf-8')
fo.close()
fo = open(OUTPUT_FILE, 'a', encoding='utf-8')
for s in string:
    if count>0:
        if s == char:
            print(string[index-1], end="")
            #Очень интересная механика)) он добавляет перенос строки при выводе в консоль, но не делает этого при записи в файл
            fo.write(string[index-1])
            count-=1
    elif count==0:
        index += 1
        continue
    index += 1
print(string[index-1])
fo.write(string[index-1])
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Результат записан в файл {OUTPUT_FILE}.")