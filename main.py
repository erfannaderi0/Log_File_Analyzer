import re

# Compile the regex pattern once
pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')

def ip_finder():
    with open('sample_log.txt', 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                print("IP Address:", match.group())

ip_finder()
