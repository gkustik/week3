with open('text.txt', 'w', encoding='utf-8') as myfile: # перезапись файла
    myfile.write("Первая строка через код!")

with open('text.txt', 'a', encoding='utf-8') as myfile: #a добавление записи в файл
    myfile.write("Вторая строка кода!\n")

with open('text.txt', 'a', encoding='utf-8') as myfile:
    myfile.write("Третья строка через код!\n")

with open('text.txt', 'a', encoding='utf-8') as myfile:
    myfile.write("\tЧетвертая строка через код!")


with open('text.txt', 'r', encoding='utf-8') as myfile: # чтение файла
    content = myfile.read()
    print(content)


# чтение файла постройчно
with open('text.txt', 'r', encoding='utf-8') as myfile:
    for line in myfile:
        line = line.upper()
        print(line)

# чтение файла постройчно без пробелом между строк
with open('text.txt', 'r', encoding='utf-8') as myfile:
    for ln in myfile:
        ln = ln.upper()
        ln = ln.replace('\n',"")
        print(ln)