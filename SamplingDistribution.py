import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import csv 
import pandas as pd

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
figure=ff.create_distplot([df["temp"].tolist()],["temp"],show_hist=False)
figure.show()
temp_mean=statistics.mean(data)
temp_sd=statistics.stdev(data)

print("temp_mean.",temp_mean)
print("standard_deviation",temp_sd)


#function to find mean or data sample
def randomdata_mean(countervalue):
    dataset=[]
    for i in range(0,countervalue):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

#function to draw graph
def showfigure(meanlist):
    df=meanlist
    figure=ff.create_distplot([df],["temp"],show_hist=False)
    figure.show()
# Pass the number of time you want the mean of the data points as a parameter in range function in for loop 
def setup(): 
    mean_list = [] 
    for i in range(0,1000): 
        set_of_means= randomdata_mean(100)
        mean_list.append(set_of_means) 
    showfigure(mean_list)
    mean = statistics.mean(mean_list) 
    print("Mean of sampling distribution :-",mean )

setup()