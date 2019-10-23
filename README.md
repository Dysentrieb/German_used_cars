# German_used_cars

### Overview:
In this notebook, a deeper look on the german used car market is applied, using the "Used cars database" from Kaggle, supplied by Orges Leka in 2016. The dataset contains over 370.000 used car adds from ebay-kleinanzeigen. For the analysis and modelling, the Cross Industry Standard Process for Data Mining (CRISP-DM) is applied. The dataset is available here: https://www.kaggle.com/orgesleka/used-cars-database

### Motication:
Germany is a car-nation. Not only it is home to several of the worlds largest car manufacturers, like BMW, Mercedes-Benz and VW, there is also a huge number of car owners. According to the Kraftfahrt-Bundesamt, the german authority responsible for cars, in the beginning of 2019 64,8 million cars and trailers with an average age of 9.5 years were registered (https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/bestand_node.html). A huge market like this also has a big market for used cars. In the following, this market is being analyzed and several questions shall be answered:

### Research Questions:
1. What are the most common vehicle types?
2. Which brands are predominant on the german used cars market?
3. What is the average age of cars on the german used cars market?
4. Are there local differences? How are the offers distributed over Germany?
5. Concerning motorization: Which fuel-systems are preferred? What is the average motor-power?
6. What is the distribution of sale prizes?
7. What is a common mileage for used cars?
8. Can a car value be predicted by using features from the add?

### Programming Language and Required libraries:
Everything was coded in Python 3. To run the notebook, you will need the following libraries:
- numpy
- pandas
- matplotlib.pyplot as plt
- scipy
- pickle
- sklearn
- xgboost

To run the command line app, you will need the following libraries:
- numpy
- pandas
- pickle
- sklearn
- xgboost

### Instructions:
- Run the Jupyter Notebook by starting German_used_Cars.ipynb
- Run the command line app by executing main.py

### Description of files
- images # images used in the Medium-Post
- autos.csv # German used cars dataset, downloaded from https://www.kaggle.com/orgesleka/used-cars-database
- df_cols.pkl # DataFrame columns to be used in the command line app
- German_used_Cars.ipynb # Jupyter Notebook, used to conduct the analysis and create the model
- German_used_Cars.html # html-export of the Jupyter Notebook
- gs_best_reg.pkl # Best regressor model from GridSearchCV - used in Command line app
- gs_object.pkl # GridSearchCV object
- LICENSE # License file
- main.py # Programm file for the command line app
- PLZ.tab # Input file with information about german Zip-Codes, downloaded from http://opengeodb.org/wiki/PLZ.tab
- README.md # This file
- regressor.pkl # Untuned regressor model
- used_cars.py # Command line app code file
- zips.pkl # Contains DataFrame with german Zip-Code-data to be used in the command line app

### Links and Contact:
- Github-Repository: https://github.com/Dysentrieb/German_used_cars
- Medium-Post: https://medium.com/@danieldysentrieb/do-you-get-ripped-of-when-buying-a-car-in-munich-2d9cd764b344
- Command line Web-App: https://repl.it/@Dysentrieb/Germanusedcars

© 2019 by Daniel Weich
