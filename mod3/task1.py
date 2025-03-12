INPUT_FILE = 'task1_input.txt'
OUTPUT_FILE = 'task1_output.txt'
print("Рассмотрим три числа a, b и c . Упорядочим их по возрастанию. Какое число будет стоять между двумя другими? ")
fi = open(INPUT_FILE, 'r')
string = fi.read().strip()
fi.close()
l = string.split()
l.sort(reverse=True)
print(l[1])
fo = open(OUTPUT_FILE, 'w')
fo.write(str(l[1]))
fo.close()