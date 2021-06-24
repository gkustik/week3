# Дата и время
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')
dt_now = datetime.now()
print(dt_now)
delta = timedelta(days=1)
dt2 = dt_now - delta
print(dt2)
delta2 = timedelta(days=30)
dt3 = dt_now - delta2
print(dt3)

print("------")

time = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(time, '%d/%m/%y ' ' %H:%M:%S.%f')
print(date_dt)

# Работа с файлами
with open('referat.txt', 'r', encoding='utf-8') as mytext:
    content = mytext.read()
    print(content)
   
print (len(content))

a = content.split()
print (len(a))

with open('referat.txt', 'r', encoding='utf-8') as mytext:
    for ln in mytext:
        ln = ln.replace(',','!')
        ln = ln.replace('.','!')
        print(ln)

with open('referat2.txt', 'w', encoding='utf-8') as mynew:
    mynew.write(ln)

# Работа CSV
people_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
with open('tast.csv', 'w', encoding='utf-8', newline='') as c:
    field = ['name', 'age', 'job']
    write = csv.DictWriter(c, field, delimiter=',')
    write.writeheader()
    for people in people_list:
        write.writerow(people)