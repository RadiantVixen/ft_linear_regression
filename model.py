import json


def thetas():
    try:
        with open("thetas.json", "r") as f:
            data = json.load(f)
    except:
        print("the thetas file is not valide")
        exit(-1)
    return data["theta0"], data["theta1"], data["max_mileage"]



def PriceEstimation():
    theta0 , theta1, max_mileage = thetas()
    input_value = None
    while not input_value:
            input_value = input("give me the mileage i give u the price\n")
    try:
        input_value = float(input_value)
    except:
        print("u should give a float as a mileage\n")
        exit(1)

    if input_value < 0:
        print("emmm the mileage is negative it make no since don't u think\n")
        exit(1)

    if input_value >= 409764:
        print("Your price car is estimated at 0 euros or under.. You should not sell it.")
        exit(-1)

    print("here u are")
    normalized_mileage = input_value / max_mileage
    estimatePrice = theta0 + theta1 * normalized_mileage
    print(f"{estimatePrice:.3f}")



if __name__=="__main__":
    PriceEstimation()


