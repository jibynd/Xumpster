def findfunc(nam):
    if sum([letter.isupper() for letter in nam]) == 1:
        pattern = nam + '.*'
    else:
        pattern = ''.join([d+'.*' for d in nam])
    for t in dir(keras.layers):
        rr = re.findall(pattern, t)
        if len(rr) > 0:
            return rr[0]
            break
        else:
            continue
            
def NeulNet(input_shape,*archi):
    import keras
    from keras.layers import Input
    from keras.models import Model
    X_input = Input(shape=input_shape)
    X = X_input
    for lay in archi[:-1]:
        funcName = findfunc(lay['name'])
        Func = getattr(keras.layers, funcName)
        X = Func(**lay['arg'])(X)
    model = Model(inputs = X_input, outputs = X, name='HappyModel')
    model.compile(**archi[-1])
    return model
