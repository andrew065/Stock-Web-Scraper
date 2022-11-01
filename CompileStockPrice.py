import csv
import os

all_industries = {}
industries = [folder for folder in os.listdir('Company Stock Data')]
industries.remove('.DS_Store')
print(industries)

for industry in industries:
    directory = f"Company Stock Data/{industry}"

    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)

        industry_stock = {}
        with open(file, newline='') as csvfile:
            for i in range(14):
                csvfile.readline()
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = row['date']
                if date in industry_stock.keys():
                    value = industry_stock[date]
                    industry_stock[date] = float((value + row['close'])/2)
                else:
                    industry_stock[date] = row['close']

        all_industries[industry] = industry_stock

for industry in all_industries:
    with open(f'{industry}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for key in all_industries[industry]:
            writer.writerow({'Date': key, 'Price': all_industries[industry][key]})

        csvfile.close()
