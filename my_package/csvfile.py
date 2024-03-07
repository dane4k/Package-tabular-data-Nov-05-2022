import csv


def load_table(filename):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            global table
            table = [row for row in reader]
            print('Таблица успешно загружена!')

    except FileNotFoundError:
        print('File is not found. Use the existing .csv file')


def save_table(file, data):
    if file[-4:] == '.csv':
        with open(file, 'w+', newline='') as file_to_write:
            write = csv.writer(file_to_write, delimiter=';')
            write.writerows(data)
        print('\n''Таблица сохранена!')
    else:
        print('Unsupported file type. Use .csv extension')

