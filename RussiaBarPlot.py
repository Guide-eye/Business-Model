#Importing pandas to load data from csv files into dataframes and matplotlib for the plotting of the data
import pandas as pd
import matplotlib.pyplot as plt

#Load csv data into a dataframe
top = pd.read_csv("Russian Tourists to Egypt between 2010 and 2017.csv")

#Determine the fonts of the graph title and labels
font1 = {"family": "serif", "color": "goldenrod", "size": 20}
font2 = {"family": "serif", "color": "goldenrod", "size": 15}

#Plot the graph and spcify the title and labels
plt.bar(top.Year, top.Number, color="goldenrod", width=0.5)
plt.title("Russian Tourists to Egypt between 2010 and 2017", fontdict=font1)
plt.xlabel("Year", fontdict=font2)
plt.ylabel("Number of Tourists in milions", fontdict=font2)

plt.show()
