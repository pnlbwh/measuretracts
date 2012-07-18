from DTImeasures import *
import getTensorData
import numpy as np
import csv

def VTKdata(VTK):

    pTract=getTensorData.get_all_tensors(VTK)
    num_fibers = getTensorData.get_num_fibers(VTK)
    length=len(pTract)

    listOfNames = ['FA','trace','mode','Linear','Planar','Spherical','axial','radial']
    results = {}
    for num in range(len(listOfNames)):
        currentName=listOfNames[num]
        results[currentName]={}

    for num in results.keys():
        results[num]['values'] = np.zeros(length)

    retLi=np.zeros(length)
    retSp=np.zeros(length)
    retPl=np.zeros(length)

    for i in range(length):
            
            currentTensor=np.array(pTract[i]).reshape((3,3))
            ev=np.linalg.eig(currentTensor)[0]
            
            for num in range(len(ev)):#eliminate negative numbers
                if ev[num]<0:
                    ev[num]=0

            ev.sort()
            ev2=np.copy(ev)
            ev[0]=ev2[2]
            ev[2]=ev2[0]

            results['mode']['values'][i]=computeModeFromTensor(currentTensor)
            results['trace']['values'][i]=tracer(currentTensor)
            [retLi[i], retPl[i], retSp[i]]=computeLPSFromTensorEigenvalues(ev)   
            results['Linear']['values'][i]=retLi[i]
            results['Planar']['values'][i]=retPl[i]
            results['Spherical']['values'][i]=retSp[i]
            #results['RA']['values'][i]=computeRAFromTensorEigenvalues(ev)
            results['FA']['values'][i]=computeFAFromTensorEigenvalues(ev)
            results['axial']['values'][i]=1000*ev[0]
            results['radial']['values'][i]=1000*(ev[1]+ev[2])/2
    i=0
    for measure in results.keys():
            data=results[measure]['values']       
            results[measure]['mean'] = 1000*sum(data)/length
            results[measure]['min'] = 1000*min(data)
            results[measure]['max'] = 1000*max(data)
            results[measure]['std'] = 1000*data.std()

    rawValues={}
    for measure in results.keys():
        rawValues=results[measure]['values']
        del results[measure]['values']

    results['num_fibers'] = {'mean': numfibers}
    listOfNames += ['num_fibers']
    return  results, listOfNames #, rawValues
