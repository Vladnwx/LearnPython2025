INPUT_FILE = 'task5_input.txt'
OUTPUT_FILE = 'task5_output.txt'
print("Дан список слов. Составить из последних букв каждого слова новое")
fi = open(INPUT_FILE, 'r', encoding="utf-8")
string = fi.read().strip()
fi.close()
l = string.split()
fo = open(OUTPUT_FILE, 'w', encoding="utf-8")
for s in l:
      print(s[-1], end="")
      fo.write(s[-1])