## Implicit Optimization with Automatically Updated Learning Rates

#Description

This algorithm allows for the training of any model using any gradient descent optimizer (such as Adam or RmsProp) without an explicit decaying function for the adjustment of learning rates to increase optimality and, most importantly, without the need to find the best learning rate, which can take much time to do. 

#Input Requirements

This optimization method will take as inputs: an array of r values for the learning rate alpha {alpha = 10**(-r)}, your model as a function, the parameter values theta, and a dictionary containing all the other inputs. A great advantage is that runtime is insensitive to the number of r values that are considered. 
For the model, it should not have a for loop for updating whatever parameters it’s trying to learn; it needs update only once. This algorithm will do that in the best possible way.

#Speed Test

If for instance you want to run 2500 iterations of 9 alphas values and then select the best one, your number of total iterations will add up to 25000. Using this optimizer, at most, you'll run for, as an example, 2500 iterations (you can choose a smaller value and modify the code accordingly) for each alpha while changing the weights as the iterations shift from one level of alpha to another, then compare the runtime. A much significant difference might be observed when training huge models like neural networks with a hundred thousands parameters.

#Summary

Instead of finding the best learning rate alpha and then learn from it the optimal parameters, get the best cost reduction possible from every alpha until the change in cost converges to a certain threshold.
