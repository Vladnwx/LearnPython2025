INPUT_FILE = 'task7_input.txt'
OUTPUT_FILE = 'task7_output.txt'
print("Человек вводит на сайте номер телефона, "
      "ему позволено для удобства использовать кроме плюса и цифр знаки "
      "‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.")
fi = open(INPUT_FILE, 'r', encoding="utf-8")
string = fi.read().strip()
fi.close()
s = (string.strip()
     .replace("-", "")
     .replace("(", "")
     .replace(")", "")
     .replace(" ", ""))
print(s)
fo = open(OUTPUT_FILE, 'w')
fo.write(s)
fo.close()