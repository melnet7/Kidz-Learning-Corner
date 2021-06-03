import numpy as np
import pandas as pd
import pydotplus
import sklearn as sk
import sklearn.preprocessing as pre
import sklearn.tree as tree
from PIL import Image

data = pd.read_csv("c:/00/icecream.csv")

# print(data)

label_encoder = pre.labelEncoder
label_encoder.fit(data['Season'].astype(str))
data['Season'] = label_encoder.transform(data['Season'].astype(str))

label_encoder.fit(data['State'].astype(str))
data['State'] = label_encoder.transform(data['State'].astype(str))

label_encoder.fit(data['Flavor'].astype(str))
data['Flavor'] = label_encoder.transform(data['Flavor'].astype(str))

X = data[['Season', 'Age', 'State']].values
Y = data['Flavor'].values

# print(Y)

classifier = tree.DecisionTreeClassifier()
my_tree =  classifier.fit(X,Y)

out = open('c:/00/tree.dot', 'w')
dot_output = tree.export_graphviz(my_tree, out_file=out, feature_names=['Season', 'Age', 'State']),
    class_names=[ Mint', 'Orange', 'Chocolate']

