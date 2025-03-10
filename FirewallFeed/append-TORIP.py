#!/usr/bin/env python3
import csv
import logging
import ipaddress

# Configure logging
logging.basicConfig(filename='/var/log/ip_append_service.log', level=logging.INFO, format='%(asctime)s %(message)s')

def is_valid_ip(ip):
    """Check if the given IP is valid."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def read_existing_ips(file_path):
    """Read existing IPs from a CSV file and return a set of valid IPs."""
    existing_ips = set()
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                ip = row[0]
                if is_valid_ip(ip):
                    existing_ips.add(ip)  # Assumes IP is in the first column
    except FileNotFoundError:
        # File does not exist, so no existing IPs
        pass
    return existing_ips

def append_unique_data(source_file, target_file):
    """Append unique and valid IPs from source_file to target_file."""
    existing_ips = read_existing_ips(target_file)

    with open(source_file, 'r') as source, open(target_file, 'a', newline='') as target:
        reader = csv.reader(source)
        writer = csv.writer(target)

        headers_written = False
        for row in reader:
            ip = row[0]  # Assumes IP is in the first column
            if is_valid_ip(ip) and ip not in existing_ips:
                if not headers_written:
                    # Write header if it's the first time
                    writer.writerow(['IP'])  # Adjust header if necessary
                    headers_written = True
                writer.writerow([ip])
                existing_ips.add(ip)

    logging.info("Valid and unique IPs appended successfully!")

if __name__ == "__main__":
    source_file = '/pathtothefile/ip-block.csv'  # Use the correct absolute path
    target_file = '/pathtothefile/ip_tor.csv'    # Use the correct absolute path

    append_unique_data(source_file, target_file)
    logging.info("IP append task completed.")
