def fun(nd, d, k) :
    for i in nd.keys() :
        if type(nd[i]) == int :
            d[(k+'.'+i).strip('.')] = nd[i]
        else :
            d = fun(nd[i], d, (k+'.'+i).strip('.'))
    return d
nested_dict = eval(input())
r = fun(nested_dict, dict(), '')
print(r)
