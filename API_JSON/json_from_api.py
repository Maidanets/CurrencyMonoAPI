import json


def json_file_from_api(exchange_rate):
    try:
        with open("File_JSON.json", mode="w") as file_json:
            json_writer = json.loads(exchange_rate.text)
            json.dump(json_writer, file_json)

    except Exception as e:
        print(e)
    else:
        if exchange_rate.text == '{"errorDescription":"Too many requests"}':
            print("🔴 Помилка запису .json файлу, бодай його чорти вхопили!")
        else:
            print(f"🟢 Дані збережено до файле File_JSON.json")
