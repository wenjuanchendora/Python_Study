import requests
# import json

from ddt import ddt, data, unpack
from getData import get_csv_data

@data(*get_csv_data('data.csv'))
@unpack
def posttest(self,post_url,update_url,accesstoken_input,title_input,tab_input,content_input):
    post_topic_url = post_url

    post_data = {
        "accesstoken":accesstoken_input,
    	"title":title_input,
    	"tab":tab_input,
    	"content":content_input
    }

    res = requests.post(post_topic_url,json=post_data)
    r = res.json()

    id = r['topic_id']

    update_topic_url = 'http://118.31.19.120:3000/api/v1/topics/update'

    update_data = {
        "accesstoken":accesstoken_input,
        "topic_id":id,
    	"title":title_input,
    	"tab":tab_input,
    	"content":content_input
    }

    res = requests.post(update_topic_url,json=update_data)


