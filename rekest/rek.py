import requests
import json

URL = "https://ttsmp3.com/makemp3_new.php"

data = {
    'msg': 'Welcome again boss',
    'lang': 'Brian',
    'source': 'ttsmp3'
}

headers = {

}

if __name__ == '__main__':
    response = requests.post(url=URL, data=data)
    response_data = json.loads(response.text)