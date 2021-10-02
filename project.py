import csv
import math

with open("project.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

def mean(data) :
    n = len(data)
    total = 0
    for x in data :
        total = total + int(x)
    mean = total/n 
    return mean

data=[]
for marks in file_data :
    data.append(float(marks[0]))

#print(data)

squared_list = []
for number in data :
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)

#getting sum
sum =0
for i in squared_list:
 sum =sum + i


result = sum/ (len(data)-1)
std_deviation=math.sqrt(result)
print(std_deviation)
