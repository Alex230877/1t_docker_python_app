import os
import sys
from datetime import datetime

# Укажите свой путь или оставьте закомментированным для корневого каталога
# path = "/home/path"  
# Путь к директории (по умолчанию — корень файловой системы)
path = "/"

def count_files(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

def top_10_files(directory):
    files_sizes = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                size_kb = os.path.getsize(filepath) / 1024
                files_sizes.append((name, size_kb))
            except OSError:
                pass
    return sorted(files_sizes, key=lambda x: x[1], reverse=True)[:10]

if __name__ == "__main__":
    # Приветственное сообщение с именем пользователя
    name = sys.argv[1] if len(sys.argv) > 1 else "User"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}!\nCurrent date and time: {current_time}")

    # Подсчет файлов
    total_files = count_files(path)
    print(f"Total files in '{path}': {total_files}")

    # Топ-10 файлов по размеру
    largest_files = top_10_files(path)
    print("Top 10 largest files (in KB):")
    for i, (file, size) in enumerate(largest_files, start=1):
        print(f"{i}. {file}: {size:.2f} KB")
