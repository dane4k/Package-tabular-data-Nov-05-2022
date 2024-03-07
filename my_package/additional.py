import datetime
from prettytable import PrettyTable



def abolishing_date(data, dates_lst):
    header = data[0]
    header.append('Дата упразднения отдела')
    dates = []
    mytable = PrettyTable()

    for els in dates_lst:
        current_date = datetime.date(*els)
        dates.append(str(current_date))

    for rows_iteration in range(len(data) - 1):
        data[rows_iteration + 1].append(dates[rows_iteration])

    mytable.field_names = header
    for row in data[1:]:
        mytable.add_row(row)
    print(mytable)





def add(data, column_number, add_all=[]):
    els = []
    for row in data[1:]:
        if type(row[column_number - 1]) == bool or type(row[column_number - 1]) == int or type(
                row[column_number - 1]) == float:
            els.append(row[column_number - 1])
    if len(add_all) == 0:
        print(sum(els))
    elif type(add_all) == list:
        counter = 0
        try:
            for iteration in add_all:
                counter += els[iteration + 1]
        except IndexError:
            print('В таблице не хватает элементов, выберите номер элемента ниже предыдущего')
        print(counter)





def sub(data, column_number, add_all):
    els = []
    for row in data[1:]:
        if type(row[column_number - 1]) == bool or type(row[column_number - 1]) == int or type(
                row[column_number - 1]) == float:
            els.append(row[column_number - 1])
    try:
        for iteration in add_all:
            counter = els[add_all[0] + 1] - els[add_all[1] + 1]
    except IndexError:
        print('В таблице не хватает элементов, выберите номер элемента ниже предыдущего')
    print(counter)







def mul(data, column_number, add_all):
    els = []
    for row in data[1:]:
        if type(row[column_number - 1]) == bool or type(row[column_number - 1]) == int or type(
                row[column_number - 1]) == float:
            els.append(row[column_number - 1])
    try:
        for iteration in add_all:
            counter = els[add_all[0] + 1] * els[add_all[1] + 1]
    except IndexError:
        print('В таблице не хватает элементов, выберите номер элемента ниже предыдущего')
    print(counter)





def div(data, column_number, add_all, rounding=True):
    els = []
    for row in data[1:]:
        if type(row[column_number - 1]) == bool or type(row[column_number - 1]) == int or type(
                row[column_number - 1]) == float:
            els.append(row[column_number - 1])
    try:
        for iteration in add_all:
            counter = els[add_all[0] + 1] / els[add_all[1] + 1]
    except IndexError:
        print('В таблице не хватает элементов, выберите номер элемента ниже предыдущего')
    if rounding:
        print(round(counter))
    else:
        print(counter)


