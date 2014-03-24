__author__ = 'yaoml'
#coding=utf-8
import requests
import json
import ConfigParser

def testKQLogin(username,password):
    postdata = {'username':username,'password':password,'this_is_the_login_form':'1'}
    r = requests.post('http://kq.channelsoft.com:49527/iclock/accounts/login/', postdata)
    print r.text == 'result=2'


def addKQUser(username,password):
    try:
        cf = ConfigParser.ConfigParser()
        cf.read('kq.conf')
        cf.add_section(username)
        cf.set(username, 'username', username)
        cf.set(username, 'password', password)
        cf.write(open("kq.conf", "w"))
        return True
    except:
        return False


postdata = {'username':'10979','password':'152307a','this_is_the_login_form':'1'}
session = requests.session()
r = session.post('http://kq.channelsoft.com:49527/iclock/accounts/login/', postdata)
print r.text == 'result=2'
print r.text

r1 = session.get('http://kq.channelsoft.com:49527/iclock/staff/transaction/?UserID__id__exact=1750&fromTime=2014-02-21&toTime=2014-03-20')
print r1.text
TTime = json.loads(r1.text)[0]['TTime']
print TTime
#import time
#print time.strptime(TTime,'')
r2 = session.get('http://kq.channelsoft.com:49527/iclock/staff/USER_OF_RUN/?UserID__id__exact=1750&fromTime=2014-02-21&toTime=2014-03-20')
print r2.text