#!/usr/bin/env python
import sys
import argparse
def printToCSV(files,fileName): 
    print files  
    #files is the list of VTKs that will be analyzed, fileName is the name that the CSV will be saved as
    
    from computeAllMeasuresVTK import VTKdata
    
    import csv    
    import os
    import re    

    data={}
    firstFile=files[0]
    print "\t"
        
    [firstFile, listOfNames]=VTKdata(firstFile)

    print "\n",

    operation=[]
    data=[]    

    print "file name \t",

    length=len(listOfNames)
    operation=['min','max','mean','std']

    measureTitles = [0]*length*len(operation)
    measureNums = [0]*length*len(operation)

    count = 0    

    for num in range(length):
        for i in range(len(operation)):
            
            print listOfNames[num] + "-" + operation[i] + "\t",
            measureTitles[count] = listOfNames[num] + "-" + operation[i]
            count = count+1
    if os.path.exists(fileName):
        fileOut=csv.writer(open(fileName, 'a'), delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar=' ')
    else:
        fileOut=csv.writer(open(fileName, 'w'), delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar=' ')
        titles=re.sub('\|', '',str(measureTitles),count=0)
        fileOut.writerow(['file name', re.sub('\[', '',str(titles),count=0)])        


    measureNums = [0]*length*len(operation)
    print "\n",
    for VTK in files:
        [results, listOfNames]=VTKdata(VTK)
        print VTK + "\t",
        count=0
        for num in range(length):
            for i in range(len(operation)):
                print "\t",
                currentName=listOfNames[num]
                currentOperation=operation[i]
                print results[currentName][currentOperation],
                measureNums[count]=results[currentName][currentOperation]
                count = count+1
        [results, listOfNames]=VTKdata(VTK)
        #measureNums=str(measureNums)        
        #measureNums=re.sub('\[', '', measureNums, count=0)
        #measureNums=re.sub('\]', '', measureNums, count=0)
        fileOut.writerow((VTK, re.sub('\[', '',str(measureNums),count=0)))    
def CLI():

    parser = argparse.ArgumentParser(description='computes various tract measures including FA and mode and saves the data to a ".csv"')
    parser.add_argument('-i', '--input', dest='files', nargs='+', required=True, help='enter the VTK files you wish to analyze separated by spaces')
    parser.add_argument('-o', '--output', dest='fileName', nargs=1, required=True, help='name the output that you wish to save your data to')
    parser.add_argument('-f', '--force', default=False, dest='force', required=False, action='store_true', help='specify in order to automatically overwrite any file that shares the name of your output file')
    
    args = parser.parse_args()
    
    import os
    files=args.files
    force=args.force
    fileName=str(args.fileName[0])

    for fileNum in range(len(files)):
        if not os.path.exists(files[fileNum]):
            print "sorry, no file found at" + files[fileNum]
    if os.path.isfile(fileName) and force==False:        
        print "The file " + fileName + " already exists. Are you sure you want to append? [y/n]"
        if raw_input()=='n':
            sys.exit()
    if os.path.isdir(fileName):
        print "Sorry, but the file output name you've entered is already the name of a directory. Please rerun with a different output name"
        sys.exit()
    if '.csv' not in fileName:
        print "Please enter an output with extension .csv"
        
        sys.exit()
    printToCSV(files, str(fileName))
if __name__=="__main__":
    CLI()
