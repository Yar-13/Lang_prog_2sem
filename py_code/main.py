import csv
import argparse
from pygost import gost34112012512
from pygost import gost34112012256

def get_csv_header(file):
    header = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if reader.line_num == 1:
                header = list(i)
    return header

def get_csv_dict(file):
    # get_column_items(str, list)
    header = get_csv_header(file)
    csv_data = dict(list((i, []) for i in header))
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if reader.line_num != 1:
                for j in header:
                    csv_data[j].append(i[header.index(j)])
    return csv_data

def get_hash_dict(data, columns):
    hash_data = data.copy()
    for key in hash_data.keys():
        if key in columns:
            for i in range(len(data[key])):
                hash_data[key][i] = gost34112012256.new(bytes(data[key][i], 'utf8')).digest()[::-1].hex()
    
    return hash_data

def write_csv_hash(source, target, hash_data):
    header = get_csv_header(source)
    with open(target, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(len(hash_data[header[0]])):
            row = [hash_data[j][i] for j in hash_data.keys()]
            writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Import csv database in csv database with hashed (striborg alrorithm) data",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--source', help='source csv database')
    parser.add_argument('-t', '--target', help='empty target csv file')
    parser.add_argument('-c', "--columns", help='will be hashed columns.\nformat: column1,column2,...')
    args = parser.parse_args()
    #обработать события, когда на вход не поданы колонки, файл и др. 
    data = get_csv_dict(args.source)
    hash_data = get_hash_dict(data, args.columns.split(','))
    '''for x in hash_data.keys():
        print(x)
        print(*hash_data[x], sep='\n')
        print('\t')    
    for x in data.keys():
        print(x)
        print(*data[x], sep='\n')
        print('\t')'''

    write_csv_hash(args.source, args.target, hash_data)