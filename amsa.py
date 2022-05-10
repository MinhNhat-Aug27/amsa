import numpy as np

data = np.array([[3.7,  5.7,  3.8,  3.2,  3.1,  4.6,  2.4,  7.2,  6.7,  5.4,  3.9,  4.5,  3.5,  4.5,  1.5,  8.5,  4.5,  4.1,  ],
                [48.5, 65.1, 47.2, 53.2, 55.5, 36.1, 24.8, 33.1, 47.4, 54.1, 36.9, 58.8, 27.8, 40.2, 13.5, ]], dtype= float)
# num of variables
p = len(data)
# num of records            
n = len(data[0])

X_mean = []
s = [[]]

for i in range(p):
    sum = 0
    for j in range(n):
        sum += data[i,j]
    X_mean.append(sum/n)

for i in range(p):
    sum = 0
    for j in range(n):
        print("")


print(X_mean)