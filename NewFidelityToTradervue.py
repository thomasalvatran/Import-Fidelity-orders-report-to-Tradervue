import csv
from datetime import datetime
import pandas as pd

with open("test.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # read header
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)

    with open("Input_test.csv", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file)
        writer = csv.DictWriter(
            new_file, fieldnames=["Symbol", "Price", "Quantity", "Time", "Date"]
        )
        writer.writeheader()
        # csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        for line in csv_reader:
            # print(line[1])
            # n = (line[1].find('$')) + 1 = 11
            s = line[0]  # array of columns
            symbol = s

            p = line[1]

            price = p[11:]
            q = line[2]
            #   q1 = line[6]
            #   print(q1.isdigit())
            #   print(-abs(int(q1)))
            # print(q[0:3])
            quant = line[6].strip()  # strip spce in this column remaining only numbers
            if quant:
              quant = int(line[6])   # convert str to int
            else:                         # empty string prevent ValueError: invalid literal for int() with base 10: ''
              quant = 0                   # ref https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
              
            if q[0:3] == "Buy":  # q[0] == "B"
                quantity = quant
            else:
                # quantity = -abs(quant)
                #   quantity = (q1)*(-1)
                quantity = -abs(int(quant))
            t = line[3]
            timing = t[0:11]
            # csv_writer = csv.writer(new_file)
            # csv_writer.writerow(val)
            print(timing)
            # csv_writer = csv.DictWriter(new_file, fieldnames=val, delimiter='\t')
            # csv_writer = csv_writer(new_file, delimiter=val)

            # Create datetime object from string
            in_time = datetime.strptime(timing, "%I:%M:%S %p")  
            #https://stackoverflow.com/questions/55402670/converting-time-format-with-strftime-and-strptime
            # convert to 24 hour format
            out_time = datetime.strftime(in_time, "%H:%M:%S")

            csv_writer.writerow(
                [symbol, price, quantity, out_time, datetime.today().date()]
            )  # Columns in new csv file
        #   csv_writer.writerow(["apple", "banana", "mango", "orange"])

        # for item in val:
        #   csv_writer.writerow([item])
# with open("Input_test.csv", "rb") as infile, open("Ouput_test.csv", "wb") as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#     for row in reader:
#         writer.writerow(item.replace("","", "") for item in row)
# add header

# f.close()
