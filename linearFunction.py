mileage = []
realPrice = []
n = 0
tetha0 = 0.0
tetha1 = 0.0
learningRate = 0.00001
epochs = 1000


def readData():
    global mileage, realPrice, n
    with open("data.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            mileage.append(int(data[0]))
            realPrice.append(int(data[1]))
            n += 1


def estimatePrice(tetha0, tetha1, mileage):
    return tetha0 + tetha1 * mileage


def MSE(n, realPrice, tetha0, tetha1, mileage):
    total = 0
    for i in range(n):
        error = realPrice[i] - estimatePrice(tetha0, tetha1, mileage[i])
        total += error ** 2
    return total / n


def DerivativeTetha0(n, realPrice, tetha0, tetha1, mileage):
    total = 0
    for i in range(n):
        error = realPrice[i] - estimatePrice(tetha0, tetha1, mileage[i])
        total += error
    return (-2 / n) * total


def DerivativeTetha1(n, realPrice, tetha0, tetha1, mileage):
    total = 0
    for i in range(n):
        error = realPrice[i] - estimatePrice(tetha0, tetha1, mileage[i])
        total += error * mileage[i]
    return (-2 / n) * total


def trainModel():
    global tetha0, tetha1
    readData()

    for _ in range(epochs):
        d0 = DerivativeTetha0(n, realPrice, tetha0, tetha1, mileage)
        d1 = DerivativeTetha1(n, realPrice, tetha0, tetha1, mileage)

        tetha0 -= learningRate * d0
        tetha1 -= learningRate * d1


trainModel()

