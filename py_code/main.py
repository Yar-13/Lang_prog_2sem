import csv
import argparse
import pygost

def get_csv_dict(file, columns):
    # get_column_items(str, list)
    csv_data = dict(list((i, []) for i in columns))
    header = {}
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if reader.line_num == 1:
                header = dict(list((x, i.index(x)) for x in i))
            else:
                for j in columns:
                    csv_data[j].append(i[header[j]])
    return csv_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Import csv database in csv database with hashed (striborg alrorithm) data",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--file', help='source csv database')
    parser.add_argument('-c', "--columns", help='will be hashed columns.\nformat: column1,column2,...')
    args = parser.parse_args()

    data = get_csv_dict(args.file, args.columns.split(','))