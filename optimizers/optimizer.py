import numpy as np
import matplotlib as mlp
import collections
from random import *

def PWA(alphas,func, theta, args):
    Costs = []; na = np.nan; i = 0
    while (np.isnan(na) or np.isinf(na)) and i!= len(alphas):
        r = alphas[i]; a = 10**(-r)
        Theta0 = theta
        for ii in range(500):
            Out = func(learning_rate = a, theta = Theta0, **args)
            Theta0 = Out['theta']
        na = Out['cost']
        i += 1
    alphas = alphas[i-1:]; conv = False; l = 0
    while not conv and l != len(alphas):
        a = 10**(-alphas[l]); conv2 = False; In_Costs = []; p = 0
        while not conv2 and p < 1000:
            Out = func(learning_rate = a,theta = theta, **args)
            theta = Out['theta']
            single_cost = Out['cost']
            In_Costs.append(single_cost)
            if p > 0:
                conv2 = conver(In_Costs[p-1],In_Costs[p],0.1)
            p += 1
        Costs.append(In_Costs[-1]);# print (-np.log(a),theta,len(In_Costs))
        if l > 0:
            conv = conver(Costs[l-1],Costs[l],0.1)
        else:
            conv = False
        l += 1
    return theta

def conver(start,end,tol):
    if end > start:
        return True
    else:
        return (abs((end-start)/start)<tol/100) or end < 10**(-4)

def LRR(X,Y,theta,learning_rate):
    n,m = X.shape; Th = theta
    Yp = np.dot(Th,X)
    Gr = np.dot((Yp-Y),X.T)/2/m;#print (Yp.shape)
    Th = Th - learning_rate*Gr
    Yp = np.dot(Th,X)
    c = np.sum((Yp-Y)**2)/m
    return {'cost':c,'theta':Th}

    def data_generator(feature_size, data_size):
    coef = np.random.random((1, feature_size))*10
    coef = np.around(coef, decimals=2)
    i = 0

    x = []
    temp_t = 0
    while i<feature_size:
        t = random()
        t_2 = np.random.random((1, data_size))**(10**-t)
        # t_2 = np.random.random((1, data_size))
        x_i = np.random.randint(1, 10, (1, data_size)) * t_2
        if((temp_t%3==0 or t<0.5) and temp_t!=0 and i!= 0):
            x_temp = np.array(x[i-1])
            x_i = x_temp*x_i
        elif(temp_t%5==0 and temp_t!=0 and i!= 0):
            x_i = np.dot(x_i, np.random.random((data_size, data_size)))**t
        x.append(x_i)
        temp_t = t
        i+=1
    x = np.array([x])
    x.resize(feature_size, data_size)
    x = np.around(x, decimals=5)

    i = 0
    y = []
    while i<data_size:
        t = random()
        x_temp = np.array(x[: ,i])
        x_temp.resize(feature_size, 1)
        y_i = np.dot(coef, x_temp)
        y.append(y_i)
        i+=1
    y = np.array(y)
    y.resize(1, data_size)
    result = dict()
    result['x'] = x
    result['y'] = y
    result['coef'] = coef
    return result
