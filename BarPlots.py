#Importing pandas to load data from csv files into dataframes and matplotlib for the plotting of the data
import pandas as pd
import matplotlib.pyplot as plt

#Load csv data into dataframes
top17 = pd.read_csv("Top 10 Nationalities to Egypt in 2017.csv")
top19 = pd.read_csv("Top 10 Nationalities to Egypt in 2019.csv")

#Determine the fonts of the graph title and labels
font1 = {"family": "serif", "color": "darkred", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
font3 = {"family": "serif", "color": "darkblue", "size": 20}
font4 = {"family": "serif", "color": "darkblue", "size": 15}

#Making The bar plot in the first row of the page
plt.subplot(2, 1, 1)
plt.bar(top17.Nationality, top17.Number, color="darkred", width=0.5)

#Spcify the graph title and labels
plt.title("Top 10 Nationalities to Egypt in 2017", fontdict=font1)
plt.xlabel("Country", fontdict=font2)
plt.ylabel("Number of Tourists", fontdict=font2)

#Making The bar plot in the second row of the page
plt.subplot(2, 1, 2)
plt.bar(top19.Nationality, top19.Number, color="darkblue", width=0.5)

#Spcify the graph title and labels
plt.title("Top 10 Nationalities to Egypt in 2019", fontdict=font3)
plt.xlabel("Country", fontdict=font4)
plt.ylabel("Number of Tourists", fontdict=font4)

plt.show()