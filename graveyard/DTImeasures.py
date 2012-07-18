import numpy as np

def tracer(currentTensor):
    trace=sum(currentTensor.diagonal(offset=0, axis1=0, axis2=1))
    return trace    

def computeLPSFromTensorEigenvalues(ev):
    if ev[0]==0:
        #all eigenvalues are zero; so this is a perfect trivial sphere
        retLi=0;
        retPl=0;
        retSp=1;
    else:
        retLi=(ev[0]-ev[1])/ev[0]
        retPl=(ev[1]-ev[2])/ev[0]
        retSp=(ev[2])/ev[0]
    return retLi, retPl, retSp

def computeRAFromTensorEigenvalues(ev):
    denom = (2**.5*(ev[1]+ev[2]+ev[0]))
    if denom > 0:
        ret = float(((ev[0]-ev[1])**2 + (ev[1]-ev[2])**2 + (ev[0]-ev[2])**2 )**0.5)/denom
    else:
        #this is a perfectly trivial sphere
        ret=0
    return ret

def computeModeFromTensor(currentTensor):
    eye3=np.array([[1,0,0],[0,1,0],[0,0,1]])
    AT=currentTensor-(1/3.0)*tracer(currentTensor)*eye3
    normAT=(AT[0,0]**2 + 2*AT[0,1]**2 + 2*AT[0,2]**2 + AT[1,1]**2 + 2*AT[1,2]**2 + AT[2,2]**2)**0.5;
    if(normAT>0):
        mode=3*((6)**0.5)*np.linalg.det((AT)/normAT)
    else:
        mode=0
    return mode

def computeFAFromTensorEigenvalues(ev):
    #denom = ((2*(ev[1]**2+ev[2]**2+ev[0]**2))**0.5)
    meanEv=(ev[0]+ev[1]+ev[2])/3.0
    numer=((ev[0]-meanEv)**2+(ev[1]-meanEv)**2+(ev[2]-meanEv)**2)**0.5
    denom=(ev[0]**2+ev[1]**2+ev[2]**2)**.5
    if denom > 0:
        #ret = (((ev[1]-ev[2])**2+(ev[2]-ev[0])**2+(ev[1]-ev[0])**2)**0.5)/denom
        ret=(1.5)**.5*(numer/denom)
    else:
        ret = 0
    return ret

#print "Enter the file name you want to import"
    #VTK=raw_input()
