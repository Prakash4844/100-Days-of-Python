with open('file.txt', 'r') as f:
    print(f.read())

with open('file.txt', 'w') as f:
    f.write('Hello World\n')

with open('file.txt', 'a') as f:
    f.write('Hello Pycharm')
