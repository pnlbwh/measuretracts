files = ['test1.vtk', 'test2.vtk']
from /projects/schiz/software/scripts/MeasureTracts-DK/dataChecker/measureTracts import printToCSV
printToCSV(files, 'testValues.csv')

import csv

CVals=[]
TVals=[]

for numLines in open('correctValues.csv'):    
    CVals=[CVals, numLines.split("\s")]
    
for numLines in open('testValues.csv'):
    TVals=[TVals, numLines.split("\s")]

CVals.pop(0)#removes the headings of the data columns
TVals.pop(0)

print CVals
print TVals

if CVals==TVals:
    print "there is no error in this file"
else:
    print "errors found, check data above"
