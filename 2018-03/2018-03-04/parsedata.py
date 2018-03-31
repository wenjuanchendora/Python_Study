data = [['accesstoken', 'title', 'tab', 'content'],
        ['6eb92a53-9392-4dc5-a10a-3a853cad6e2c', 'helloworld', 'share', 'hshahdhsahashhdhahda']]

def parse_data():
    json_data ={}
    for i in range(len(data)):
        for j in range(len(data[i])):
            json_data[data[0][j]] = data[1][j]
    print(json_data)

# parse_data()


jsondata = {
    "accesstoken": "6eb92a53-9392-4dc5-a10a-3a853cad6e2c",
    "title": "helloworld",
    "tab": "share",
    "content": "how to do api testing"
}

def queue_json_data():
    # print(jsondata.keys(),jsondata.values())
    for x in jsondata.keys():
        temp = jsondata[x]
        jsondata[x] = ""
        print(jsondata)
        jsondata[x] = temp

queue_json_data()
