from pymongo import MongoClient
import csv

def db_get_ip_to_file(ip_column):
    # Establish connection
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient['IPBlockRecommended']  # Database name is IPBlockRecommended
    mycol = mydb['IPBlockRecommended']     # Collection name is also IPBlockRecommended

    # Fetch all documents
    documents = mycol.find()

    # Open CSV file for writing IP addresses
    with open('ip_tor.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)

        # Write header for the CSV file
        csv_writer.writerow([ip_column])

        # Write IP addresses to the CSV
        for document in documents:
            ip = document.get(ip_column, None)
            if ip:  # Only write if the IP exists
                csv_writer.writerow([ip])

if __name__ == "__main__":
    ip_column = 'ip'

    db_get_ip_to_file(ip_column)
