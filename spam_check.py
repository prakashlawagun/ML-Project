# -*- coding: utf-8 -*-
"""Spam check.ipynb

Automatically generated by Colaboratory.

"""

#importing dependencies
import numpy as pn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

raw_mail_data = pd.read_csv('/content/mail_data.csv')

raw_mail_data.head()

raw_mail_data.shape

mail_data =raw_mail_data.where((pd.notnull(raw_mail_data)),'')

mail_data.head()

mail_data.shape

"""Label Encoding
0---->Spam mail
1---->Ham mail
"""

mail_data.loc[mail_data['Category']=='spam','Category'] = 0
mail_data.loc[mail_data['Category']=='ham','Category'] = 1

#spereting data 
X = mail_data['Message']
Y = mail_data['Category']

print(X)
print(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

print(X.shape,X_train.shape,X_test.shape)

"""Feature extraction """

#transform text data into featrue vectors
feature_extraction = TfidfVectorizer(min_df=1,stop_words='english',lowercase='True')

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

#conveting Y train into integer

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train)

print(X_train_features)

"""Training model

"""

#training logistic regression model
model = LogisticRegression()

model.fit(X_train_features,Y_train)

"""Evaluating trained model"""

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)

print("Accuracy on training data: ",accuracy_on_training_data)

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_test_data)

print("Accuracy on test data: ",accuracy_on_test_data)

"""Building prediction system"""

input_data = ["Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"]

input_data_features = feature_extraction.transform(input_data)

prediction = model.predict(input_data_features)

if(prediction[0] == 0):
   print("Spam mail is detect")
else:
   print("Ham mail is detect")

