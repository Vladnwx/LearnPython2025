# Названия файлов
import copy

INPUT_FILE = 'task4_input.txt'
OUTPUT_FILE = 'task4_output.txt'
print("На вход подается строка. Напишите функцию для реализации: "
      "если из слова можно составить палиндром, то составить его и вывести на экран")

# Открытие файла на чтение
fi = open(INPUT_FILE, 'r', encoding="utf-8")
# Чтение данных из файла
string = fi.read().strip()
# Закрытие файла
fi.close()
# Преобразование в список используя регулярное выражение
list_string = string.split(" ")
print(f"Исходные данные:  {list_string}")

#Функция является ли полученное значение палиндромом
def is_palindrome(s):
      if s == s[::-1] :
            print(f"{string} - это палиндром")
      else:
            print(f"{string} - это НЕ палиндром")

#Функция выполняет быструю проверку на возможный палиндром
def fast_check_palindrome (palindrome):
      # Пробуем сделать SET и проверить длины, чтобы сразу отсечь невозможные
      # SET позволяет проверить только уникальные символы
      set_palindrome = set(palindrome)
      if len(set_palindrome) == len(palindrome):
            print(f"{string} - нельзя составить палиндром")
            return False
      else:
            return True

#Функция проверяет, может быть палиндром или нет в случае четного числа
def palindrome_odd(list_characters):
#При четном количестве каждый символ должен встречаться четное количество раз
#Предполагаем, что нам не подсунут слишком большую строку, иначе надо искать другое решение
#В лоб напрашивается решение с двумя циклами for, что даст О(n**2)
#Чтобы уменьшить количество итераций, будем удалять проверенные символы
      temp_list = copy.copy(list_characters)
      print(type(temp_list))
      count = 0
      while temp_list.__sizeof__()>0:
            current_index = 0
            list_index =[]
            find_index =0
            for value in temp_list:
                  if value == temp_list[find_index]:
                        list_index.__add__(current_index)
                        current_index +=1
            if len(list_index)%2 !=0:
                  return "Это не палиндром"
            for value in list_index:
                  temp_list.remove(value)




 #Наверное тут можно подключить библиотеку на поиск существования данного слова, но мы не будем этого делать
#Просто выведем данный вариант как возможный

palindrome_odd(list_string)