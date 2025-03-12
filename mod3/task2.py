INPUT_FILE = 'task2_input.txt'
OUTPUT_FILE = 'task2_output.txt'
print("Для введенного в десятичном коде натурального числа найти представление "
      "в двоичном, восьмеричном и шестнадцатеричном кодах. "
      "Если введено не натуральное число, вывести диагностику: «Неверный ввод»")
fi = open(INPUT_FILE, 'r')
string = fi.read().strip()
fi.close()
try:
    number = int(string)
    b = bin(number)[2:]
    o = oct(number)[2:]
    h = hex(number)[2:].upper()
    fo = open(OUTPUT_FILE, 'w')
    print(f"{b}, {o}, {h}")
    fo.write(f"{b}, {o}, {h}")
    fo.close()
except ValueError:
    print("Неверный ввод")