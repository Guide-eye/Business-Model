#Importing pandas to load data from csv files into dataframes and matplotlib for the plotting of the data
import pandas as pd
import matplotlib.pyplot as plt

#Load csv data into dataframes
top17 = pd.read_csv("Top 10 Nationalities to Egypt in 2017.csv")
top19 = pd.read_csv("Top 10 Nationalities to Egypt in 2019.csv")

#Determine the fonts of the graph title and labels
font1 = {"family": "serif", "color": "darkred", "size": 20}
font3 = {"family": "serif", "color": "darkblue", "size": 20}

#Convert the percentage column from string to float data type
Plabels17 = top17["Percentage"]
top17["Percentage"] = top17["Percentage"].str.rstrip("%").astype("float") / 100.0

#Putting The pie chart in the left of the page
plt.subplot(1, 2, 1)
plt.pie(top17.Percentage, labels = Plabels17)

#Spcify the chart title and legend
plt.legend(title = "Countries", labels=top17.Nationality)
plt.title("Top 10 Nationalities to Egypt in 2017", fontdict=font1)

#Convert the percentage column from string to float data type
Plabels19 = top19["Percentage"]
top19["Percentage"] = top19["Percentage"].str.rstrip("%").astype("float") / 100.0

#Putting The pie chart in the right of the page
plt.subplot(1, 2, 2)
plt.pie(top19.Percentage, labels = Plabels19)

#Spcify the chart title and legend
plt.legend(title = "Countries", labels=top19.Nationality, loc="lower right")
plt.title("Top 10 Nationalities to Egypt in 2019", fontdict=font3)

plt.show()