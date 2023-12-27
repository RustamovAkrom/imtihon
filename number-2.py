from  multiprocessing import Process
import  os

pakeg = 'descriptions'


def data_print(func):
    def inner():
        x = func()
        print(x)
    return inner

@data_print
def get_upper():

    global pakeg

    upper_txt = []

    ls = os.listdir(pakeg)
    for i in ls:
        with open(pakeg + '/' + i, 'r') as f:
            x = f.read().split('\n')
            x = x[2]
            xls = x.split()
            for i in xls:
                if i[0].isupper():
                    upper_txt.append(i)

    with open('upper.txt','w+') as file:
        for i in upper_txt:
            file.write(i + '\n')

    return upper_txt

if __name__=='__main__':
    proses = Process(target=get_upper())
    proses.start()
    proses.join()
