import requests

get_topic_url = 'http://118.31.19.120:3000/api/v1'

res = requests.get(get_topic_url+"/topics?page=3&tab=ask&limit=1")

print(res.json())

assert res.status_code == 200