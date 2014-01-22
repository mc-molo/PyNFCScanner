'''
#    Copyright (C) 2014 marvin
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import serial
import json
import urllib2

def send_json(uid):
    
    data = {
            'uid': uid
    }
    
    req = urllib2.Request('http://localhost:30003')
    req.add_header('Content-Type', 'application/json')
    
    urllib2.urlopen(req, json.dumps(data))
    #print response
    
    
ser = serial.Serial(0)  # open first serial port

while True:
    line = ser.readline()
    #print line
    send_json(line[:-1])
