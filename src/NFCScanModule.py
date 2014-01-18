'''
Created on 18 Jan 2014

@author: marvin
'''

import nfc
import sys
import json
import urllib2


def send_json(uid):
    
    
    data = {
            'uid': uid
    }
    
    req = urllib2.Request('http://localhost:30003')
    req.add_header('Content-Type', 'application/json')
    
    response = urllib2.urlopen(req, json.dumps(data))
    #print response


def format_data(data, w=16):
    if type(data) is not type(str()):
        data = str(data)
    s = []
    for i in range(0, len(data), w):
        s.append("")
        s[-1] += ''.join(["%02x" % ord(c) for c in data[i:i+w]])
        s[-1] += (8 + w*3 - len(s[-1])) * ' '
    return '\n'.join(s)

def getTT2UID(tag):
    memory = bytearray()
    for offset in range(0, 1 * 4, 8):
        try: memory += tag[offset:offset+8]
        except nfc.clf.DigitalProtocolError as error:
            print error
    tag.clf.sense([nfc.clf.TTA(uid=tag.uid)])
    return format_data(memory)
        
def connected(tag):     
    if tag.ndef:
        record = tag.ndef.message.pop(i=-1)
        #print record.data[-14:]
        send_json(record.data[-14:])
        
        
    elif tag.type == "Type2Tag":
        taguid = getTT2UID(tag)
        #print "NFCSCan: " + taguid
        sys.exit(0)
        if getTT2UID(tag) == '04a3f4db8a583280':
            #print "NFCSCan: bye bye"
            sys.exit(0)
    #else:
        #print "NFCSCan: Sorry, no NDEF"
    return True
    

while True:
    #print "NFCSCan: starting scan"
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect': connected})        
        