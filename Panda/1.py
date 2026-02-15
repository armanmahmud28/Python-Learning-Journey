import pandas as pd

print("                        Learning Panda...")

mydataset = {
    'car': ["BMW", "Volvo", "Ford"],
    'speed': [200, 150, 200]
}

data = pd.DataFrame(mydataset)
print(data)

a = [1, 3, 4]

myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

print(myvar["z"])


mydataset2 = {
    'calori': [300, 200, 100],
    'duration': [30, 20, 10]
}

data2 = pd.DataFrame(mydataset2)
print(data2)
