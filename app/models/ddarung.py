#데이콘 따릉이 문제풀이
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler

class DDarung:



#1. 데이터
path = './_data/ddarung/'
train_set = pd.read_csv(path + 'train.csv', 
                        index_col=0) 


test_set = pd.read_csv(path + 'test.csv', 
                       index_col=0)



train_set =  train_set.dropna()

test_set = test_set.fillna(test_set.mean())


x = train_set.drop(['count'], axis=1) 
#

y = train_set['count']



x_train, x_test, y_train, y_test = train_test_split(x,y,
             train_size=0.75, shuffle=True, random_state=85)

# scaler = MinMaxScaler()
# scaler = StandardScaler()
# scaler = MaxAbsScaler()
scaler = RobustScaler()

scaler.fit(x_train)
print(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x.shape,y.shape) # (1328, 9) (1328,)
print(x_train.shape,x_test.shape)


#2. 모델구성
from sklearn.svm import LinearSVR
model = LinearSVR()


#3. 컴파일, 훈련
model.fit(x_train, y_train)

import datetime
# date= datetime.datetime.now()      # 2022-07-07 17:22:07.702644
# date = date.strftime("%m%d_%H%M")  # 0707_1723
# print(date)

# filepath = './_ModelCheckpoint/k26_9/'
# filename = '{epoch:04d}-{loss:.4f}.hdf5'

model.fit(x_train, y_train, epochs=100, batch_size=10, verbose=1)


#4. 평가, 예측
result = model.score(x_test, y_test) # evaluate 대신 score 사용
print('결과 :', result)

y_predict = model.predict(x_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)
print('r2스코어 : ', r2)


# dropout 적용 후 
# loss :  28.843862533569336
# r2스코어 :  0.6956438021524509

# loss :  33.54220962524414
# r2스코어 :  0.655130804113361