import re

#this pattern is being used to find ip address
ip_pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
#this pattern is being used to find log time - means \[ \] => exact brakets - (.*?) => means non greedy capture of whatever is inside
time_pattern = re.compile(r'\[(.*?)\]')
#extract HTTP method an request path
method_request_pattern = re.compile(r'"([A-Z]+)\s([^ ]+)')

def log_parser():
    with open('sample_log.txt', 'r') as file:
        for line in file:
            ip_match = ip_pattern.search(line)
            time_match = time_pattern.search(line)
            m_r = method_request_pattern.search(line)
            if ip_match:
                print(f"IP: {ip_match.group()} | Time: {time_match.group(1)} | method: {m_r.group(1)} request: {m_r.group(2)}")
                
log_parser()
