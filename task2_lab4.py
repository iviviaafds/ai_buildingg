# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    data = []
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [OrderedDict(row) for row in reader]
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")