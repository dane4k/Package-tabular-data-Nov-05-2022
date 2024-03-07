import csv
from prettytable import from_csv


def get_rows_by_number(data, start, stop, copy_table=False):
    print(*data[0], sep='\t')
    if not copy_table:
        if start == stop:
            print(*data[start])
        else:
            result = data[start:stop + 1]
            for row in result:
                print(*row, sep='\t')
    else:
        copiedtable = []
        for rows in data:
            copiedtable.append(rows)
        if start == stop:
            print(*copiedtable[start])
        else:
            result = copiedtable[start:stop + 1]
            for row in result:
                print(*row, sep='\t')





def get_rows_by_index(data, val1, val2='', val3='', val4='', val5='', val6='', copy_table=False):
    values = []
    values += val1, val2, val3, val4, val5, val6
    for row in data[1:]:
        for value in values:
            if value == row[0]:
                print(*row)




def get_column_types(data, by_number=True):
    header = data[0]
    if not by_number:
        dictionary = {header[i]: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
    else:
        dictionary = {i: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
    for el in dictionary:
        if str(dictionary[el])[8:11] == 'str':
            dictionary[el] = 'str'
        if str(dictionary[el])[8:11] == 'int':
            dictionary[el] = 'int'
        if str(dictionary[el])[8:11] == 'float':
            dictionary[el] = 'float'
        if str(dictionary[el])[8:11] == 'bool':
            dictionary[el] = 'bool'
    print(dictionary)




def set_column_types(data, types_dict, by_number=True):
    header = data[0]
    try:
        if types_dict == 'int':
            for cols in data:
                for i in range(len(cols)):
                    for s in data:
                        s[i] = int(s[i])
        if types_dict == 'float':
            for cols in data:
                for i in range(len(cols)):
                    for s in data:
                        s[i] = float(s[i])
        if types_dict == 'bool':
            for cols in data:
                for i in range(len(cols)):
                    for s in data:
                        s[i] = bool(s[i])
        if types_dict == 'str':
            for cols in data:
                for i in range(len(cols)):
                    for s in data:
                        s[i] = str(s[i])
        if not by_number:
            dictionary = {header[i]: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
        else:
            dictionary = {i: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
        for el in dictionary:
            if str(dictionary[el])[8:11] == 'str':
                dictionary[el] = 'str'
            if str(dictionary[el])[8:11] == 'int':
                dictionary[el] = 'int'
            if str(dictionary[el])[8:11] == 'float':
                dictionary[el] = 'float'
            if str(dictionary[el])[8:11] == 'bool':
                dictionary[el] = 'bool'
        print(dictionary)


    except ValueError:
        print('Невозможно конвертировать изначальный тип данных в требуемый Вами')




def get_values(data, column=0):
    header = data[0]
    if column > 0:
        lst = [[i, type(row[i])] for row in data[1:] for i in range(len(header))][:len(header)]
    else:
        lst = [[header[i], type(row[i])] for row in data[1:] for i in range(len(header))][:len(header)]
    for el in lst:
        if str(el[1])[8:11] == 'str':
            el[1] = 'str'
        if str(el[1])[8:11] == 'int':
            el[1] = 'int'
        if str(el[1])[8:11] == 'bool':
            el[1] = 'bool'
        if str(el[1])[8:11] == 'float':
            el[1] = 'float'
    print(lst)




def get_value(data, column=0):
    header = data[0]
    if column > 0:
        lst = [[i, type(row[i])] for row in data[1:] for i in range(len(header))][:len(header)]
        for el in lst:
            if str(el[1])[8:11] == 'str':
                el[1] = 'str'
            if str(el[1])[8:11] == 'int':
                el[1] = 'int'
            if str(el[1])[8:11] == 'bool':
                el[1] = 'bool'
            if str(el[1])[8:11] == 'float':
                el[1] = 'float'
        for length in range(len(lst)):
            if length + 1 == column:
                print(lst[length][1])

    else:
        lst = [[header[i], type(row[i])] for row in data[1:] for i in range(len(header))][:len(header)]
        for el in lst:
            if str(el[1])[8:11] == 'str':
                el[1] = 'str'
            if str(el[1])[8:11] == 'int':
                el[1] = 'int'
            if str(el[1])[8:11] == 'bool':
                el[1] = 'bool'
            if str(el[1])[8:11] == 'float':
                el[1] = 'float'




def set_values(data, values, column=0):
    header = data[0]
    try:
        for iterator in range(len(data[0])):
            if values[iterator] == 'int':
                for cols in data[1:]:
                    for i in range(len(cols)):
                        cols[iterator] = int(cols[iterator])
            if values[iterator] == 'float':
                for cols in data[1:]:
                    for i in range(len(cols)):
                        cols[iterator] = float(cols[iterator])
            if values[iterator] == 'bool':
                for cols in data[1:]:
                    for i in range(len(cols)):
                        cols[iterator] = bool(cols[iterator])
            if values[iterator] == 'str':
                for cols in data[1:]:
                    for i in range(len(cols)):
                        cols[iterator] = str(cols[iterator])

        if column == 0:
            dictionary = {header[i]: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
        else:
            dictionary = {i: type(rows[i]) for rows in data[1:] for i in range(len(rows))}
        for el in dictionary:
            if str(dictionary[el])[8:11] == 'str':
                dictionary[el] = 'str'
            if str(dictionary[el])[8:11] == 'int':
                dictionary[el] = 'int'
            if str(dictionary[el])[8:13] == 'float':
                dictionary[el] = 'float'
            if str(dictionary[el])[8:12] == 'bool':
                dictionary[el] = 'bool'
        print(*header, sep='\t')
        for els in data[1:]:
            print(*els, sep='\t')


    except ValueError:
        print('Невозможно конвертировать изначальный тип данных в требуемый Вами')




def set_value(data, value, column=1):
    header = data[0]
    if type(header[column - 1]) == type(value):
        header[column - 1] = value
    else:
        print('Введите значение в виде другого типа данных')
    print(*header, sep='\t\t')
    for rows in data[1:]:
        print(*rows, sep='\t')




def print_table(file):
    with open(file, 'r') as f:
        table_result = from_csv(f)
        print(table_result)

