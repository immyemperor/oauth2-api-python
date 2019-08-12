import requests
import config
import util
import json
from requests.exceptions import ConnectionError

def get_finance_data():
    access_token=json.loads(util.get_token())["access_token"]
    print(access_token)
    host_ip,host_name=util.get_Host_name_IP()
    print('host=',host_name,'address=',host_ip)
    headers={
        "Authorization":"Bearer "+access_token,
        'REMOTE_ADDR':host_ip,
        'REMOTE_HOST':host_name
    }
    print(headers)
    res=requests.get(config.data_url,headers=headers)
    if res is not None:
        #print(res.text)
        return res.text
    else:
        return {'error': res.error}
  


print(get_finance_data())