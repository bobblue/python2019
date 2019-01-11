import math
import pandas as pd
import numpy as np
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error

df = pd.read_excel('C:/Users/leevi/Desktop/데상트_1월/기상청데이터셋/arima_input_bymonth_test.xlsx')

#list_ondo = df['체감온도'].values.tolist()
list_ondo = df['평균기온'].values.tolist()
series = pd.Series(list_ondo, index = df['연월'])

model = ARIMA(series, order=(0,1,1))
model_fit_ = model.fit(trend = 'c', full_output =True, disp =1)
print(model_fit_.summary())

model = ARIMA(series, order=(0,1,1))
model_fit = model.fit(trend='nc',full_output=True, disp=1)
print(model_fit.summary())

model_fit.plot_predict()

residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())

X = series.values
size = int(len(X) * 0.8)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
    model = ARIMA(history, order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

rmse = math.sqrt(error)
print('Test RMSE: %.3f' % rmse)

# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()

X = series.values
size = int(len(X))
train = X[0:size]

history = [x for x in train]
predictions = list()

for t in range(13):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    print('predicted=%f' % (yhat))
    obs = test[t]
    history.append(obs)

