## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


# base_url = 'http://127.0.0.1:5000/' #base url local host
base_url = 'http://ec2-user@ec2-35-88-95-237.us-west-2.compute.amazonaws.com:5000/'

json_data = {
"age":42,
"sex":1,
"cp":1,
"trestbps":120,
"chol":295,
"fbs":0,
"restecg":1,
"thalach":162,
"exang":0,
"oldpeak":0.0,
"slope":2,
"ca":0,
"thal":2
}


test = pd.read_csv("test.csv", index_col=0)
test = test.to_json(orient='records')
test = json.loads(test)


# Get Response
# response = r.get(base_url + 'helloworld')
# response = r.post(base_url + "predict", json = json_data)
response = r.post(base_url + "predict", json = test)

if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')