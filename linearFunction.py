import json


def readData():
    mileage = []
    realPrice = []
    
    with open("data.csv", "r") as file:
        next(file)
        for line in file:
            data = line.strip().split(",")
            mileage.append(int(data[0]))
            realPrice.append(int(data[1]))
    return mileage, realPrice, len(mileage)

def normalizeMileage(mileage):
    max_mileage = max(mileage)
    normalized = [m / max_mileage for m in mileage]
    return normalized


def estimatePrice(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def MSE(n, realPrice, theta0, theta1, mileage):
    total = 0
    for i in range(n):
        error = estimatePrice(theta0, theta1, mileage[i]) - realPrice[i]
        total += error ** 2
    return total / n



def DerivativeThetas(n, realPrice, theta0, theta1, mileage):
    d0, d1 = 0.0, 0.0
    for i in range(n):
        error = estimatePrice(theta0, theta1, mileage[i]) - realPrice[i]
        d0 += error
        d1 += error * mileage[i]
    d0 = (-2 / n) * d0
    d1 = (-2 / n) * d1
    return d0, d1



def save_thetas(theta0, theta1, max_mileage):
    data = {
        "theta0": theta0,
        "theta1": theta1,
        "max_mileage": max_mileage
    }
    with open("thetas.json", "w") as f:
        json.dump(data, f)


def trainModel():
    theta0 = 0.0
    theta1 = 0.0
    learningRate = 0.00001
    epochs = 1000
    mileage, realPrice, n = readData()
    normalized_mileage= normalizeMileage(mileage)

    # for _ in range(epochs):
    d0 , d1 = DerivativeThetas(n, realPrice, theta0, theta1, normalized_mileage)
    theta0 -= learningRate * d0
    theta1 -= learningRate * d1
    
    save_thetas(theta0, theta1, max(mileage))



if __name__=="__main__":
    trainModel()
