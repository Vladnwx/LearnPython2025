# Названия файлов
INPUT_FILE = 'task1_input.txt'
OUTPUT_FILE = 'task1_output.txt'
print("На вход подается список чисел через пробел. Напишите функцию выводящую сообщение для списка чисел")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read().strip()
# Закрытие файла
fi.close()
# Преобразование в список используя регулярное выражение
list_string = string.split(" ")

def task1(string_number):
    l = [int(i) for i in string_number]
    print(l)
    if number_equal(l):
        print("Все числа равны")
    elif number_not_equal(l):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

def number_equal(list_number):
    s = sum(list_number)/len(list_number)
    if s == list_number[0]:
        return True
    else:
        return False

def number_not_equal(list_number):
    s = set(list_number)
    if len(list_number)== len(s):
        return True
    else:
        return False

task1(list_string)