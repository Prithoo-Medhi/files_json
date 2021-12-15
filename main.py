from os import listdir
from os.path import isfile, join
import json

BASE_PATH = 'allureReport/'


def find_list_of_files(directory='allureReport'):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    # print(files)
    return files


def fields_in_json(file: str):
    with open(file) as file:
        json_data = json.load(file)
        return list(json_data.keys())

def text_lines(file: str):
    with open(file) as file:
        lines = file.readlines()
    return lines




def main():
    list_of_fields = []
    text_lines = []

    files = find_list_of_files(directory='allureReport')
    # print(files)
    for file in files:
        if file.endswith('.json'):
            fields_in_file = fields_in_json(f'{BASE_PATH}{file}')
            list_of_fields.extend(fields_in_file)
        elif file.endswith('.txt'):
            lines = text_lines(f'{BASE_PATH}{file}')
            text_lines.extend(lines)

    set_of_fields = set(list_of_fields)
    set_of_fields = sorted(set_of_fields)

    save_fields_to_file(set_of_fields)
    save_lines_to_file(text_lines)


def save_fields_to_file(fields: set):
    with open('output/json_fields.txt', 'wt') as file:
        file.write(str(fields))
        file.write('\n')

def save_lines_to_file(lines: list):
    with open('output/text_lines.txt', 'wt') as file:
        for line in lines:
            file.write(line)
            file.write('\n')


if __name__ == "__main__":
    main()
