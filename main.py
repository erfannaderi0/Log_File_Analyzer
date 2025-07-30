import re
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
import pandas as pd
from datetime import datetime

#this pattern is being used to find ip address
ip_pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
#this pattern is being used to find log time - means \[ \] => exact brakets - (.*?) => means non greedy capture of whatever is inside
time_pattern = re.compile(r'\[(.*?)\]')
#extract HTTP method an request path
method_request_pattern = re.compile(r'"([A-Z]+)\s([^ ]+)')
#http status code
status_pattern = re.compile(r'"\s(\d{3})\s')
#user agent(browser and ...)
user_agent_pattern = re.compile(r'"([^"]+)"$')

def log_parser():
    from collections import Counter

    total_requests = 0
    unique_ips = set()
    page_counter = Counter()
    status_counter = Counter()
    browser_counter = Counter()

    with open('sample_log.txt', 'r') as file:
        for line in file:
            ip_match = ip_pattern.search(line)
            time_match = time_pattern.search(line)
            m_r_match = method_request_pattern.search(line)
            status_match = status_pattern.search(line)
            user_agent_match = user_agent_pattern.search(line)
            if ip_match and time_match and m_r_match and status_match and user_agent_match:
                total_requests += 1
                unique_ips.add(ip_match.group())
                page_counter[m_r_match.group(2).rstrip('/')] += 1
                status_counter[status_match.group(1)] += 1

                # Very simple browser extraction:
                user_agent = user_agent_match.group(1).lower()
                if "chrome" in user_agent:
                    browser_counter["Chrome"] += 1
                elif "firefox" in user_agent:
                    browser_counter["Firefox"] += 1
                elif "safari" in user_agent:
                    browser_counter["Safari"] += 1
                elif "curl" in user_agent:
                    browser_counter["cURL"] += 1
                else:
                    browser_counter["Other"] += 1
        print("\n📊 Log Summary Report")
        print(f"Total Requests: {total_requests}")
        print(f"Unique IPs: {len(unique_ips)}")

        print("\nTop 5 Most Visited Pages:")
        for page, count in page_counter.most_common(5):
            print(f"{page} — {count} times")

        print("\nHTTP Status Codes:")
        for code, count in status_counter.items():
            print(f"{code} — {count} times")

        print("\nBrowsers Used:")
        for browser, count in browser_counter.items():
            print(f"{browser} — {count} times")

    # Ask user where to save
    Tk().withdraw()
    # Generate a default filename with timestamp
    filename = f"log_summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    save_path = asksaveasfilename(initialfile=filename, defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Save summary report as...")

    if save_path:
        top_pages_df = pd.DataFrame(page_counter.most_common(5), columns=["Page", "Hits"])
        status_df = pd.DataFrame(status_counter.items(), columns=["Status Code", "Count"])
        browser_df = pd.DataFrame(browser_counter.items(), columns=["Browser", "Count"])

        with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
            top_pages_df.to_excel(writer, sheet_name="Top Pages", index=False)
            status_df.to_excel(writer, sheet_name="Status Codes", index=False)
            browser_df.to_excel(writer, sheet_name="Browsers", index=False)

        print(f"\n📁 Report saved successfully to: {save_path}")
    else:
        print("❌ Export cancelled.")
         
log_parser()
