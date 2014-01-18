'''
Created on 18 Jan 2014

@author: marvin
'''

import web
import json
import csv

urls = (
    '/(.*)', 'handle'
)

uid = ''
toner = ''
did = ''

class handle:

    def POST(self, data):

        j = json.loads(web.data())
        filer = Filer()
        filer.findCodeinFile(j['uid'])

class Filer:
    def writeToFile(self, toner, did):
        print 'writing to file'
            

    def findCodeinFile(self, code):
        #scan toner file
        with open ('toner.csv', 'rb') as csvfile:
            tonerreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in tonerreader:
                if (line[0] == code):
                    print 'id: ' + line[0]
                    print 'name: ' + line[1]
                    print 'model: ' + line[2]
                    break
        
        #scan department file
        with open ('department.csv', 'rb') as csvfile:
            tonerreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in tonerreader:
                if (line[0] == code):
                    print 'id: ' + line[0]
                    print 'name: ' + line[1]
                    print 'department: ' + line[2]
                    break
                
        #scan uid file
        with open ('uid.csv', 'rb') as csvfile:
            tonerreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line in tonerreader:
                if (line[0] == code):
                    print 'id: ' + line[0]
                    print 'name: ' + line[1]
                    print 'uid: ' + line[2]
                    break

    pass

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()