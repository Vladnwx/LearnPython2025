# Названия файлов
INPUT_FILE = 'task2_input.txt'
OUTPUT_FILE = 'task2_output.txt'
print("На вход подается два числа через пробел: a, n. "
      "Напишите функцию для реализации алгоритма быстрого "
      "возведения в степень с помощью рекурсивной функции")
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

#Функция быстрого возведения в степень
def task2(a , n):
    if n ==0:
        return 1
    elif n%2 ==0:
        #print("n четное")
        temp = task2(a, n/2)
        return temp * temp
    else:
        #print("n НЕ четное")
        return a * task2(a, n-1)


print(f"{list_int[0]} в степени {list_int[1]} Результат: {task2(a = list_int[0], n =list_int[1])}")