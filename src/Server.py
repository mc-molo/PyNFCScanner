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

import web
import json
import csv
import datetime

urls = (
    '/(.*)', 'handle'
)

nid = ''    #nfc id
tid = ''    #toner id
did = ''    #department id
count = 0

class handle:

    def POST(self, data):

        j = json.loads(web.data())
        filer = Filer()
        filer.findCodeinFile(j['uid'])

        #check if did and tid are set
        if (tid == '' or did == ''):
            #skip and wait for more data
            print 'not enough data'
        else:
            #all data available to write to file
            filer.writeToFile(tid, did)
        
        return 0

class Filer:
    def writeToFile(self, local_tid, local_did):
        print 'writing to file'
        #yes, right now we're doing nothing with the local copies of the variable
        #maybe once i'll get the hang of python i'll remove the globals and only work with local
        #or maybe even a class for the set [tid, did]
        
        global count
        global tid
        global did
                
        i = datetime.datetime.now()
        time = "%s-%s-%s" % (i.year, i.month, i.day)
        count += 1
        
        with open('storage.csv', 'ab') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
            csvwriter.writerow([tid[1]] + [tid[2]] + [did[2]] + [time] + [count])
        
        tid = ''
        did = ''
        

    def findCodeinFile(self, code):
        #scan tid file
        with open ('toner.csv', 'rb') as csvfile:
            tonerreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in tonerreader:
                if (line[0] == code):
                    global tid
                    tid = line
                    break
        
        #scan department file
        with open ('department.csv', 'rb') as csvfile:
            departmentreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in departmentreader:
                if (line[0] == code):
                    global did
                    did = line
                    break
                
        #scan uid file
        with open ('uid.csv', 'rb') as csvfile:
            nfcreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in nfcreader:
                if (line[0] == code):
                    global nid
                    nid = line
                    break

    pass

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()