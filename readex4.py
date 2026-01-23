try:
    filename=input('Enter the file name to view Its Content:')
    fp=open(filename,'r')
except FileNotFoundError:
    print('Fil not found try new one')
else:
    filedata=fp.read()
    if len(filedata)==0:
        print('File is empty')
    else:
        print('-'*50)
        print('Content of:{}'.format(fp.name))
        print('-'*50)
        print(filedata)