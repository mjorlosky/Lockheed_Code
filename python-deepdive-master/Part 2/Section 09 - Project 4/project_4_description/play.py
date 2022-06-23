import file_constants
import parser

for files in file_constants.files:
    print(files)
    with open(files) as f:
        print(next(f), end='')
        print(next(f), end='')
        print(next(f), end='')
    print()