#!/usr/bin/python

import dns.resolver


domain = raw_input('input an domain:')

###A###
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        if 'address' in dir(j):
            print j.address
        else:
            print 'failed to resolver'
###MX###
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print 'MX preference =', i.preference, 'mail exchanger =', i.exchange


