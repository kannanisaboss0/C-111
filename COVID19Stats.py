#--------------------------------------------------------COVID19DataIndia.py--------------------------------------------------------#
'''
Importing modules:
-statistics (st)
-plotly.graph_objects (go)
-plotly.figure_factory (ff)
-plotly.express (px)
-pandas (pd)
-random (rd)
-time (tm)
'''
import statistics as st 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import random as rd
import time as tm

#Defining a function to calculate all teh standard deviations, mean and median values
def CalculateStandardDeviations(list_arg,label_arg,choice_arg,state_choice_arg):

  mean_param=st.mean(list_arg)
  st_dev_param=st.stdev(list_arg)
  median_param=st.median(list_arg)

  print("Calculating data...")
  tm.sleep(2.4)

  st_dev_1_start,st_dev_1_end=mean_param-(1*st_dev_param),mean_param+(1*st_dev_param)
  st_dev_2_start,st_dev_2_end=mean_param-(2*st_dev_param),mean_param+(2*st_dev_param)
  st_dev_3_start,st_dev_3_end=mean_param-(3*st_dev_param),mean_param+(3*st_dev_param)

  GenerateGraphFromData(list_arg,label_arg,mean_param,"Mean Value",st_dev_1_start,st_dev_1_end,st_dev_2_start,st_dev_2_end,st_dev_3_start,st_dev_3_end,st_dev_param,median_param,choice_arg,state_choice_arg)

#Defining a function to create a graph from stipulated data
def GenerateGraphFromData(list_arg,label_arg,mean_arg,label_mean_arg,st_dev_arg_1,st_dev_arg_2,st_dev_arg_3,st_dev_arg_4,st_dev_arg_5,st_dev_arg_6,st_dev_arg,median_arg,choice_arg,state_choice_arg):
  
  plot_param=ff.create_distplot([list_arg],[state_choice_arg+":"+choice_arg+"("+label_arg+")"],show_hist=False,curve_type='normal')

  plot_param.add_trace(go.Scatter(x=[mean_arg,mean_arg],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name=label_mean_arg))

  plot_param.add_trace(go.Scatter(x=[st_dev_arg_1,st_dev_arg_1],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 1"))
  plot_param.add_trace(go.Scatter(x=[st_dev_arg_2,st_dev_arg_2],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 1"))
  plot_param.add_trace(go.Scatter(x=[st_dev_arg_3,st_dev_arg_3],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 2"))
  plot_param.add_trace(go.Scatter(x=[st_dev_arg_4,st_dev_arg_4],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 2"))
  plot_param.add_trace(go.Scatter(x=[st_dev_arg_5,st_dev_arg_5],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 3"))
  plot_param.add_trace(go.Scatter(x=[st_dev_arg_6,st_dev_arg_6],y=[0,(max(plot_param['data'][0]["y"])*1.3)],mode="lines",name="Standard Deviation 3"))

  plot_param.update_yaxes(range=[0,(max(plot_param['data'][0]["y"])*1.3)])

  plot_param.update_layout(title=state_choice_arg+":"+choice_arg+"("+label_arg+")")

  print("Generating data...")
  tm.sleep(2.4)

  plot_param.show()

  percentage_1=[value_1 for value_1 in list_arg if st_dev_arg_1<value_1<st_dev_arg_2]
  percentage_2=[value_2 for value_2 in list_arg if st_dev_arg_3<value_2<st_dev_arg_4]
  percentage_3=[value_3 for value_3 in list_arg if st_dev_arg_5<value_3<st_dev_arg_6]

  print("{}% of data lies between the values {} and {}".format(round((len(percentage_1)*100)/len(list_arg),2),round(st_dev_arg_1),round(st_dev_arg_2)))
  print("{}% of data lies between the values {} and {}".format(round((len(percentage_2)*100)/len(list_arg),2),round(st_dev_arg_3),round(st_dev_arg_4)))
  print("{}% of data lies between the values {} and {}".format(round((len(percentage_3)*100)/len(list_arg),2),round(st_dev_arg_5),round(st_dev_arg_6)))

  print("The mean of the data is:{}".format(round(mean_arg,2)))
  print("The standard deviation of the data is:{}".format(round(st_dev_arg,2)))
  print("The median of the data is:{}".format(round(median_arg,2)))

#Defining a function to find the Z-Sample value
def FindZ_Sample(list_arg,sample_list_arg):

  original_mean,sample_mean,sample_st_dev=st.mean(list_arg),st.mean(sample_list_arg),st.stdev(sample_list_arg)

  Z_sample=(original_mean-sample_mean)/sample_st_dev

  return print("The Z-sample of the data is:{}".format(round(Z_sample,2))),print("Thank You for using COVID19DataIndia.py")
  

#Reading data from the database
df=pd.read_csv("data.csv")

#Creating a line graph to show the vacccinations conducted in India
India_loc=df.loc[df["State"]=="India"]
line_graph=px.line(India_loc,x="Updated On",y="Total Doses Administered",color="State",title="India:COIVD-19 Vaccinations (16/01/2021 to 09/05/2021)")
line_graph.show()

#Introductory statement and  user input
print("Welcome to COIVD19DataIndia.py. We provide statistical insights about vaccinations on several places in India.")
print("Loading data...")
tm.sleep(2.4)
state_choice=input("Please enter the name of the state/country(India) whose data should be displayed(Exapmle:West Bengal):")
df_state=df.loc[df["State"]==state_choice]

#Verifying the valididty of the abstracted data
#Case-1
if(len(df_state)==0):

  print("There is no state called {} in India.".format(state_choice))
  print("Thank You for using COVID19DataIndia.py")
#Case-2
else:

  choice_list=["Unusable_Element","Total Doses Administered","Total Covaxin Administered","Total CoviShield Administered","Males Vaccinated","Females Vaccinated","Total Individuals Vaccinated","Total Sessions Conducted","Total Sites Present"]
  choice_index=0

  for choice in choice_list[1:]:

    choice_index+=1
    print(str(choice_index)+":"+choice)

  user_input=int(input("Please enter the index of the statistical cosntituent desired to statistically analyse:"))

  choice=choice_list[user_input]

  comparitive_choice=input("Should the data be lower or greater than the specified value:(:-Lower or Greater)")

  #Analysing the user's input
  #Case-1
  if(comparitive_choice=="Lower"):

    value=int(input("Please the number the data should be lesser than:"))
    df_loc=df_state.loc[df_state[choice]<=int(value)]
    df_list=df_loc[choice].tolist()

    #Verfying the validity of the abstracted data
    #Case-1
    if(len(df_list)<=1):

      print("Request Terminated")
      print("No Values Match The Specified Condition ")
    #Case-2
    else:

        #Calling the function to anaylse the data
        CalculateStandardDeviations(df_list,"Original Data",choice,state_choice)

        final_list=[]

        for loop in range(1000):

          mean_list=[]

          for value in range(100):

            random_index=rd.randint(0,(len(df_list)-1))

            df_value=df_list[random_index]

            mean_list.append(df_value)
          mean_list_mean=st.mean(mean_list)
          final_list.append(mean_list_mean)

        #Calling the functions to anaylse the data and find the Z-Sample
        CalculateStandardDeviations(final_list,"Sample Data",choice,state_choice)
        FindZ_Sample(df_list,final_list)

  #Case-2
  elif(comparitive_choice=="Greater"):


    value=int(input("Please enter the number the data should be greater than:"))

    df_loc=df_state.loc[df_state[choice]>=int(value)]
    df_list=df_loc[choice].tolist()

    #Verfying the validity of the abstracted data
    #Case-1
    if(len(df_list)<=1):

      print("Request Terminated")
      print("No Values Match The Specified Condition ")

    #Case-2
    else:

      CalculateStandardDeviations(df_list,"Original Data",choice,state_choice)

      final_list=[]

      for loop in range(1000):

        mean_list=[]

        for value in range(100):

          random_index=rd.randint(0,(len(df_list)-1))

          df_value=df_list[random_index]

          mean_list.append(df_value)
        mean_list_mean=st.mean(mean_list)
        final_list.append(mean_list_mean)

      #Calling the functions to anaylse the data and find the Z-Sample  
      CalculateStandardDeviations(final_list,"Sample Data",choice,state_choice)
      FindZ_Sample(df_list,final_list)

  #Case-3
  else:

    print("Request Terminated.")
    print("Invalid Input")
    print("Thank You for using COVID19DataIndia.py")
#--------------------------------------------------------COVID19DataIndia.py--------------------------------------------------------#








