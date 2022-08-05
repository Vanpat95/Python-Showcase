import os
import csv


with open('budget_data.csv', encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first_row = next(csvreader)
    monthcount = 1
    previous_value = int(first_row[1])
    month = first_row[0]
    greatest_increase = 0
    increase_month = ''
    greatest_decrease = 0
    decrease_month = ''
    avgchange = 0
    change = 0
    totalcount = int(first_row[1])
    totalchange = 0
    
    
    
    for row in csvreader:
        monthcount = monthcount + 1
        totalcount = totalcount + int(row[1])
        change = int(row[1]) - previous_value
        totalchange = totalchange + change
        previous_value = int(row[1])
        if (change > greatest_increase):
            greatest_increase = change
            increase_month = row[0]
        if (change < greatest_decrease):
            greatest_decrease = change
            decrease_month = row[0]
    avgchange = (totalchange/monthcount)

            


            

print(f'Financial Analysis')
print(f'______________________________')    
print(f' ')    #for spacing
print(f'Total Months:', monthcount)
print(f'Total: $', totalcount)
print(f'Average Change: $', avgchange)
print(f'Greatest Increase in Profits: ', increase_month, ' ($', greatest_increase, ')')
print(f'Greatest Decrease in Profits: ', decrease_month, ' ($', greatest_decrease, ')') 