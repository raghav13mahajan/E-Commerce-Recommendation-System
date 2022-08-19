# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 18:52:00 2016

@author: Raghav
"""

from scipy import spatial

dataSetI = [3, 45, 7, 2]
dataSetII = [2, 54, 13, 15]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
print result

'''
def sim_adjustedCosine(prefs,p1,p2):
    x = []
    y = []
    n = []
    si = {}
    
    for items in prefs[p1]:
        if items in prefs[p2]:
            si[items] = 1
            x.append(prefs[p1][items])   
            y.append(prefs[p2][items])
            n.append(sum(rating[items])/len(rating[items]))
    k = len(si)
    if k == 0:
        return 0
    x = x - n
    y = y - n
    ans = 1 - spatial.distance.cosine(x,y)
    return ans
    '''