import requests

print("测试--------------------------")
response = requests.request(url="www.twitter.com", method="get")
print(response.content)