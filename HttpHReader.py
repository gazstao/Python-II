import sys
import requests

response = requests.get(sys.argv[1], timeout=20)

print(f"Status code: {str(response.status_code)}")
print("___________________Headers: ")
for header, value in response.headers.items():
    print(header," - ",value)
print("___________________Headers Request:")
for header, value in response.request.headers.items():
    print(header, " - ", value)