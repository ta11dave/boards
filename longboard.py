import numpy
import math

#THIS IS A TEST TO MAKE SURE GIT WORKS

#functions

def trans(array):
    array=numpy.matrix(array)
    array=numpy.matrix.transpose(array)
    array=numpy.array(array)


# Program to find strength of plywood

#clear
counter1=1 #counters
counter2=1
holder=1
holder2=1
print('Draw a cross section of the board and label EVERYTHING.')
print('Label on the top as 1 and go down.')
print('This will help you from getting confused.')
print('Dont start answering questions until that picture is done!')
startmenu=raw_input('enter to start: ')
#Getting info about layers

#clc
print("--------")

layer=input('How many layers of material?: ')
print('')
print('press 1 for baltic birch')
print('press 2 for maple')
print('press 3 for a layer of fiberglass ')
print('press 4 for a layer of carbon fiber ')
print('press 5 for a costom material')

E1perlay=[]
E2perlay=[]
posrat=[]
shearmod=[]
theta=[]
density=[]
Hn=[]

while holder==1:
    #    if  modulo(counter1,2)==1
    stringa='What is layer '
    stringb=str(counter2)
    stringc=' made of?'
    stringd=stringa+stringb+stringc
    layermaterial=input(stringd)
    if  layermaterial==1:
        #birch
        print('assuming solid birch..')
        E1perlay.append(11)
        E2perlay.append(11)
        posrat.append(451)
        shearmod.append(.00579)
        theta.append(0)
        density.append(670)
        string1='height of layer '
        stringy=str(counter2)
        string2=' in inches: '
        stringcomp=string1+stringy+string2
        layerheight=input(stringcomp)
        Hn.append(layerheight*25.4) #in mm
    elif layermaterial==2:
        #maple
        E1perlay.append(12.5)
        E2perlay.append(12.5)
        posrat.append(.5)
        shearmod.append(.00951)
        theta.append(0)
        density.append(733)
        string1='height of layer '
        stringy=str(counter2)
        string2=' in inches: '
        stringcomp=string1+stringy+string2
        layerheight=input(stringcomp)
        Hn.append(layerheight*25.4) #in mm
    elif layermaterial==3:
        #fiberglass mat #fiber is .005"" thick
        E1perlay.append(69)
        E2perlay.append(69)
        posrat.append(.22)
        shearmod.append(4)
        angle=input('What angle (0 is stright front to back) ')
        theta.append(angle)
        density.append(1850)
        Hn.append(0.1)
    elif layermaterial==4:
        #carbon mat #fiber is .005"" thick
        E1perlay.append(150)
        E2perlay.append(150)
        posrat.append(.1)
        shearmod.append(4)
        angle=input('What angle (0 is stright front to back) ')
        theta.append(angle)
        density.append(1522)
        Hn.append(0.1)
    elif layermaterial==5:
        #custom material
        print('assuming isotropic')
        valueStore=input('What is the materials modulus of elasticity going front to back? (GPa) ')
        E1perlay[counter1]=valueStore
        while holder1point5==0:
            isotropic=input('Is it isotropic? 1) yes 2) no 3) lol idk ')
            if isotropic==1:
                E2perlay[counter1]=E1perlay[counter1]
                holder1point5=1
            elif isotropic==2 or isotropic==3:
                E2perlay[counter1]=input('What is the materials modulus of elasticity going side to side? (GPa) ')
                holder1point5=1
            
        
        posrat.append(input('what is the materials poisson ratio? '))
        shearmod.append(input('What is the materials shear modulus? (GPa) '))
        theta.append(input('What angle are grain/fiber? (0 is stright front to back) '))
        density.append(input('what is the material density? (kg/m**3) '))
        tensileStrength.append(input('Whats its the materials tensile strength (along grain/fiber) in GPa? '))
        shearStrength.append(input('Whats its the materials shear strength in GPa? '))
        string1='height of layer '
        stringy=str(counter2)
        string2=' in inches: '
        stringcomp=string1+stringy+string2
        layerheight=input(stringcomp)
        Hn.append(layerheight*25.4) #in mm
    else:
        clc
        print('press 1 for baltic birch')
        print('press 2 for maple')
        print('press 3 for a layer of fiberglass')
        print('press 4 for a layer of carbon fiber')
        print('press 5 for a custom material layer')
        print('And then press the return key, duh')
        print('')
        continue
    
    counter1=counter1+1 #layers of material
    counter2=counter2+1 
    if (layer)<counter1:
        print('here goes')
        holder=2
    

trans(Hn)
trans(E1perlay)

Htotal=sum(Hn)  #the conversion is from inches to mm
Htotalinches=Htotal/25.4
print('Assuming radial concave')
concavedepth=input('how deep is the concave in inches? ')*25.4
camber=input('what is the rocker in inches? Camber is negative. ')*25.4
boardwidth=input('How wide is the board in inches at the thinnest section? ')*25.4
wheelbase=input('What is the boards wheelbase in inches? ')*25.4

for item in range(0,len(density)):
    density[item]*=10**(-9)  #kg/mm**3

epsXnought=0
epsYnought=0
epsZnought=0 #board geometry details
if camber==0:
    KXnought=0
else:
    KXnought=1/((wheelbase**2+4*camber**2)/(8*camber))

if concavedepth==0:
    KYnought=0
else:
    KYnought=1/((boardwidth**2+4*concavedepth**2)/(8*concavedepth))

KXYnought=0

#premade bits for speedyness
A11=0
A12=0
A16=0
A26=0
A22=0
A66=0
B11=0
B12=0
B16=0
B26=0
B22=0
B66=0
D11=0
D12=0
D16=0
D26=0
D22=0
D66=0

#THICKNESS BIT SHOULD BE Hn?
#making a thickness bit
thickness=[]
subtracted=0 #amount to be taken away every
for counter2point5 in numpy.linspace(1,(counter1-1),(counter1-1)):
    thickness.append(Htotal-subtracted)
    subtracted+=Hn[int(counter2point5)-1]

trans(thickness)
layeredges=[]
for item in thickness:
    layeredges.append(item-Htotal/2)
layeredges.append(-1*layeredges[0])
trans(layeredges)

#May the great looping begin! Making the ABD matrix
counter3=numpy.linspace(1,(counter1-1),(counter1-1))
for loopvar in counter3:
    loopvar=int(loopvar)
    E1=E1perlay[loopvar-1]
    E2=E2perlay[loopvar-1]
    n12=posrat[loopvar-1]
    G12=shearmod[loopvar-1]
    S11=1/E1
    S12=-n12/E1
    S22=1/E2
    S66=1/G12
    Q11=S22/(S11*S22-S12**2)
    Q12=-S12/(S11*S22-S12**2)
    Q22=S11/(S11*S22-S12**2)
    Q66=G12
    Q=[[Q11,Q12,0],[Q12,Q22,0],[0,0,Q66]]
    Q=numpy.matrix(Q)
    Rtheta=theta[loopvar-1]*math.pi/180
    m=math.cos(Rtheta)
    n=math.sin(Rtheta)
    T=[[m**2,n**2,2*m*n],
    [n**2,m**2,-2*m*n],
    [-m*n,m*n,m**2-n**2]]
    T=numpy.matrix(T)
    Tinv=numpy.linalg.inv(T)
    Qbar=Tinv*Q*T
    Qbar=numpy.array(Qbar)
    Qbar[1-1][3-1]/=2
    Qbar[3-1][2-1]/=2
    Qbar[2-1][3-1]/=2
    Qbar[3-1][1-1]/=2
    loopvar2=loopvar+1
    A11=A11+Hn[loopvar-1]*Qbar[1-1][1-1]  #python starts indexing at 0
    A12=A12+Hn[loopvar-1]*Qbar[1-1][2-1]
    A16=A16+Hn[loopvar-1]*Qbar[1-1][3-1]
    A22=A22+Hn[loopvar-1]*Qbar[2-1][2-1]
    A26=A26+Hn[loopvar-1]*Qbar[2-1][3-1]
    A66=A66+Hn[loopvar-1]*Qbar[3-1][3-1]
    B11=B11+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[1-1][1-1]
    B12=B12+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[1-1][2-1]
    B16=B16+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[1-1][3-1]
    B22=B22+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[2-1][2-1]
    B26=B26+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[2-1][3-1]
    B66=B66+(layeredges[loopvar2-1]**2-layeredges[loopvar-1]**2)*Qbar[3-1][3-1]
    D11=D11+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[1-1][1-1]
    D12=D12+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[1-1][2-1]
    D16=D16+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[1-1][3-1]
    D22=D22+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[2-1][2-1]
    D26=D26+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[2-1][3-1]
    D66=D66+(layeredges[loopvar2-1]**3-layeredges[loopvar-1]**3)*Qbar[3-1][3-1]

print loopvar
print loopvar2
print layeredges

A=[[A11,A12,A16],
[A12,A22,A26],
[A16,A26,A66]]
A=numpy.matrix(A)
print('A')
print(A)
B=(1/2)*[[B11,B12,B16],
[B12,B22,B26],
[B16,B26,B66]]
B=numpy.matrix(B)
print('B')
print(B)
D=(1/3)*[[D11,D12,D16],
[D12,D22,D26],
[D16,D26,D66]]
D=numpy.matrix(D)
print('D')
print(D)
ABDcombined=numpy.vstack((numpy.hstack((A,B)),numpy.hstack((B,D)))) #figure out
print ("\n")
print("ABDcombined")
print ABDcombined

print("\n")
print("det(ABD)")
print(numpy.linalg.det(ABDcombined))  #this is what isn't working

print("\n")
#N (force per length) and M (Moment per area) **************************FIX?****************************
#figuring out the N and M matrix
NM=ABDcombined*numpy.matrix([[epsXnought+1],[epsYnought+1],[epsZnought+1],[KXnought+1],[KYnought+1],[KXYnought+1]])
print "NM"
print NM
print("\n")


#This is now an iterative process. No guess and check here.
holder3=1
weightNewtons=1
stressLfinal=0
strainLfinal=0
while holder3==1:
    
    newNM=NM+[0,0,0,weightNewtons*.5,0,0] #weight from the person
    ABDcombined=numpy.array(ABDcombined)
    ABDcombined=numpy.linalg.inv(ABDcombined) ##############PROBLEM HERE#######################
    ABDcombined=numpy.matrix(ABDcombined)
    newNoughts=ABDcombined*newNM
    #With the assumptions made for this program to work, I can only add 
    #the person's weight as a moment in the X (front-back) direction.  
    
    
    newEPSXnought=newNoughts[1-1]
    newEPSYnought=newNoughts[2-1]
    newEPSXYnought=newNoughts[3-1]
    newKXnought=newNoughts[4-1]
    newKYnought=newNoughts[5-1]
    newKXYnought=newNoughts[6-1]
    
    counter5=0  #making that Zalt business
    for loopvar5 in layeredges:
        counter5=counter5+1
        if sum(numpy.linspace(1,(counter1),(counter1)))==3:
            layeredges2=layeredges
            break
        
        if loopvar5==layeredges[1] or loopvar5==layeredges[counter1]:
            layeredges2[counter5]=loopvar5
        else:
            layeredges2[counter5]=loopvar5
            counter5=counter5+1
            layeredges2[counter5]=loopvar5
        
    trans(layeredges2)

    for loopvar3 in numpy.linspace(1,(counter1-1),(counter1-1)):
        epsX=newEPSXnought+layeredges2[loopvar3]*newKXnought
        epsY=newEPSYnought+layeredges2[loopvar3]*newKYnought
        gamXY=newEPSXYnought+layeredges2[loopvar3]*newKXYnought
        #now to find the stresses
        #material properties by layer
        counter6=0
        counter7=-1
        counter8=0
        counter9=0
        for loopvar6 in E1perlay:
            counter6=counter6+1
            E1perlay2[counter6]=loopvar6
            counter6=counter6+1
            E1perlay2[counter6]=loopvar6
        
        E1=E1perlay2[loopvar3]
        trans(E2perlay)
        for loopvar7 in numpy.linspace(1,(counter1-1),(counter1-1)):
            counter7=counter7+2
            E2perlay2[counter7]=E2perlay[loopvar7]
            E2perlay2[counter7+1]=E2perlay[loopvar7]
        
        E2=E2perlay2[loopvar3]
        trans(posrat)
        for loopvar8 in numpy.linspace(1,(counter1-1),(counter1-1)):
            counter8=counter8+1
            posrat2[counter8]=posrat[loopvar8]
            counter8=counter8+1
            posrat2[counter8]=posrat[loopvar8]
        
        n12=posrat[loopvar3]
        trans(shearmod)
        for loopvar9 in numpy.linspace(1,(counter1-1),(counter1-1)):
            counter9=counter9+1
            shearmod2[counter9]=shearmod[loopvar9]
            counter9=counter9+1
            shearmod2[counter9]=shearmod[loopvar9]
        
        G12=shearmod[loopvar3]
        S11=1/E1
        S12=-n12/E1
        S22=1/E2
        S66=1/G12
        Q11=S22/(S11*S22-S12**2)
        Q12=-S12/(S11*S22-S12**2)
        Q22=S11/(S11*S22-S12**2)
        Q66=G12
        Q=[[Q11,Q12,0],[Q12,Q22,0],[0,0,Q66]]
        Q=numpy.matrix(Q)
        Rtheta=theta[loopvar3]*pi/180
        m=math.cos(Rtheta)
        n=math.sin(Rtheta)
        T=[[m**2,n**2,2*m*n],
        [n**2,m**2,-2*m*n],
        [-m*n,m*n,m**2-n**2]]
        T=numpy.matrix(T)
        Tinv=numpy.linalg.inv(T)
        Qbar=Tinv*Q*T
        Qbar[1][3]/=2
        Qbar[3][2]/=2
        Qbar[2][3]/=2
        Qbar[3][1]/=2
        # the 'human' element lol
        strainGlobe=[epsX,epsY,gamXY] # in mm/mm
        # strains are all unitless
        #stresses should be GPa
        stressGlobe=Qbar*strainGlobe*1000
        strainLocal=T*strainGlobe
        strainLfinal=strainLfinal+strainLocal
        stressLocal=Q*strainLocal
        stressLfinal=stressLfinal+stressLocal
        strainLocal2=strainLfinal*1000 #no idea why this works
        stressLocal2=stressLfinal*1000


        #print(weightNewtons)
        #print(stressLocal2) #all time 10**9
        if E1perlay2[loopvar3]==11:  #birch
            if abs(stressLocal2[1])>39*10**6 or abs(stressLocal2[3])>8.3*10**6: #units?
                breakcause=1
                breakNewtons=(floor(weightNewtons))
                breakLBS=floor(weightNewtons*0.224808943)
                holder3=2
                break
            else:
                weightNewtons=weightNewtons+1 #increasing weight
            
        elif E1perlay2(loopvar3)==12.5: #maple
            if  abs(stressLocal2[1])>41*10**6 or abs(stressLocal2[3])>16*10**6: #units?
                breakcause=2
                breakNewtons=(floor(weightNewtons))
                breakLBS=floor(weightNewtons*0.224808943)
                holder3=2
                break
            else:
                weightNewtons=weightNewtons+1 #increasing weight
            
        elif E1perlay2(loopvar3)==69: #fiberglass
            if abs(stressLocal2[1])>0.440*10**6 or abs(stressLocal2[3])>0.04*10**6: #units?
                breakcause=3
                breakNewtons=(floor(weightNewtons))
                breakLBS=floor(weightNewtons*0.224808943)
                holder3=2
                break
            else:
                weightNewtons=weightNewtons+1 #increasing weight
            
        elif E1perlay2(loopvar3)==150: #carbon
            if abs(stressLocal2[1])>1.5*10**6 or abs(stressLocal2[3])>0.07*10**6: #units?
                breakcause=4
                breakNewtons=(floor(weightNewtons))
                breakLBS=floor(weightNewtons*0.224808943)
                holder3=2
                break
            else:
                weightNewtons=weightNewtons+1 #increasing weight
            
        elif E1perlay2(loopvar3)==valueStore: #custom
            if abs(stressLocal2[1])>tensileStrength or abs(stressLocal2[3])>shearStrength:
                breakcause=5
                breakNewtons=(floor(weightNewtons))
                breakLBS=floor(weightNewtons*0.224808943)
                holder3=2
                break
            else:
                weightNewtons=weightNewtons+1 #increasing weight
            
        
    



#now to see if it deflects more than the height of the trucks and wheels
#if it does I assume it bottoms out

# to find the moment of inertia, first i'll need a center line
centerlinePRE=0
totalMass=0
for loopvar4 in numpy.linspace(1,(counter1-1),(counter1-1)):
    layercenter=(layeredges[loopvar4]+layeredges[loopvar4+1])/2
    footplatform=boardwidth*wheelbase
    layerMass=Hn[loopvar4]*footplatform*density[loopvar4]
    centerlinePRE=centerlinePRE+layerMass*layercenter
    totalMass=totalMass+layerMass #kg


centerline=centerlinePRE/(totalMass) # units of mm

PreE=0
counter10=1 #finding all the neutral axis distances
for loopvar10 in numpy.linspace(1,(counter1-1),(counter1-1)):
    NeutralAxisDist[counter10]=(layeredges[counter10]+layeredges[counter10+1])/2-centerline
    PreE=PreE+E1perlay[counter10]*abs(layeredges[counter10]-layeredges[counter10+1])*boardwidth  
    #I'll just take an average with respect to area. 
    counter10=counter10+1


FinalE=PreE/((layeredges(1)-layeredges(counter1))*boardwidth)

# remember || axis theorm, I=Ii+Ad**2
counter11=1
IFinal=0
for loopvar11 in numpy.linspace(1,(counter1-1),(counter1-1)):
    IInitial=((layeredges[counter11]-layeredges[counter11+1])*boardwidth**3)/12
    layerarea=(layeredges[counter11]-layeredges[counter11+1])*boardwidth
    distancesquared=NeutralAxisDist[counter11]**2
    IFinal=IFinal+IInitial+layerarea*distancesquared
    counter11=counter11+1


#ok, I'm trying to find the b in a simply supported beam
#delta=(Force*Length**3)/(48*E*I)
bottomOut=48*FinalE*IFinal*(50.8+camber)/(wheelbase**3) 
#conversion from GPa to LBS
bottomOutLBS=bottomOut*145037.73773*(wheelbase*boardwidth/(25.4**2)) 

if round(bottomOutLBS)<breakLBS:
    print('Itll bottom out at')
    print(round(bottomOutLBS))
    print('lbs')
    print('and would have broken at')
    print(breakLBS)
    print('lbs')
else:
    print('Its going to snap before it bottoms out')
    print('itll hold '+str(breakLBS)+' lbs')
    breakGPa=breakLBS/(145037.73773*(wheelbase*boardwidth/(25.4**2)))
    flex=(breakGPa*wheelbase**3)/(48*FinalE*IFinal)
    flexInches=flex/25.4
    print('Itll flex ',str(flexInches),' inches')


#shows how heavy it'll be
stringe='Your board will be '
stringf=str(round(totalMass*2.2))
stringg=' lbs'
stringh=stringe+stringf+stringg
print(stringh)


