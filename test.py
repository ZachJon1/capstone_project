import requests

#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://uk07iee9we.execute-api.us-east-2.amazonaws.com/crackdetectiontest/predict'

data = {'url': 'https://raw.githubusercontent.com/ZachJon1/capstone_project/main/img/test_1.jpg?token=AOGFKC7NBH2KMHLZFQHB7U3BWWFP4'}


result = requests.post(url, json=data).json()
print(result)