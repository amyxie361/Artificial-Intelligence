# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# get the columns and index names for a new pandas DataFrame
# def get_points (filename):
#     d = {}   # d denotes the distance form start to the point, but currently it just presents the points
#     f = file(filename)
#     while True:
#         s = f.readline()
#         if s == '':
#             break
#         s = s.strip().split(' ')
#         d[s[0]] = d[s[1]] = 0
#     return d 

# def get_points ():
#     d = {}   # d denotes the distance form start to the point, but currently it just presents the points
#     s = raw_input()
#     l = s.split('\n')[1:]
#     for s in l:
#         if 'END' in s:
#             break
#         s = s.strip().split(' ')
#         d[s[0]] = d[s[1]] = 0
#     return d 

def get_points ():
    d = {}   # d denotes the distance form start to the point, but currently it just presents the points
    s = raw_input()
    while True:
        print "s is",s
        s = raw_input()
        if 'END' in s:
            break
        s = s.strip().split(' ')
        d[s[0]] = d[s[1]] = 0
    return d   

# get the value of cost and fill df : the DataFrame which denotes the graph
def set_df (filename, d):
    df = pd.DataFrame(index = d.keys(),columns = d.keys())
    f = file('input.txt')
    while True:
        s = f.readline()
        if s == '':
            break
        s = s.strip().split(' ')
        df.loc[s[0],s[1]]=int(s[2])
        
    # adding prior vector to df : the prior point of each checked points
    df2 = pd.DataFrame(index = ['prior'],columns = d.keys())
    df = df.append(df2)
    return df

# the kernel of ucs_search, with a dataframe as input, converting the last line of df
def ucs_search (df, d):
    # keys denots the unchecked points
    keys = d.keys()
    keys.remove('Start')
      
    # v_checked is list storing checked points
    print ''
    v_checked = ['Start']
    
    # iterating :kernel of ucs search
    while len(v_checked) != len(d):
        min = -1
        for s1 in v_checked:
            for s2 in keys:
                cost = df.loc[s1][s2]
                if np.isnan(cost) == False:
                    cost = cost + d.get(s1)
                    if min == -1 or min > cost:
                        min = cost
                        t_point = s2
                        t_point_prior = s1
        df.loc['prior'][t_point] = t_point_prior
        d[t_point] = min
        if t_point != 'Goal':
            keys.remove(t_point)
        v_checked.append(t_point)
                    
    # df with prior denots optimum path
    print ''
    print df
    return df
    
    
# get the shortest path from df
def get_path (df):
    # iterate to get the path through each 'prior' point
    s = 'Goal'
    result = [s]
    while True:
        t = df.loc[:,s].loc['prior']
        result.append(t)
        s = t
        if s == 'Start':
            break
    result = result[::-1]
    r = '->'.join(result)    # final result
    print ''
    print 'Result:', r
    print 'Total lenth:', d.get('Goal')
    return r


# write r to output.txt
def write_txt(filename,r):
    f = open(filename,'w')
    f.write(r)
    f.close()




d = get_points()
df = set_df('input.txt',d)
df_result = ucs_search(df,d)
r = get_path(df_result)
write_txt('output.txt',r)




