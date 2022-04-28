import pandas as pd
import numpy as np

agesArray = []
count = 0

data = pd.read_pickle('/home/alan/Escritorio/api-flask/data/AgesAndHeights.pkl')

data.hist()
# print(data)

ages = data['Age']
heights = data['Height']

ages_np = ages.to_numpy()
heights_np = heights.to_numpy()

# print(ages_np)

def returnAges():
    for x in ages_np:
        if x>0:
            agesArray.append(x)            
    
    np.sort(agesArray)
    return agesArray