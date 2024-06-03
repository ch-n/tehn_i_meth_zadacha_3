import os

__root = ".\Проект 3"

__mark_flag = "_r"
# помечаем файлы, которые будем перемещать, чтобы не было конфликт имён
def __mark_files(root: str):
    for path, _, files in os.walk(root):
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            old_file_full_path = os.path.join(path, name)
            new_file_full_path = os.path.join(path, file_name + __mark_flag + file_extension)
            os.rename(old_file_full_path, new_file_full_path)


# сортируем файлы так, чтобы в папке А первые по номеру картинки из папок 1, 2, 3 оказались в новой папке 1 с новыми именами и так далее
def __sort_images(root: str):
    for path, _, files in os.walk(root):
        for file_idx, name in enumerate([file for file in files if __mark_flag in file]):
            _, file_extension = os.path.splitext(name)

            old_file_full_path = os.path.join(path, name)
            new_file_full_path = os.path.join(os.path.dirname(path), str(file_idx + 1), os.path.basename(path) + file_extension)
            
            print("Старое имя: " + old_file_full_path.replace(__mark_flag, ""))
            print("Новое имя: " + new_file_full_path)
            print("")

            os.rename(old_file_full_path, new_file_full_path)

def sort_images():
    __mark_files(__root)
    __sort_images(__root)
