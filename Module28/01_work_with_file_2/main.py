# TODO здесь писать код
class File:
    """
    Класс файл открывает, создает файлы
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """ Функция входа
        если файла не существует,
        то создается файл.
        """
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.filename, 'x', encoding='utf-8')
        finally:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('test.txt', 'r') as file:
    print(file.read())
