# Названия файлов
INPUT_FILE = 'task2_input.txt'
OUTPUT_FILE = 'task2_output.txt'
print("На вход подается длина стороны квадрата, рассчитать периметр, площадь и диагональ с округлением до 2 знака.")
# Открытие файла на чтение
fi = open(INPUT_FILE, 'r')
# Чтение данных из файла
string = fi.read()
# Закрытие файла
fi.close()
# Вывод считанных данных в консоль
print(f"Исходные данные: {string} ")
print(type(string))
# Приведение типа стороны квадрата к типу int
a = int(string)
# Вывод значений полученных переменных в консоль
print(f"a = {a}")
print(type(a))
# Нахождение периметра, площади и диагонали
perimetr = float(a*4)
square = float(a**2)
diagonal = float(a*1.414) #Так как запретили пользоваться какими либо функциями возьмем число с достаточной точностью
# Вывод в консоль
print(f"Периметр: {perimetr:.2f}")
print(f"Площадь: {square:.2f}")
print(f"Диагональ: {diagonal:.2f}")
# Запись результата в файл
fo = open(OUTPUT_FILE, 'w')
fo.write(f"{perimetr:.2f}, {square:.2f}, {diagonal:.2f}")
fo.close()
# Вывод в консоль в какой файл осуществлена запись
print(f"Результаты записаны в файл {OUTPUT_FILE}.")