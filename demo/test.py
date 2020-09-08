from modules.configEmail import EMailInstrument as emi
import os

if __name__ == '__main__':
    path = 'D://pycharm//IT_modules_demo//result//20200918'
    files = os.listdir(path)
    flag = True
    temp = None
    i = 0
    while flag:
        if temp == None:
            temp = files[i]
        else:
            if temp.split('.')[0] < files[i].split('.')[0]:
                temp = files[i]
        i+=1
        if i == len(files):
            flag = False
    print(temp)