import json
import matplotlib.pyplot as plt
import os
import sys


LEARNING_RATE = 0.1
EPOCHS = 1000
THETAS_FILE = "thetas.json"


def read_data(data_file):
    mileage = []
    prices = []

    with open(data_file, "r") as file:
        next(file)
        for line in file:
            x, y = line.strip().split(",")
            mileage.append(float(x))
            prices.append(float(y))

    return mileage, prices, len(mileage)


def normalize_mileage(mileage):
    max_mileage = max(mileage)
    if max_mileage <= 0:
        print("invalide data\n")
        sys.exit(1)
    normalized = [m / max_mileage for m in mileage]
    return normalized, max_mileage


def estimate_price(theta0, theta1, x):
    return theta0 + theta1 * x


def rmse(n, prices, theta0, theta1, mileage):
    total = 0.0
    for i in range(n):
        error = estimate_price(theta0, theta1, mileage[i]) - prices[i]
        total += error ** 2
    return (total / n) ** 0.5


def derivatives(n, prices, theta0, theta1, mileage):
    d0, d1 = 0.0, 0.0
    for i in range(n):
        error = estimate_price(theta0, theta1, mileage[i]) - prices[i]
        d0 += error
        d1 += error * mileage[i]
    return (2 / n) * d0, (2 / n) * d1


def save_thetas(theta0, theta1, max_mileage):
    with open(THETAS_FILE, "w") as f:
        json.dump(
            {
                "theta0": theta0,
                "theta1": theta1,
                "max_mileage": max_mileage
            },
            f
        )


def show_plot(mileage, prices, theta0, theta1, max_mileage):
    plt.scatter(mileage, prices, color="red",label="Data points")
    x = [0, max_mileage]
    y = [estimate_price(theta0, theta1, xi / max_mileage) for xi in x]
    plt.plot(x, y, label="Regression line")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


def train():
    if len(sys.argv) < 2:
        print("Usage: python train.py <data.csv> [accuracy]")
        sys.exit(1)

    data_file = os.path.expanduser(sys.argv[1])
    if not os.path.isfile(data_file):
        raise FileNotFoundError(f"File not found: {data_file}")

    theta0, theta1 = 0.0, 0.0
    mileage, prices, n = read_data(data_file)
    norm_mileage, max_mileage = normalize_mileage(mileage)

    for _ in range(EPOCHS):
        d0, d1 = derivatives(n, prices, theta0, theta1, norm_mileage)
        theta0 -= LEARNING_RATE * d0
        theta1 -= LEARNING_RATE * d1

    save_thetas(theta0, theta1, max_mileage)

    if len(sys.argv) == 3 and sys.argv[2] == "accuracy":
        print(f"RMSE: {rmse(n, prices, theta0, theta1, norm_mileage):.4f}")
    else:
        show_plot(mileage, prices, theta0, theta1, max_mileage)


if __name__ == "__main__":
    train()
