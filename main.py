import re

#this pattern is being used to find ip address
ip_pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
#this pattern is being used to find log time - means \[ \] => exact brakets - (.*?) => means non greedy capture of whatever is inside
time_pattern = re.compile(r'\[(.*?)\]')

def log_parser():
    with open('sample_log.txt', 'r') as file:
        for line in file:
            ip_match = ip_pattern.search(line)
            time_match = time_pattern.search(line)
            if ip_match:
                print(f"IP: {ip_match.group()} | Time: {time_match.group(1)}")
                
log_parser()
