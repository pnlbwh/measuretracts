#!/usr/bin/env python
import sys
import argparse

sys.path.append('/projects/schiz/software/SlicerModules/MeasureTracts')
from measureTractsFunctions import printToCSV
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
    [names,values]=printToCSV(files, str(fileName))
    print names, values
if __name__=="__main__":
    CLI()
