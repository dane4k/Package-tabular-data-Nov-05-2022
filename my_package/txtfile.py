def save_table(data, txt):
    for rows in data:
        for iteration in range(len(rows)):
            rows[iteration] = str(rows[iteration])
    with open(txt, 'w+') as txtfile:
        for el in data:
            txtfile.write(' '.join(el) + '\n')
    print('Таблица сохранена')

