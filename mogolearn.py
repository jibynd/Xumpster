global path
path = '/Users/username/anaconda/envs/snakes/lib/python3.6/site-packages/'

def mogolearn(function, module ='sklearn'):
    single = False
    if type(function) == str:
        function = [function]
        single = True
    import importlib
    func_objs = []
    for func in function:
        level = func.split('.')
        full_name = deep_detect(module, level)
        actual_function = full_name.split('.')[-1]
        layers = ''.join([letter+'.' for letter in full_name.split('.')[:-1]])[:-1]
        mod = importlib.import_module(layers)
        func_objs.append(getattr(mod, actual_function))
    if single:
        return func_objs[0]
    else:
        return func_objs
    
 def deep_detect(pre_layer, level):
    goal = None
    if len(level) > 0:
        import os
        import importlib
        mod = dir(importlib.import_module(pre_layer))
        loc = ''.join(node+'/' for node in pre_layer.split('.'))
        try:
            other_mod = [node.split('.')[0] for node in os.listdir(path+loc) if node.split('.')[0] not in mod]
        except:
            other_mod = []
        mod.extend(other_mod)
        func_name = fullfind(level[0], mod); dum = 1/len(func_name); print ('functions',func_name)
        if len(func_name) > 0:
            for fn in func_name:
                templ = level; tempp = pre_layer; print ('fn',fn, level, pre_layer)
                try:
                    pre_layer = pre_layer +'.'+ fn
                    level = level[1:]
                    goal = deep_detect(pre_layer, level)
                    return goal
                    break
                except:
                    level = templ; pre_layer = tempp
                    if fn == func_name[-1]: dum = 1/0
                    continue
            return goal
            print ('dum = 0'); dum = 1/0
        else: return 'Error in input'
    else:
        return pre_layer
    
def deep_detect(pre_layer, level):
    goal = None
    if len(level) > 0:
        import os
        mod = dir(importlib.import_module(pre_layer))
        loc = ''.join(node+'/' for node in pre_layer.split('.'))
        try:
            other_mod = [node.split('.')[0] for node in os.listdir(path+loc) if node.split('.')[0] not in mod]
        except:
            other_mod = []
        mod.extend(other_mod)
        func_name = fullfind(level[0], mod); dum = 1/len(func_name); print ('functions',func_name)
        if len(func_name) > 0:
            for fn in func_name:
                templ = level; tempp = pre_layer; print ('fn',fn, level, pre_layer)
                try:
                    pre_layer = pre_layer +'.'+ fn
                    level = level[1:]
                    goal = deep_detect(pre_layer, level)
                    return goal
                    break
                except:
                    level = templ; pre_layer = tempp
                    if fn == func_name[-1]: dum = 1/0
                    continue
            return goal
            print ('dum = 0'); dum = 1/0
        else: return 'Error in input'
    else:
        return pre_layer
    
def fullfind(name, name_list):
    import re
    def matcher(pattern, name_list):
        regex = [re.findall(pattern, mot) for mot in name_list]
        regex = [val[0] for val in regex if len(val) > 0]
        return regex
    pattern = '^'+ name + '\S*'
    full_name = matcher(pattern, name_list)
    pattern = '^'+''.join([letter+'\S*' for letter in name])
    other_name = [name for name in matcher(pattern, name_list) if name not in full_name]
    full_name.extend(other_name)
    return full_name
    
