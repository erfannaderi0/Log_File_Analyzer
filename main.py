import re

#this pattern is being used to find ip address
ip_pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
#this pattern is being used to find log time - means \[ \] => exact brakets - (.*?) => means non greedy capture of whatever is inside
time_pattern = re.compile(r'\[(.*?)\]')
#extract HTTP method an request path
method_request_pattern = re.compile(r'"([A-Z]+)\s([^ ]+)')
#http status code
status_pattern = re.compile(r'"\s(\d{3})\s')

def log_parser():
    with open('sample_log.txt', 'r') as file:
        for line in file:
            ip_match = ip_pattern.search(line)
            time_match = time_pattern.search(line)
            m_r_match = method_request_pattern.search(line)
            status_match = status_pattern.search(line)
            if ip_match and time_match and m_r_match and status_match:
                print(f"IP: {ip_match.group()} | Time: {time_match.group(1)} | method: {m_r_match.group(1)} request: {m_r_match.group(2)} | http status code : {status_match.group(1)}")
                
log_parser()
