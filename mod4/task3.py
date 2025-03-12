# Названия файлов
INPUT_FILE = 'task3_input.txt'
OUTPUT_FILE = 'task3_output.txt'
print("На вход подается два числа через пробел: a, b. "
      "Напишите функцию для реализации рекурсивного алгоритма Евклида поиска наибольшего общего делителя. ")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read().strip()
# Закрытие файла
fi.close()
# Преобразование в список используя регулярное выражение
list_string = string.split(" ")
list_int = [int(i) for i in list_string]
print(f"Исходные данные: \na= {list_int[0]} \nn= {list_int[1]}")

#Функция
def euclid_algorithm(a , n):
    if n ==0:
        return a
    else:
        return euclid_algorithm(n, a%n)


print(f"{list_int[0]} НОД {list_int[1]} Результат: {euclid_algorithm(a = list_int[0], n =list_int[1])}")