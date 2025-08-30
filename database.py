import pandas as pd
import numpy as np
import os

def check_plate(num_plate, df):
    checking1 =df['Numberplate'].str.contains(num_plate)
    checking2 = len(num_plate) == df['npl']
    #print(checking1)
    #print(checking2)
    checking = np.logical_and(checking1, checking2)
    print(checking)
    checking = checking * 1.0
    sum_plate = np.sum(checking, axis = 0)
    print(bool(sum_plate))


def make_npl(df):
    i = len(df)
    df_temp = np.zeros(i)
    j = 0
    while j < i:
        x = len(df.iloc[j,0])
        df_temp[j] = int(x)
        j += 1
    df['npl'] =  df_temp
    df.to_csv("test1.csv")
    return

def clear_file():
    os.remove('test1.csv')

df=pd.read_csv('test.csv')

make_npl(df)
df1=pd.read_csv('test1.csv')
check_plate('ABC1234', df1)

print('Done!')

clear_file()