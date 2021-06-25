import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics as st 
import random
import pandas as pd 
import csv 


df= pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

pop_mean=st.mean(data)
print(pop_mean)
pop_std_dev= st.stdev(data)
print(pop_std_dev)

mean_dataset=[]
for i in range(0,1000):
    dataset=[]
    for i in range(0,100):
        random_index=random.randint(0,9999)
        value=data[random_index]
        dataset.append(value)
    mean_data=st.mean(dataset)
    mean_dataset.append(mean_data)


sample_mean= st.mean(mean_dataset)
print(sample_mean)
sample_std=st.stdev(mean_dataset)
print(sample_std)


first_std_dev_start,first_std_dev_end= sample_mean-sample_std,sample_mean+sample_std
second_std_dev_start,second_std_dev_end= sample_mean-(2*sample_std),sample_mean+(2*sample_std)
third_std_dev_start,third_std_dev_end= sample_mean-(3*sample_std),sample_mean+(3*sample_std)

print("std1",first_std_dev_start,first_std_dev_end)
print("std2",second_std_dev_start,second_std_dev_end)
print("std3",third_std_dev_start,third_std_dev_end)

data1= pd.read_csv("data2.csv")
datalist1= data1["Math_score"].tolist()
mean_datalist1=st.mean(datalist1)


data2= pd.read_csv("data2.csv")
datalist2= data2["Math_score"].tolist()
mean_datalist2=st.mean(datalist2)


data3= pd.read_csv("data3.csv")
datalist3= data3["Math_score"].tolist()
mean_datalist3=st.mean(datalist3)



fig= ff.create_distplot([mean_dataset],["Math Scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_datalist3,mean_datalist3],y=[0,0.2],mode="lines",name="MEAN3"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.2],mode="lines",name="STD DEV 1 START"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.2],mode="lines",name="STD DEV 1 END"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.2],mode="lines",name="STD DEV 2 START"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.2],mode="lines",name="STD DEV 2 END"))
fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.2],mode="lines",name="STD DEV 3 START"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.2],mode="lines",name="STD DEV 3 END"))

fig.show()