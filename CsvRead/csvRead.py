import csv

iFile = open('Z:/GitProjects/Python Scripts/CsvRead/gameDevCompanies.csv')
reader = csv.reader(iFile)


aFile = open('results.abc', 'w')
results = "" 
name = ""
email = ""


rownum = 0
for row in reader: 
   #save header row
   if rownum == 0:
      header = row
   else:
      colnum = 0
      for col in row:
      	if colnum == 0:
      	   name = col
      	else:
      	   email = col
        results += col
        colnum = colnum + 1
   print (name + ' ' + email)
   aFile.write(results + '\n')
   results = ''
   rownum += 1

aFile.close()