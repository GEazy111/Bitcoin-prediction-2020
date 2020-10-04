from create_dataset import create_dataset, download_data
import numpy as np

# download_data(num_weeks=100)

dataset = np.loadtxt('dataset.csv', delimiter=',') # 0~16238

train_dataset = dataset[:-5000]
test_dataset = dataset[-5000:]

trainX, trainY = create_dataset(train_dataset,lookback=24)
testX, testY = create_dataset(test_dataset, lookback=24)

print(trainX.shape)
print(trainY.shape)