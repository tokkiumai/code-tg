import math
from sklearn.linear_model import LinearRegression

x = []
y = []

with open('data.csv') as file:
    for line in file:
        xx, yy = map(float, line.strip().split(','))
        x.append(xx)
        y.append(yy)
    features = []
    for xx in x:
        current_features = [math.sin(xx) ** 2, math.log(xx) ** 2, math.sin(xx) * math.log(xx), xx ** 2]
        features.append(current_features)
    lm = LinearRegression()
    lm.fit(features, y)
    coeffs = lm.coef_
    a = math.sqrt(coeffs[0])
    b = math.sqrt(coeffs[1])
    c = coeffs[3]
    print(a, b, c)
