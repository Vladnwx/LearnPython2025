INPUT_FILE = 'task6_input.txt'
OUTPUT_FILE = 'task6_output.txt'
print("На вход подается последовательность целых чисел. "
      "Требуется определить, присутствуют ли в этой последовательности одинаковые числа. "
      "Результат вернуть в формате Boolean")
fi = open(INPUT_FILE, 'r', encoding="utf-8")
string = fi.read().strip()
fi.close()
l = string.split()
s  = set(string.split())
fo = open(OUTPUT_FILE, 'w', encoding="utf-8")
if len(l) == len(s):
      print(True)
      fo.write("True")
else:
      print(False)
      fo.write("False")
fo.close()