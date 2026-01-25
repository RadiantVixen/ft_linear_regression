import json
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def readData(data_file):
    mileage = []
    realPrice = []

    with open(data_file, "r") as file:
        next(file)
        for line in file:
            data = line.strip().split(",")
            mileage.append(int(data[0]))
            realPrice.append(int(data[1]))
    return mileage, realPrice, len(mileage)


def normalizeMileage(mileage):
    max_mileage = max(mileage)
    normalized = [m / max_mileage for m in mileage]
    return normalized, max_mileage


def estimatePrice(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def RMSE(n, realPrice, theta0, theta1, mileage):
    total = 0.0
    for i in range(n):
        error = estimatePrice(theta0, theta1, mileage[i]) - realPrice[i]
        total += error ** 2
    mean = total / n
    return mean ** 0.5


def DerivativeThetas(n, realPrice, theta0, theta1, mileage):
    d0, d1 = 0.0, 0.0
    for i in range(n):
        error = estimatePrice(theta0, theta1, mileage[i]) - realPrice[i]
        d0 += error
        d1 += error * mileage[i]
    d0 = (2 / n) * d0
    d1 = (2 / n) * d1
    return d0, d1


def save_thetas(theta0, theta1, max_mileage):
    data = {
        "theta0": theta0,
        "theta1": theta1,
        "max_mileage": max_mileage
    }
    with open("thetas.json", "w") as f:
        json.dump(data, f)


def showPlot(mileage, realPrice, theta0, theta1, max_mileage):
    plt.scatter(mileage, realPrice, color='blue', label='Data Points')
    x = np.array([0, max_mileage])
    y = theta0 + theta1 * (x / max_mileage)
    plt.plot(x, y, color='red', label='Regression Line')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Mileage vs Price')
    plt.legend()
    plt.show()


def trainModel():
    theta0 = 0.0
    theta1 = 0.0
    learningRate = 0.1
    epochs = 1000

    if len(sys.argv) > 1 and sys.argv[1].strip():
        data_file = os.path.expanduser(sys.argv[1].strip())
    else:
        data_file = os.path.expanduser(input("Enter the path to the CSV data file (mileage,price): ").strip())

    if not os.path.isfile(data_file):
        raise FileNotFoundError(f"Data file not found: {data_file}")
        exit(-1)
    mileage, realPrice, n = readData(data_file)
    normalized_mileage, max_mileage = normalizeMileage(mileage)
    for epoch in range(epochs):
        d0, d1 = DerivativeThetas(n, realPrice, theta0, theta1, normalized_mileage)
        theta0 -= learningRate * d0
        theta1 -= learningRate * d1

    save_thetas(theta0, theta1, max_mileage)
    print(f"the precision of the algorithm RMSE: {RMSE(n, realPrice, theta0, theta1, normalized_mileage):.4f}")
    showPlot(mileage, realPrice, theta0, theta1, max_mileage)




if __name__=="__main__":
    trainModel()
