
## Single function for building Neural Networks with modifiable optimizations 

# Motivation

It's not uncommon nowadays to build networks that have thousands of layers. This function is a great tool that can be used for that as you'll see.
On the othe end, one way to start extracting useful information about data is to try different models and choose those with the best performance and then improve. Such task would be facilitated if there existed one or two joint functions that can be accessed using some iterations that feed them with various parameters among which the specific model we want to try is given (model = “SVM”). 
This general function is a first step toward building a broader one. This version allows the user to access all features that are present in the following modules: keras.(optimizers, layers, losses, metrics, regularizers). It does not require to know or write the exact name of the function needed as it will figure it out given a good approximation following some simple naming convention. 

# Flexibility

The challenge about having a general function is that it’s still hard to keep track what to input. So this methodology will provides much flexibility in that we can write our own mapper that turns our input into an expected architecture. So we can define the easiest way to build a neural network without being forced to any style. Different options will shown in the example section.

# Naming convention

Having seen the main keras classes, I have noticed that a simple naming convention identifies them all uniquely. There are only two rules, which can be slightly broken if one wants but you need to be familiar with the actual functions you’re calling.
First, if the function needed has at least two uppercase letters and numerics, put them in order with at least one lowercase. The first letter should always be provided. For instance, to use MaxPooling2D, we put ‘MaP2D’ or ‘MPo2D’. We may use ‘MP2D’ or ‘M2D’ or even ‘M2’, but we need be careful.
Second, if the function only has one upper or less, we should provide at least three consecutive letters start from the beginning. For instance, Activation becomes ‘Act’. Something like ‘Avt’ will work but it’s not recommended since future versions might be tighter in requirements. 

# Example

In keras, there is an example for building a Visual question answering model. The biggest chunk is as follow:

vision_model = Sequential()
vision_model.add(Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)))
vision_model.add(Conv2D(64, (3, 3), activation='relu'))
vision_model.add(MaxPooling2D((2, 2)))
vision_model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
vision_model.add(Conv2D(128, (3, 3), activation='relu'))
vision_model.add(MaxPooling2D((2, 2)))
vision_model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
vision_model.add(Conv2D(256, (3, 3), activation='relu'))
vision_model.add(Conv2D(256, (3, 3), activation='relu'))
vision_model.add(MaxPooling2D((2, 2)))
vision_model.add(Flatten())

Using this function, we have:

pre_archi = [(Co2D, 64, (3,3), ‘relu’, ‘same’), ‘previous[:-1]’, (‘MP2D’, (2,2)),	 (‘Co2D’, 128, (3,3), ‘relu’, ‘same’), ‘previous[:-1]’,  ‘pre_archi[2]’, (Co2D, 256, (3,3), ‘relu’, ‘same’), ‘previous[:-1], ‘previous’,  ‘pre_archi[2]’, (‘Flat’)]

pre_archi will be mapped to the complete following architecture.

architecture = mapper(pre_archi)

 architecture =  [{‘name’: ‘Co2D’, ‘arg’:{ ’filters’:64,  ‘kernel_size’: (3, 3), ‘activation’:’relu', ‘padding’:’same’}},  {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:64, ‘kernel_size’: (3, 3), ‘activation’:’relu’}}, {‘name’: ‘MP2D’, ‘arg’:{‘pool_size’: (2, 2)}}, {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:128,  ‘kernel_size’: (3, 3), ‘activation’:’relu', ‘padding’:’same’}}, {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:64, ‘kernel_size’: (3, 3), ’activation’:’relu’}}, {‘name’: ‘MP2D’, ‘arg’:{‘pool_size’: (2, 2)}}, {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:256,  ‘kernel_size’: (3, 3), ‘activation’:’relu', ‘padding’:’same’}}, {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:256,  ‘kernel_size’: (3, 3), ’activation’:’relu’}}, {‘name’: ‘Co2D’, ‘arg’:{ ’filters’:256, ‘kernel_size’: (3, 3), ‘activation’:’relu’}}, {‘name’: ‘MP2D’, ‘arg’:{‘pool_size’: (2, 2)}}, {‘name’: ‘Fla’, ‘arg’:{}}]

# Advanced Mapping

 A slightly complicated but more general pre_architectures are shown below. In Names, the data format used looks like (structure, number of that structure). This format allows for some power nesting that can be unpacked from the inside to the outside into a complete list, then matched to params’ values to generate the full architecture. In the second version, the same formatting is used in params as well.

Names = [( (((“Co2D”,2), ‘MP2D’), 2), (‘Co2D’,3), ‘MP2d’, ‘Fla’]
params =  [{ ’flt’:64,  ‘k_s’: (3, 3), ‘act’:’relu', ‘pad’:’same’}, { ’flt’:64, ‘k_s’: (3, 3), ‘act’:’relu’},{‘p_s’: (2, 2)}, { ’flt’:128,  ‘k_s’: (3, 3), ‘act’:’relu', ‘pad’:’same’},{ ’flt’:64, ‘k_s’: (3, 3), ’act’:’relu’}},{‘p_s’: (2, 2)},{ ’flt’:256,  ‘k_s’: (3, 3), ‘act’:’relu', ‘pad’:’same’},{ ’flt’:256,  ‘k_s’: (3, 3), ’act’:’relu’}, { ’flt’:256, ‘k_s’: (3, 3), ‘act’:’relu’}, {‘p_s’: (2, 2)},{}]

Names = [( (((“Co2D”,2), ‘MP2D’), 2), (‘Co2D’,3), ‘MP2d’, ‘Fla’]
params = [ ((2, {‘pad’:’same’}), { ’filt’:64, ‘k_s’: (3, 3), ‘act’:’relu’}, {‘p_s’: (2, 2)}),  (2,  { ’filt’:128}),  ((2, {‘pad’:’same’}), { ’filt’:64, ‘k_s’: (3, 3), ‘act’:’relu’}, (2,{})), {‘p_s’: (2, 2)}, {}]

# Possible modifications and Incorporating of more complicated models

This current version does not allow to flexibly choose the parameter names, but it will be added soon as it works the same way as the function name itself.
As for models using structures such as residual networks, inception layers or shared vision models, nested tuples can be used to deal with the specific layers where they are applied. The previos example in Advance Mapping should give you a sense of how that would work. 
