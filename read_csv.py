import csv

def readcsv():
    data = []
    with open('hospitals.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            name = row[0]
            address = row[1]
            specialization = row[2].split(",")
            contact = row[3]
            
            data.append({
                "name": name,
                "address": address,
                "specialization": specialization,
                "contact": contact,
            })
    return data
