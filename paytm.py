#import panda for operation on the csv file using dataframe
import pandas as pd
#import matplotlib to plot the chart for visualization
import matplotlib.pyplot as plt


#read the CSV file
df=pd.read_csv("/home/imsaiful/Desktop/mypaytm.csv")


#fill all the nan value to zero
df.fillna({'Debit':0,'Credit':0},inplace=True)

#fetach all the cashback.
#Note:chack in your csv file. In some CSV it is Bonus Added in place of Cashback Received
df_check_cashback=df[['Date','Credit']][df['Activity']=='Cashback Received']

#convert date coloumn to date time value. It will help in sorting , sum and group by operation
df_check_cashback['Date']=pd.to_datetime(df_check_cashback['Date'])

#add all the cashback according to month
df_cashback=df_check_cashback.groupby(df_check_cashback['Date'].dt.strftime('%B'))['Credit'].sum()

#save the cashback file. Change path according to your computer.
df_cashback.to_csv("/home/imsaiful/Desktop/paytmcashback.csv")


#convert main dataframe date coloumn to date time value. It will help in sorting , sum and group by operation
df['Date']=pd.to_datetime(df['Date'])

#group the debit and credit of month 
summary_by_month=df.groupby(df['Date'].dt.strftime('%B'))['Debit','Credit'].sum()

#save the file.check path accoring to your system
summary_by_month.to_csv("/home/imsaiful/Desktop/paytm_summary.csv")

#read the summary file
df_paytm_summary=pd.read_csv("/home/imsaiful/Desktop/paytm_summary.csv")

#read tthe cashback file
df_cashback=pd.read_csv("/home/imsaiful/Desktop/paytmcashback.csv",header=None,names=["Month","Cashback"])


print("***Welcome to the magic of python***")
#prinf the summary file
print("\nYour's paytm summary\n\n",df_paytm_summary)

#print the cashback file
print("\nYour's total cashback\n\n",df_cashback)


print("\nFull summary\n")
#print total debit in a year for my case according to csv file
print("\nTotal Debit ",df['Debit'].sum()," Rs.")
#print total credit in a year for my case according to csv file
print("\nTotal Credit" ,df['Credit'].sum()," Rs.")
#print total cashback in a year for my case according to csv file
print("\nTotal Cashback",df_cashback['Cashback'].sum()," Rs.")
#print total cashabck percentage against debit in a year for my case according to csv file
print("\nTotal Cashback Percentage",df_cashback['Cashback'].sum()/(df['Debit'].sum())*100," %")

print("\nNow plot figure to visualize data\n")

#create the plot
plt.figure(figsize=(12,12))

#take all 12 month debit values
y1=df_paytm_summary['Debit']

#take all 12 month credit values
y2=df_paytm_summary['Credit']

#take all 12 month on x axis
x=df_paytm_summary['Date']
xc=df_cashback['Month']

#take all 12 month cashback values
yc=df_cashback['Cashback']


plt.title('Paytm')


#label x axis as month
plt.xlabel("Date")

#label y axis as debit/credit
plt.ylabel("Debit/Credit")

#plot the chart of the credit/debit against month
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(xc,yc)

#check top right corner on graph and will indicate color of the line
plt.legend(['Debit','Credit','Cashback','mean'],loc=1)
plt.savefig('/home/imsaiful/Desktop/paytmfig.pdf', format='pdf')
