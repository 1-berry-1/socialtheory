import pandas as pd
import numpy as np

def dataframe_formation(file1, file2):
    costs = open(file1).readlines()
    speeds = open(file2).readlines()

    costs2 = []

    for i in costs:
        if 'Flag' in i:
            continue
        costs2.append(i)

    dataframe = {'country': [], 'broadband cost':[], 'broadband cost adj': []}

    for i in costs2:
        country, bbcperm, bbcpermadj = i.split('\t')
        if '\n' in bbcpermadj:
            bbcpermadj = bbcpermadj[:-2]

        dataframe['country'].append(country)
        dataframe['broadband cost'].append(bbcperm)
        dataframe['broadband cost adj'].append(bbcpermadj)

    df1 = pd.DataFrame(dataframe)

    dataframe2 = {'country':[], 'mobile connectivity(download)': []}

    for i in speeds[1:]:
        index, rank, country, speed = i.split('\t')
        if '\n' in speed:
            speed = speed[:-2]

        dataframe2['country'].append(country)
        dataframe2['mobile connectivity(download)'].append(speed)

    df2 = pd.DataFrame(dataframe2)

    return df1, df2