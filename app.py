import os
import re
import flask
from flask import request, jsonify
from collections import Counter

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def parse_log_file(log_file_path):
    log_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*?)\] "(.*?)" (\d+) \d+ "(.*?)" "(.*?)"'
    ip_addresses = set()
    top_referrers = {}
    status_codes = {}
    ip_address_requests = {}
    
    with open(log_file_path, "r") as f:
        for line in f:
            match = re.match(log_pattern, line)
            if match:
                ip_address = match.group(1)
                status_code = match.group(4)
                request_type = match.group(3)
                referrer = match.group(5)
                
                ip_addresses.add(ip_address)
                if request_type.startswith("GET"):
                    top_referrers[referrer] = top_referrers.get(referrer, 0) + 1
                status_codes[status_code] = status_codes.get(status_code, 0) + 1
                ip_address_requests[ip_address] = ip_address_requests.get(ip_address, 0) + 1
                
    unique_ip_address_count = len(ip_addresses)
    top_5_referrers = dict(sorted(top_referrers.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return {
        "unique_ip_address_count": unique_ip_address_count,
        "ip_address_requests": ip_address_requests,
        "status_codes_distribution": status_codes,
        "top_5_referrers": top_5_referrers
    }

@app.route("/stats", methods=['GET'])
def stats():
    log_file_path = os.environ.get("LOG_FILE_PATH")
    log_data = parse_log_file(log_file_path)
    return jsonify(log_data)

app.run()
