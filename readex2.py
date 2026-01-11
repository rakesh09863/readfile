try:
    with open('bang.data') as fd:
        filename=fd.read()
        print('-'*50)
        print(filename)
        print(type(filename))
        print('-'*50)
except FileNotFoundError:
    print('select file is not Found')