try:
    with open('bang.data') as fd:
        filename=fd.readlines()
        for name in filename:
            print(name,end='')
        print('-'*50)
        print(type(filename))
except FileNotFoundError:
    print('your selected file is not found')