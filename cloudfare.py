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
