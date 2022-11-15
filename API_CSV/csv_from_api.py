import csv


def csv_file_from_api(exchange_rate):
    try:
        with open('File_CSV.csv', mode='w') as file_csv:
            exchange_rate_keys = {}
            for i in exchange_rate.json():
                exchange_rate_keys.update(i)
            csv_writer = csv.DictWriter(file_csv, fieldnames=list(exchange_rate_keys.keys()))
            csv_writer.writeheader()
            for i in exchange_rate.json():
                csv_writer.writerow(i)

    # якщо робити запити до API дуже швидко - спрацює помилка
    # помилка створення ключів словника
    except ValueError:
        print("🔴 Помилка запису .csv файлу, а щоб його підняло та гепнуло!")

    else:
        print(f"🟢 Дані збережено до файле File_CSV.csv")
