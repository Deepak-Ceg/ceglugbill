import csv
write=csv.DictWriter(open('eggs.csv','a'),fieldnames=['marconi','einstein'])
write.writeheader()
write.writerow({'marconi':'i','einstein':'cibi'})

