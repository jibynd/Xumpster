import numpy as np

def conver(start, end, tol):
    start = np.array(start); end = np.array(end)
    diff = end - start; RelaDiff = (end-start)/start
    if not (diff < 0).all():
        if end[-1] - start[0] > 0:
            return True
        else:
            return False
    else:
        FlatCostTrend = (abs(RelaDiff) < tol/100).all()
        return  FlatCostTrend or end[-1] < 10**(-4)


def PwAlpha(alphas,func, theta, args):
    Costs = []; na = np.nan; i = 0
    while (np.isnan(na) or np.isinf(na)) and i!= len(alphas):
        r = alphas[i]; a = 10**(-r)
        Theta0 = theta
        for ii in range(100):
            Out = func(learning_rate = a, theta = Theta0, **args)
            Theta0 = Out['theta']
        na = Out['cost']
        i += 1
    alphas = alphas[i-1:]; OutConv = False; l = 0
    while not OutConv and l != len(alphas):
        a = 10**(-alphas[l]); Inconv = False; In_Costs = []; p = 0
        while not Inconv and p < 500:
            Out = func(learning_rate = a,theta = theta, **args)
            theta = Out['theta']
            single_cost = Out['cost']
            In_Costs.append(single_cost)
            if p > 3:
                Inconv = conver(In_Costs[p-4:p-1],In_Costs[p-3:p],0.1)
            p += 1
        Costs.append(In_Costs[-1]);# print (-np.log(a),theta,len(In_Costs))
        if l > 7:
            OutConv = conver(Costs[l-8:l-1],Costs[l-7:l],0.1)
        else:
            OutConv = False
        l += 1
    return theta
    
# Example of what the input function looks like

def LRR(X,Y,theta,learning_rate):
    n,m = X.shape; Th = theta
    Yp = np.dot(Th,X)
    Gr = np.dot((Yp-Y),X.T)/2/m;#print (Yp.shape)
    Th = Th - learning_rate*Gr
    Yp = np.dot(Th,X)
    c = np.sum((Yp-Y)**2)/m 
    return {'cost':c,'theta':Th}

# Example of function call
PWA(np.linspace(0,10,40),LRR,np.array([0.01,0.01]),{'X':X,'Y':Z})
