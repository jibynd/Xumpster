# Implicit Optimization with Automatically Updated Learning Rates

Description

This algorithm allows for the training of any model using any gradient descent optimizer (such as Adam or RmsProp) without an explicit decaying function for the adjustment of learning rates to increase optimality and, most importantly, without the need to find the best learning rate, which can take much time to do. 

Input Requirements

This optimization method will take as inputs: an array of r values for the learning rate alpha {alpha = 10**(-2)}, your model as a function, the parameter values theta, and a dictionary containing all the other inputs. 
For the model, it should not have a for loop for updating whatever parameters it’s trying to learn. This algorithm will do that in the best possible way.

Summary

Instead of finding the best learning rate alpha and then learn from it the optimal parameters, get the best cost reduction possible from every alpha until the change in cost converges to a certain threshold.
