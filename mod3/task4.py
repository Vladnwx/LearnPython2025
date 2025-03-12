INPUT_FILE = 'task4_input.txt'
OUTPUT_FILE = 'task4_output.txt'
print("Строка состоит из 0 и 1. Выведите ‘yes’, если количество единиц совпадает с количеством нулей. И ‘no’ в противном случае.")
fi = open(INPUT_FILE, 'r')
string = fi.read().strip()
fi.close()
a =string.count("1")
b =string.count("0")
fo = open(OUTPUT_FILE, 'w')
if a==b:
      print("yes")
      fo.write("yes")
else:
      print("no")
      fo.write("no")
fo.close()