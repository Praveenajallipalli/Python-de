import csv

with open('data/orders.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)