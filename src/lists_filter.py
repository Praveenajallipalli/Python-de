orders = [
    {'orer_id':1, 'country': 'US'},
    {'orer_id':2, 'country': 'IN'},
    {'orer_id':3, 'country': 'IN'}
]

in_order = []

for x in orders:
    if x['country']=='IN':
        in_order.append(x)

print(in_order)