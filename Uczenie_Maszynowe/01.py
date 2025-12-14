import numpy as np
import matplotlib.pyplot as plt
# from sklearn 
import sklearn.datasets as skd

# np.random.seed(123)
# 1

    # x = np.random.normal(5.0, 1.0, 500)
    # y = np.random.normal(10.0, 1.0, 500)

    # plt.scatter(x, y)
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.show()

    # x1 = np.random.normal(5.0, 1.0, 500)
    # y1 = np.random.normal(10.0, 1.0, 500)

    # plt.subplot(1, 2, 1)
    # plt.scatter(x, y)
    # plt.xlabel("X")
    # plt.ylabel("Y")

    # plt.subplot(1, 2, 2)
    # plt.scatter(x1, y1)
    # plt.xlabel("X")
    # plt.ylabel("Y")

    # plt.show()
x, y = skd.make_blobs(n_samples=6000, centers=5, n_features=2, random_state=432)

plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()
x, y = skd.load_iris(return_X_y=True)
print(x)

frameData = skd.load_iris(as_frame=True)
print(frameData.keys())

df = frameData['frame']
df_X = frameData['data']
df_Y = frameData['target']
# print(frameData['target_names'])
# print(feature)

from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

scaledDFIris = scale.fit_transform(df_X)
# print(scaledDFIris)

np.random.seed(333)
newX = np.random.normal(3, 1, 100)
newY = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

myModel = np.poly1d(np.polyfit(train_x, train_y, 4))

myModelLinie = np.linspace(0, 6, 100)
