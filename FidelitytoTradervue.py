import csv
from datetime import datetime
import pandas as pd

with open('test.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
  
        next(csv_reader)  #read header
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)
  
  
        with open('Input_test.csv','w',newline='') as new_file:
            csv_writer = csv.writer(new_file)
            writer = csv.DictWriter(new_file, fieldnames=["Symbol", "Price", "Quantity", "Time", "Date"])
            writer.writeheader()
            # csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            for line in csv_reader: 
                        # print(line[1])
                        # n = (line[1].find('$')) + 1 = 11
                        s = line[0]
                        symbol = s
                        p = line[1]
                        price = (p[11:])
                        q = line[2]
                        #   q1 = line[6]
                        #   print(q1.isdigit())
                        #   print(-abs(int(q1)))
                        
                        if (q[0] == 'B'):   #B for Buy and S for Sell which negative -1
                            quantity = line[6]
                        else:
                            quantity = -abs(int(line[6]))
                            #   quantity = (q1)*(-1)
                            #   quantity = -abs(line[6])
                        t = line[3]
                        time = (t[0:11])
                        # csv_writer = csv.writer(new_file)
                        # csv_writer.writerow(val)
                        print(time)
                        # csv_writer = csv.DictWriter(new_file, fieldnames=val, delimiter='\t')
                        # csv_writer = csv_writer(new_file, delimiter=val)
                        
                      #Create datetime object from string
                        in_time = datetime.strptime(time, "%I:%M:%S %p")
                        #convert to 24 hour format
                        out_time = datetime.strftime(in_time, "%H:%M:%S")
                      
                        csv_writer.writerow([symbol, price, quantity, out_time, datetime.today().date()]) 
                    #   csv_writer.writerow(["apple", "banana", "mango", "orange"]) 

                      
                      # for item in val:
                      #   csv_writer.writerow([item])            
# with open("Input_test.csv", "rb") as infile, open("Ouput_test.csv", "wb") as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#     for row in reader:
#         writer.writerow(item.replace("","", "") for item in row)
                        #add header
                       
                        # f.close()