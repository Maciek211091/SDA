from datetime import datetime


class Logger:

    def __current_date_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def log_error(self, message):
        date_and_time = self.__current_date_time()
        print(f'ERROR {date_and_time}, {message}')

    def log_debug(self, message):
        date_and_time = self.__current_date_time()
        print(f'DEBUG {date_and_time} {message}')

    def log_info(self, message):
        date_and_time = self.__current_date_time()
        print(f'INFO {date_and_time} {message}')


# l1 = Logger()
# l1.log_info('Data migration has been completed')

# wada tego rozwiązania jest taka, że można zrobić kolejną (niepotrzebną) instancję tej klasy


class No_Single_Instance_Exception(Exception):
    pass


class Simple_Logger:
    '''informacja, czy został już zrobiony obiekt tej klasy'''
    __instance = None

    def __init__(self):
        'jeśli została stworzona instancja tej klasy to rzucamy wyjątek'
        if Simple_Logger.__instance is not None:
            raise No_Single_Instance_Exception
        else:
            Simple_Logger.__instance = self

    @staticmethod
    def get_instance():
        if Simple_Logger.__instance is None:
            Simple_Logger()

        return Simple_Logger.__instance

    def __current_date_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def log_error(self, message):
        date_and_time = self.__current_date_time()
        print(f'ERROR {date_and_time}, {message}')

    def log_debug(self, message):
        date_and_time = self.__current_date_time()
        print(f'DEBUG {date_and_time} {message}')

    def log_info(self, message):
        date_and_time = self.__current_date_time()
        print(f'INFO {date_and_time} {message}')


# poniższe metody uzyskują referencje na obiekt i nawet tworzenie logger2 nie daje błędu - referencja na ten sam obiekt
logger1 = Simple_Logger.get_instance()
logger2 = Simple_Logger.get_instance()

print(logger1)
# print(logger2)

try:
    logger3 = Simple_Logger()
except No_Single_Instance_Exception:
    print('You can create only one instance')