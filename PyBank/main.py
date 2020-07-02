#Dependencies- Operating System and File Type
import os
import csv
#--------------------------------------------------------------------------------------------
#Define file path for program back to the open folder in Python
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
totalmonths = 0
profit=0
averagechange=0
net_change_list = []
prev_value=0
#--------------------------------------------------------------------------------------------
#Open the file path, initialize the reader and define how data from the file should be parsed
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
#-------------------------------------------------------------------------------------------
#Make the file content readable in the program and for people
    #print results for computer consumption
    print(csvreader)
    #define header row to isolate it from remaining data set
    csv_header = next(csvreader)
    firstrow=next(csvreader)
    totalmonths=totalmonths+1
    profit= profit + float(firstrow[1])
    prev_value= int(firstrow[1])
    
    #print header for human viewing
    print(csv_header)
    #create loop to find details within the data extract
    for row in csvreader:
        #find total number of months being evaluated
        net_change= int(row[1]) -prev_value 
        prev_value= int(row[1])
        net_change_list.append(net_change)
        #net_change_list = net_change_list + [net_change]
        totalmonths=totalmonths+1
        print(f'"Total Months:" {totalmonths}')
        #find total profit for the entire period
        profit= profit + float(row[1]) 
        print(f'"Total profits:"{profit}')
avgdiff= sum(net_change_list)/len(net_change_list)
print(f'"Average Change:"{avgdiff}')
MaxChange=max(net_change_list)
MinChange=min(net_change_list)
print(f'"Greatest increase in profits:"{MaxChange}')
print(f'"Greatest descrease in profits:"{MinChange}')



#-------------------------------------------------------------------------------------------
  #Total Number of Months in the Dataset
  #Net Total of Profit/Losses over the entire period 
  #The greatest increase in profits(date and amount) over entire period 
  #The greatest decrease in losses (date and amount) over the entire period
  #Results should appear as: 
  #Financial Analysis
  #-----------------------------------------------------------------------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #------------------------------------------------------------------------------------------