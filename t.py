import csv

user_list = [
   {'name': 'Ирина', 'last_name':'Величкина','email':'nlp808@yandex.ru','time':'2021-06-01','status':'approved'},
   {'name': 'Наталия', 'last_name':'Пак','email':'n11lp808@yandex.ru','time':'2021-06-01','status':'approved'},
   {'name': 'Сергей', 'last_name':'Ган','email':'8@yandex.ru','time':'2021-06-01','status':'approved'},
   {'name': 'Олег', 'last_name':'Личкина','email':'1208@yandex.ru','time':'2021-06-01','status':'approved'},
   ]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'last_name', 'email', 'time', 'status']
    writer = csv.DictWriter(f, fields, delimiter=',')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)



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