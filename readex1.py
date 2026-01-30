print('Enter the Data from key board Press @ to stop')
with open('bang.data','a') as fd:
    while(True):
        kbdata=input()
        if kbdata!='@':
            fd.write(kbdata+'\n')
        else:
            print('Data is Written to the file')
            break