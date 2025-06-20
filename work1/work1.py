from pathlib import Path

path_to_file_salary = Path("salary_file.txt")

def total_salary(path):
    total_salarys = 0
    average_salarys = 0
    if path.exists():
        with open(path, encoding="utf-8") as file_salary:
            lines = [el.strip() for el in file_salary.readlines()]
        for line in lines:
            sum_salarys = line.split(',')[-1]
            if sum_salarys.isdigit():
                total_salarys += int(sum_salarys)
            else:
                total_salarys = 0
                average_salarys = 0
                print("Файл пошкоджений або некорректні данні!")
                return total_salarys, average_salarys
        average_salarys = total_salarys / len(lines)
    else:
        print(f'Файл {path} не існує!')

    return total_salarys, average_salarys

total, average = total_salary(path_to_file_salary)
if total and average:
    print(f" Загальна сума заробітної плати: {total:.2f}")
    print(f" Середня заробітна плата: {average:.2f}")