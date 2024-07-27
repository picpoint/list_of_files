import os

FOLDERNAME = "photo"
FILENAME = "list_photo.txt"
'''
Функция перебора всех файлов в папке и записи в текстовый файл
'''
def list_of_files(folder):
    try:
        files_list = os.listdir(folder)
        if len(files_list) != 0:
            with open(FILENAME, "w+") as file:
                for i in files_list:
                    file.write(i[:-4] + "\n")
            print("Список создан!")
        else:
            print("Нет файлов в папке ... :-(")
            return
    except:
        print("Произошла ошибка во время выполнения ... :-(")


list_of_files(FOLDERNAME)