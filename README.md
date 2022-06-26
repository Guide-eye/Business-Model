### Description

A Python program to visualize data from CSV files to bar plots and pie charts.

### Dependencies

* `python 3.10.4`
* `matplotlib==3.5.2`
* `pandas==1.4.3`

### Installation & Running

1. `pip3 -r  requriments.txt`

```python 
import pandas as pd
import matplotlib.pyplot as plt

top17 = pd.read_csv("Top 10 Nationalities to Egypt in 2017.csv")
top19 = pd.read_csv("Top 10 Nationalities to Egypt in 2019.csv")
```

2. You have to modify `6th` and `7th` in `BarPlots.py` and `PieCharts.py` to your CSV files names which you need to visualize thier data.
  -  #### NOTE : CSV files must be exist along with the program in the same directory

3. Run the python program to pop up the graphs with an option to save them.

### Samples Output

* for testing purposes you can download the CSV files from here:<br>
  1. [Top 10 Nationalities to Egypt in 2017](https://www.kaggle.com/datasets/marcatef/top-10-nationalities-to-egypt-in-2017)
  2. [Top 10 Nationalities to Egypt in 2019](https://www.kaggle.com/datasets/marcatef/top-10-nationalities-to-egypt-in-2019)
  3. [Russian Tourists to Egypt between 2010 and 2017](https://www.kaggle.com/datasets/marcatef/russian-tourists-to-egypt-between-2010-and-2017)

* After Running the program:<br>
  1. <img src="https://github.com/Guide-eye/Business-Model/blob/main/Output-Samples/BarPlots.png" style="height: 600px; width:1000px;"/>
  2. <img src="https://github.com/Guide-eye/Business-Model/blob/main/Output-Samples/PieCharts.png" style="height: 600px; width:1000px;"/>
  3. <img src="https://github.com/Guide-eye/Business-Model/blob/main/Output-Samples/RussiaBarPlot.png" style="height: 600px; width:1000px;"/>
