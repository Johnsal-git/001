import requests
import readline
from time import strftime,localtime

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
try:
    print ('---------------------------------')
    url=input('please input your url here:')
    r=requests.get(url,headers=headers)
    mseconds=r.elapsed.total_seconds()*1000
    print ('Time:',strftime("%Y-%m-%d %H:%M:%S", localtime()))
    print ('Status_code is:',r.status_code)
    print ("Response-time:",mseconds,'ms')
    print ('---------------------------------')
except:
    print ('Failed!')
    print ('---------------------------------')

