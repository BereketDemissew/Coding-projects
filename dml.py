import pandas as pd #like excel but python to deal with columned data
import numpy as np  #like arrays/lists but more memory efficient and faster
import random as rand
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


poke = pd.read_csv('pokemon_data.csv')
#print(poke.loc[poke['Name']== "mewtwo"])

hell = rand.randrange(0, 800)

print(poke.loc[hell, 'Name'])



#poke['Heavy hitter'] = poke['Sp. Atk'].apply(lambda x: 'Weak AF' if x<30 else ('ok' if x<120 else 'MAY GOD PROTECT YOU BECAUSE i WONT'))
poke['Stat total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']

#poke['ranking spk atk']= poke['Sp. Atk'].rank(ascending=True)

#print(poke)

#b = np.array([[1.0,2.6,9.3,17.4],[2.9,9.6,3.4,12.7]]) # a more complex float array in 2 dimentions (there is two lists in a list)
#print(b.ndim)

#a = np.array([[1,2,3,4,5,6,7],[4,5,6,7,8,9,10],[4,5,6,7,8,9,10]])
#print(a.ndim)

#print(poke.Overall())

y = poke.Attack # The columns that are inputted into our model (and later used to make predictions) are called "features."



finder = ['HP', 'Generation', 'Defense', 'Stat total']
# ^ - you have to use a varible to hold multiple column names then be able to use houses[] to find them
x = poke[finder]



# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)# x is independent variable and y is the dependent




print("Making predictions for pokemon attack stats:")
print(x)
print("The predictions are")
print(melbourne_model.predict(x))


Lister = melbourne_model.predict(x)
print("____________________________________________________________________________________________________________________________________________________")

print(mean_absolute_error(y, Lister)) # avg predictions are off by

tx, vx, ty, vy = train_test_split(x, y, random_state = 0) # Split arrays or matrices into random train and test subsets
melbourne_model = DecisionTreeRegressor()
 
melbourne_model.fit(tx,ty)

prediction = melbourne_model.predict(vx)
print(mean_absolute_error(vy, prediction))

print("----------------------------------------------------------------------------------------------------------------------------------------------------")

print(poke)



