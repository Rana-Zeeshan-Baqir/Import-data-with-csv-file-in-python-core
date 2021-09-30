import csv

csv_file = open('lahore_weather_1996_Dec.csv','r')
csv_reader = csv.reader(csv_file)
print(csv_file)
aa = []
max_temp = []
min_temp = []
pkt = []
for i in csv_reader:
    aa.append(i)
    try:
        if i[1]:
            max_temp.append(i[1])
        if i[3]:
            min_temp.append(i[3])
        if i[0]:
            pkt.append(i[0])
    except:
        pass
print(aa)
print(max_temp)
print(max(list(map(int,max_temp[1:]))))
print(min_temp)

min_list = list(map(int,min_temp[1:]))
pkt = pkt[1:]
print(pkt)
print("minimum tempreture ", min(min_list), "and data is ", pkt[min_list.index(min(min_list))])
sum_number = sum(list(map(int,min_temp[1:])))
total_len = len(list(map(int,min_temp[1:])))
average = sum_number/total_len
print(average)
