import sys
from colorama import Fore
from pathlib import Path

if len(sys.argv) > 1:
    original_path = Path(sys.argv[1])

    def print_dir (dir, n):
        n += 1
        for path in dir.iterdir():
            if path.is_dir():     
                print(f'{"    " * n}{Fore.BLUE}{path.name}/{Fore.RESET}')
                print_dir(path, n)
            else:
                print(f'{"    " * n}{Fore.YELLOW}{path.name}{Fore.RESET}')

    if original_path.is_dir():
        print(f'{Fore.BLUE}{original_path.name}/{Fore.RESET}')
        print_dir(original_path, 0)
    else:
        print("Вказаний шлях не існує або він не веде до директорії")
else:
    print("Введіть повний шлях до папки(без пробілів), як аргумент до викликаємого файлу(через пробіл)")