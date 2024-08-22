import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define the regex pattern for a valid IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Check if the input matches the general IPv4 format
    if not re.match(pattern, ip):
        return False

    # Split the IP into its components and check each part
    parts = ip.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()
