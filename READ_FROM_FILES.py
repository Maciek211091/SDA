def read_from_files(file_paths: list) -> str:

    new_str = ''

    for i in file_paths:
        with open(i, 'r') as f:
            a = f.read()
            new_str += a

    return new_str


file_paths_to_read = ['/home/maciej/PycharmProjects/Wzroce-projektowe/text1.txt',
              '/home/maciej/PycharmProjects/Wzroce-projektowe/text2.txt']


#print(read_from_files(file_paths_to_read))


def read_from_files_decor(func, file_paths: list):
    def wrapper():
        print('---')
        print('Reading from files\n')
        print(func(file_paths))
        print('\nReading ended')
        print('---')
    return wrapper


wrapped_func = read_from_files_decor(read_from_files, file_paths_to_read)


if __name__ == '__main__':
    wrapped_func()