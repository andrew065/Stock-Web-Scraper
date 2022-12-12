import csv
import os


def avg_industry(ind):
    directory = f"Company Stock Data/{ind}"

    for filename in os.listdir(directory):
        if filename == ".DS_Store":
            return
        file = os.path.join(directory, filename)

        industry_stock = {}
        print(file)
        with open(file, newline='') as file:
            for i in range(14):
                file.readline()
            reader = csv.DictReader(file)
            for row in reader:
                date = row['date']
                found = False
                if len(industry_stock) == 0:
                    industry_stock[date] = float(row['close'])
                for k in industry_stock.keys():
                    if k == date:
                        value = industry_stock[date]
                        industry_stock.update({date: float((value + float(row['close'])) / 2)})
                        found = True
                        break
                if not found:
                    industry_stock[date] = float(row['close'])

        all_industries[ind] = industry_stock


count = 0
all_industries = {}
industries = [folder for folder in os.listdir('Company Stock Data')]
industries.remove('.DS_Store')
print(industries)

for industry in industries:
    avg_industry(industry)

for industry in all_industries:
    with open(f'{industry}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Price', '% Growth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Date': 'Date', 'Price': 'Price', '% Growth': '% Growth'})

        current_ind = all_industries[industry]

        initial_price = list(current_ind.values())[0]

        for key in all_industries[industry]:
            price = current_ind[key]
            writer.writerow({'Date': key, 'Price': price, '% Growth': float((price - initial_price)/initial_price)})

        csvfile.close()
        count += 1

print(count)
