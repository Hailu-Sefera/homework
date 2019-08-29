import os
import csv
filepath = os.path.join("Resources","budget_data.csv")
with open(filepath) as csv_file:
   csv_data = csv.reader(csv_file)
   next(csv_data)
   count = 0
   sum = 0
   net_change = []
   months = []
   previous_row=0
   current_row=0
   sum_change=0
   for row in csv_data:
       count = count + 1
       sum = int(row[1])+sum
       current_row=int(row[1])
    #    print (row[0])
       months.append (row[0])
       (current_row-previous_row)
       net_change.append(current_row-previous_row)
       previous_row=current_row
   net_change = net_change[1:]
   months = months[1:]
#    print (months)
   sum1 = 0
   greatest_current_loss=0
   greatest_current_gain=0
   greatest_increase_month = ""
   greatest_decrease_month = ""
   for x, month in zip(net_change, months):
       sum1 += x
       if x < 0:
           if x < greatest_current_loss:
               greatest_current_loss = x
               greatest_decrease_month = month
               
       if x > 0:
           if x > greatest_current_gain:
               greatest_current_gain = x
               greatest_increase_month = month
       # print(greatest_current_loss)
   print('Financial Analysis')
print('----------------------------')
with open("PyBank text Result.txt", "a") as myfile:
   myfile.write("Financial Analysis\n")
with open("PyBank text Result.txt", "a") as myfile:
   myfile.write("---------------------\n")
#Net Total Profit
print("Net Total Profit: $",sum)
with open("PyBank text Result.txt", "a") as myfile:
   text = "Net Total Profit: $" + str(sum) + "\n"
   myfile.write(text)
#Total number of months
print("Total number of months: ",count)
with open("PyBank text Result.txt", "a") as myfile: 
   text = "Total number of months: $" + str(count) + "\n"
   myfile.write(text)

print("Average Change: $",sum1/len(net_change))
with open("PyBank text Result.txt", "a") as myfile:
   text = "Average Change: $" + str(sum1/len(net_change)) + "\n"
   myfile.write(text)
print ("Greatest Increase in Profits:", (greatest_increase_month) ,"$", (greatest_current_gain))
with open("PyBank text Result.txt", "a") as myfile:
   text = "Greatest Increase in Profits:"  + str((greatest_increase_month)) +   "$"   + str((greatest_current_gain)) + "\n"
   myfile.write(text)
print ("Greatest Decrease in Profits:", (greatest_decrease_month) ,"$", (greatest_current_loss))
with open("PyBank text Result.txt", "a") as myfile:
   text = "Greatest Decerese in Profits:" + str((greatest_decrease_month)) +   "$"   + str((greatest_current_loss)) + "\n"
   myfile.write(text)
