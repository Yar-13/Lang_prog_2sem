import csv
import argparse
import pygost

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args(
        description="Import csv database in csv database with hashed (striborg alrorithm) data")
    parser.add_argument('-f', '--file', help='source csv database')
    parser.add_argument('-c', "--columns", help='will be hashed columns.\nformat: column1,column2,...')
    