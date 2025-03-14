import csv
with open("C:/Users/kelka/OneDrive/Documents/IPL/IPL_2018.csv") as f:
  data = csv.reader(f)
  datalist = list(data)
  for i in datalist:
    if i[0] == ("Virat Kohli"):
      print("The number of runs scored by", i[0], "is equal to", i[4] )
with open ("C:/Users/kelka/OneDrive/Documents/IPL/new.csv", "w") as f:
  write1 = csv.writer(f)
  header = ('Name', 'Country')
  data=(   ('Akash',"dubai"),   ('Shishir','london') , ('Geeta','us') )
  write1.writerow(header)
  for i in data:
    write1.writerow(i)
