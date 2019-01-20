# Modelers
Explanations coming soon

## Example usage sklearn

global path 
path = '/Users/jibynd/anaconda/envs/snakes/lib/python3.6/site-packages/'

mogolearn('clu.km') =  sklearn.cluster.k_means_.k_means

mogolearn('dst.lir') =  sklearn.datasets.base.load_iris
  
mogolearn('e.AB') = mogolearn('en.AB') = mogolearn('e.AdaBoost') = sklearn.ensemble.weight_boosting.AdaBoostClassifier
  
mogolearn('lm.RiC') = mogolearn('lm.RidC') = sklearn.linear_model.ridge.RidgeCV

mogolearn(['d.LDAna', 'lm.LR', 'kr.KRi', 'fex.img.itg']) =  [keras.wrappers.scikit_learn.KerasClassifier, 
                                                         keras.layers.core.Dense, 
                                                         keras.layers.pooling.MaxPooling2D, 
                                                         keras.regularizers.l1_l2, 
                                                         keras.preprocessing.text.Tokenizer] 


## Example usage keras

global path 
path = '/Users/jibynd/anaconda/envs/snakes/lib/python3.6/site-packages/keras'

mogolearn(['w.sl.KC', 'l.Den','l.MP2', 're.ll', 'prep.tx.Tok'], module='keras') = [sklearn.discriminant_analysis.LinearDiscriminantAnalysis, 
 sklearn.linear_model.base.LinearRegression, 
 sklearn.kernel_ridge.KernelRidge, 
 function sklearn.feature_extraction.image.img_to_graph] 

mogolearn('re.l1') = mogolearn('regu.l1') =  keras.regularizers.l1

mogolearn('re.ll') =  keras.regularizers.l1_l2

mogolearn('app.vgg') = keras.applications.vgg16

mogolearn('app.r50') = mogolearn('app.res50') = keras.applications.resnet50
