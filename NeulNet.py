def findfunc(name, name_list):
    if sum([letter.isupper() for letter in name]) <= 1:
        pattern = name + '.*'
    else:
        pattern = ''.join([letter+'.*' for letter in name])
    for item in name_list:
        regex = re.findall(pattern, item)
        if len(regex) > 0:
            return regex[0]
            break
        else:
            continue
            
def opti_build(compiler_arg):
    myList = ['optimizer', 'loss', 'metrics']
    myDict = {}
    for key in compiler_arg:
        val = compiler_arg[key]
        compiler_arg_name = findfunc(key, myList)
        if compiler_arg_name == 'optimizer':
            if type(val) == str:
                true_val = findfunc(val, dir(keras.optimizers))
                myDict[compiler_arg_name] = true_val
            else:
                opt_name = findfunc(val['name'], dir(keras.optimizers))
                opt = getattr(keras.optimizers, opt_name)
                myDict[compiler_arg_name] = opt(**val['arg'])
        elif compiler_arg_name == 'loss':
            true_val = findfunc(val, dir(keras.losses))
            myDict[compiler_arg_name] = true_val
        elif compiler_arg_name == 'metrics':
            metr_list = []
            for met in val:
                true_val = findfunc(met, dir(keras.metrics))
                metr_list.append(true_val)
            myDict[compiler_arg_name] = metr_list
        else:
            print ('Argument name not understood, please rename')
    return myDict


def NeulNet(input_shape,architecture):
    import keras
    from keras.layers import Input
    from keras.models import Model
    from keras import regularizers
    import importlib
    X_input = Input(shape=input_shape)
    X = X_input
    for lay in architecture[:-1]:
        funcName = findfunc(lay['name'], dir(keras.layers))
        Func = getattr(keras.layers, funcName)
        X = Func(**lay['arg'])(X)
    model = Model(inputs = X_input, outputs = X, name='myModel')
    compiler_arg = architecture[-1]
    reformatted_compil = opti_build(compiler_arg)
    model.compile(**reformatted_compil)
    return model 
