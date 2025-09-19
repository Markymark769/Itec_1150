#!/usr/bin/env python3

# Step 1: status code development
# import sys
# import requests

# url = 'https://www.cloudflare.com/'

# response = requests.get(url)
# if response.status_code == 200:
#     print(f"OK - HTTP 200 {url}")
#     sys.exit(0)   # OK
# else:
#     print(f"CRITICAL - HTTP {response.status_code} {url}")
#     sys.exit(2)   # Critical



# Step 2: more complex
#!/usr/bin/env python3

# import sys
# import requests

# def check_http(url):
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             print(f"OK - HTTP 200 {url}")
#             sys.exit(0)   # OK
#         else:
#             print(f"CRITICAL - HTTP {response.status_code} {url}")
#             print('no reponse from code')
#             sys.exit(2)   # Critical
#     except Exception as error:
#         print(f"CRITICAL - HTTP check failed for {url}: {error}")
#         sys.exit(2)

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: check_http_simple.py <URL>")
#         sys.exit(3)   # Unknown
#     url = sys.argv[1]
#     print('this shit is working for {url}.') ## check for debug
#     check_http(url)

# if __name__ == "__main__":
#     main()

#note to get working in the cmd enter:
# python check_http_simple.py https://www.cloudflare.com/

# Step 3: EVEN MORE COMPLEX!!!!!
#!/usr/bin/env python3

import argparse
import sys
import requests
import time

def check_http(url, warning=2.0, critical=5.0, timeout=10):
    """
    Nagios-style HTTP check.
    - url: the site to check
    - warning: response time (seconds) threshold for WARNING
    - critical: response time (seconds) threshold for CRITICAL
    - timeout: HTTP timeout in seconds
    Returns (exit_code, message)
    """
    try:
        start = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed = time.time() - start

        if response.status_code != 200:
            return 2, f"CRITICAL: HTTP {response.status_code} for {url}"

        # Evaluate thresholds based on response time
        if elapsed >= critical:
            return 2, f"CRITICAL: {url} responded in {elapsed:.3f}s"
        elif elapsed >= warning:
            return 1, f"WARNING: {url} responded in {elapsed:.3f}s"
        else:
            return 0, f"OK: {url} responded in {elapsed:.3f}s (HTTP 200)"

    except Exception as e:
        return 2, f"CRITICAL: HTTP check failed for {url} - {e}"

def main():
    parser = argparse.ArgumentParser(description="Nagios plugin for HTTP check.")
    parser.add_argument("url", help="URL to check (e.g., https://example.com)")
    parser.add_argument("-w", "--warning", type=float, default=2.0,
                        help="Warning threshold for response time (seconds)")
    parser.add_argument("-c", "--critical", type=float, default=5.0,
                        help="Critical threshold for response time (seconds)")
    parser.add_argument("-t", "--timeout", type=int, default=10,
                        help="HTTP request timeout (seconds)")
    args = parser.parse_args()

    code, msg = check_http(args.url, args.warning, args.critical, args.timeout)
    print(msg)
    sys.exit(code)

if __name__ == "__main__":
    main()

