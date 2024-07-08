def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Удаляем пробелы и переводы строк
                if line:  # Пропускаем пустые строки
                    cat_id, name, age = line.split(',')
                    cats_list.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_list

# Пример использования функции:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)