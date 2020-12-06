# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:35:13 2020

@author: Saptarshi Mondal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('Data.csv')

#creating dummy variables
dummy=pd.get_dummies(dataset,columns=['Country'],drop_first=True)
dummy.head()
dummy1=pd.get_dummies(dataset,columns=['Purchased'],drop_first=True)

x=dummy.iloc[:,[0,1,3,4]].values
y=dummy1.iloc[:,[3]].values

#handling missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy="mean",axis=0)
imputer=imputer.fit(x[:,0:3])
x[:,0:3]=imputer.transform(x[:,0:3])


#splititng into test and training
from sklearn.cross_validation import train_test_split
x_test,x_train,y_test,y_train=train_test_split(x,y,train_size=0.2,random_state=0)

#feature scalling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x,y)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
