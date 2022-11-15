

def txt_file_from_api(exchange_rate):
    try:
        with open("File_TXT.txt", mode="w") as file_txt:
            file_txt.write(exchange_rate.text)

    except Exception as e:
        print(e)
    else:
        if exchange_rate.text == '{"errorDescription":"Too many requests"}':
            print("🔴 Помилка запису .txt файлу, хай йому грець!")
        else:
            print(f"🟢 Дані збережено до файле File_TXT.txt")
