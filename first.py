def create_salary_file(path):
    data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        total_salary = 0
        count = 0
        
        for line in lines:
            try:
                name, salary = line.strip().split(',')
                total_salary += float(salary)
                count += 1
            except ValueError:
                print(f"Invalid line format: {line}")
                continue
        
        if count == 0:
            raise ValueError("No valid salary data found")
        
        average_salary = total_salary / count
        return total_salary, average_salary
    
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Створення файлу з даними про заробітні плати
file_path = "salary_file.txt"
create_salary_file(file_path)

# Використання функції для обчислення заробітних плат
total, average = total_salary(file_path)
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print("Не вдалося обробити файл.")
