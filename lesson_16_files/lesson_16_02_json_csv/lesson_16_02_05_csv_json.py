import csv
import json


def get_data_from_csv_dict(file_path: str) -> list[dict[str, str]]:
    csv_data = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            csv_data.append(row)
    return csv_data


def write_data_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Данные записаны успешно!')
    return True


if __name__ == '__main__':
    sales_data = get_data_from_csv_dict('data_files/sales_data.csv')
    write_data_to_json(r'data_files/output_data.json', sales_data)
