import requests

print("测试--------------------------")
response = requests.get(url="http://www.twitter.com")
print(response.text)