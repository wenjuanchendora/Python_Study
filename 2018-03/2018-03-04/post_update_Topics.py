import requests
# import json

from getData import get_csv_data

post_topic_url = 'http://118.31.19.120:3000/api/v1/topics'

post_data = {
    "accesstoken":"6119cc39-80dd-4717-a8d7-b9268f9a6bdf",
	"title":"1234513",
	"tab":"ask",
	"content":"1234513"
}

res = requests.post(post_topic_url,json=post_data)
print(res.json())
r = res.json()
id = r['topic_id']

assert res.status_code == 200

update_topic_url = 'http://118.31.19.120:3000/api/v1/topics/update'

update_data = {
    "accesstoken":"6119cc39-80dd-4717-a8d7-b9268f9a6bdf",
    "topic_id":id,
	"title":"1234514",
	"tab":"ask",
	"content":"1234514"
}

res = requests.post(update_topic_url,json=update_data)

assert res.status_code == 200