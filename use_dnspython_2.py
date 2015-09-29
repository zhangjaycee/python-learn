#!/usr/bin/python

import httplib
import os
import dns.resolver

iplist = []
domain = "www.xidian.edu.cn"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception,e:
        print "dns resolver error:" + str(e)
        return 
    
    for i in A.response.answer:
        for j in i.items:
            if 'address' in dir(j):
                iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ':80'
    getcontent = ''
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers = {"Host": domain})
        r = conn.getresponse()
        getcontent = r.read(17)
    finally:
        #print getcontent[3:]
        if getcontent[3:] == "<!DOCTYPE html":
            print ip + "\t[OK]"
        else:
            print ip + "\t[ERROR]"

if __name__ == "__main__":
    if get_iplist(domain) and len(iplist) > 0:
        for ip in iplist:
            print ip
            checkip(ip)
    else:
        print "dns resolver error."


        

