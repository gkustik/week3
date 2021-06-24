import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'time', 'status', 'cash']
    reader = csv.DictReader(f, fields, delimiter=',')
    cash_total = 0
    for row in reader:
        cash_total += float(row['cash'])
        print(row)
    print(cash_total)
    