#MapPlot.py
#Name: Harrison Drake
#Date: 4/19/25
#Assignment: Lab 10

import cars
import pandas
import matplotlib.pyplot as plt

car = cars.get_car()

years = []
mpgs = []

for vehicle in car:
    year = vehicle["Identification"]["Year"]
    mpg = vehicle["Fuel Information"]["Highway mpg"]
    if mpg <= 100:
        years.append(year)
        mpgs.append(mpg)
   # print(year, mpg)

df = pandas.DataFrame([{"Year": years,
                        "mpg": mpgs}])

print(df)
plt.plot(years, mpgs, 'ro')
plt.savefig("output")

""" The graph shows the relationship between the year the car was made and the highways mpg it gets. As you can see the
the data is pretty consistent, maybe goes up a little bit each year but not by very much,
except for one outlier which was at 200 mpg so Im not sure what car gets that but I removed it."""