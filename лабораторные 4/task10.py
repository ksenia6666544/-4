import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    # Читаем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Конвертируем список словарей в красивую JSON строку
    json_data = json.dumps(data, indent=4, ensure_ascii=False)

    # Записываем JSON строку в выходной файл
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as out_file:
        out_file.write(json_data)


if __name__ == '__main__':
    # Выполняем основную задачу
    task()

    # Проверяем полученный результат
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
