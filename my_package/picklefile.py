import pickle

def save_table(data, file):
    with open(file, 'wb+') as pickle_file:
        pickle.dump(data, pickle_file)


def load_table(filename):
    with open(filename, 'rb') as file_to_read:
        result_data = pickle.load(file_to_read)
    for i in result_data:
        print(*i, sep='\t')

