INPUT_FILE = 'task3_input.txt'
OUTPUT_FILE = 'task3_output.txt'
print("На вход подается доменное имя сайта. Необходимо вывести все домены по порядку начиная с домена первого уровня")
fi = open(INPUT_FILE, 'r')
string = fi.read().strip()
fi.close()
l = string.split(sep=".")
print(l)
fo = open(OUTPUT_FILE, 'w')
for s in l:
      fo.write(s)
      fo.write("\n")
fo.close()