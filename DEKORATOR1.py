"""
Dekorator - wzorzec strukturalny

wrapper - koncepcja polegająca na rozszerzeniu, opakowaniu logiki pewnej klasy o dodatkowe elementy

Celem dekoratora jest rozszerzenie pewnej logiki (klasy, funkcji) o dodatkowe elementy
"""

from datetime import datetime


def simple_logger_error(message: str):
    print(f'ERROR {message}')


def log_decoraator(func, message:str):
    def wrapper():
        print("-"*10)
        print("----", datetime.now(), '----')
        func(message)
        print('-'*10)
    return wrapper


def main():
    simple_logger_error("file doesn't exist")
    simple_logger_error("connection to DB failed")

# chcemy wzbogacić zachowanie istniejącego loggera bez zmiany jego logiki
    decorated_func = log_decoraator(simple_logger_error, "connection to DB failed")
    decorated_func()



if __name__ == '__main__':
    main()
