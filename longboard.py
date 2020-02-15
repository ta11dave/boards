import numpy
import math
#import a clue

#THIS IS A TEST TO MAKE SURE GIT WORKS

#functions

def trans(anarray):
	anarray=numpy.matrix(anarray)
	anarray=numpy.transpose(anarray)
	anarray=numpy.array(anarray)
	return anarray

#to replace mylinspace
def mylinspace(start, stop, terms):
	firstarray =[]
	myarray=[]
	val = start
	firstarray.append(val)
	amt = (stop-start)/terms
	while val != stop:
		val += amt
		firstarray.append(val)
	for anumber in firstarray:  #makes results int type if int
		if anumber%1 == 0:
			myarray.append(int(anumber))
		else:
			myarray.append(anumber)
	return myarray


# Program to find strength of plywood

interfacingEdges=1
mylayer=1
inputLoop=True
print('Draw a cross section of the board and label EVERYTHING.')
print('Label on the top as 1 and go down.')
print('This will help you from getting confused.')
print('Dont start answering questions until that picture is done!')
startmenu=input('enter to start: ')
#Getting info about layers

#clc
print("--------")

layer=input('How many layers of material?: ')
print('')
print('press 1 for baltic birch')
print('press 2 for maple')
print('press 3 for a layer of fiberglass ')
print('press 4 for a layer of carbon fiber ')
print('press 5 for a custom material')

E1perlay=[]
E2perlay=[]
posrat=[]
shearmod=[]
theta=[]
density=[]
Hn=[]

while inputLoop==True:
	stringa='What is layer '
	stringb=str(mylayer)
	stringc=' made of?'
	stringd=stringa+stringb+stringc
	layermaterial=input(stringd)
	if  layermaterial=='1':
		#birch
		print('assuming solid birch..')
		E1perlay.append(11)
		E2perlay.append(11)
		posrat.append(451)
		shearmod.append(.00579)
		theta.append(0)
		density.append(670)
		string1='height of layer '
		stringy=str(mylayer)
		string2=' in inches: '
		stringcomp=string1+stringy+string2
		layerheight=float(input(stringcomp))
		Hn.append(layerheight*25.4) #in mm
	elif layermaterial=='2':
		#maple
		E1perlay.append(12.5)
		E2perlay.append(12.5)
		posrat.append(.5)
		shearmod.append(.00951)
		theta.append(0)
		density.append(733)
		string1='height of layer '
		stringy=str(mylayer)
		string2=' in inches: '
		stringcomp=string1+stringy+string2
		layerheight=float(input(stringcomp))
		Hn.append(layerheight*25.4) #in mm
	elif layermaterial=='3':
		#fiberglass mat #fiber is .005"" thick
		E1perlay.append(69)
		E2perlay.append(69)
		posrat.append(.22)
		shearmod.append(4)
		angle=int(input('What angle in degrees (0 is stright front to back) '))
		theta.append(angle)
		density.append(1850)
		Hn.append(0.1)
	elif layermaterial=='4':
		#carbon mat #fiber is .005"" thick
		E1perlay.append(150)
		E2perlay.append(150)
		posrat.append(.1)
		shearmod.append(4)
		angle=int(input('What angle in degrees (0 is stright front to back) '))
		theta.append(angle)
		density.append(1522)
		Hn.append(0.1)
	elif layermaterial=='5':
		#custom material
		print('assuming isotropic')
		valueStore=input('What is the materials modulus of elasticity going front to back? (GPa) ')
		E1perlay[interfacingEdges]=valueStore
		while isotropicType==True:
			isotropic=input('Is it isotropic? 1) yes 2) no 3) lol idk ')
			if isotropic=='1':
				E2perlay[interfacingEdges]=E1perlay[interfacingEdges]
				isotropicType==False
			elif isotropic=='2' or isotropic=='3':
				E2perlay[interfacingEdges]=int(input('What is the materials modulus of elasticity going side to side? (GPa) '))
				isotropicType==False
			
		
		posrat.append(input('what is the materials poisson ratio? '))
		shearmod.append(input('What is the materials shear modulus? (GPa) '))
		theta.append(input('What angle are grain/fiber? (0 is stright front to back) '))
		density.append(input('what is the material density? (kg/m**3) '))
		tensileStrength.append(input('Whats its the materials tensile strength (along grain/fiber) in GPa? '))
		shearStrength.append(input('Whats its the materials shear strength in GPa? '))
		string1='height of layer '
		stringy=mylayer
		string2=' in inches: '
		stringcomp=string1+stringy+string2
		layerheight=float(input(stringcomp))
		Hn.append(layerheight*25.4) #in mm
	else:
		print('-----------------------------------------------------')
		print('Just type the number and hit return')
		print('-----------------------------------------------------')
		print('press 1 for baltic birch')
		print('press 2 for maple')
		print('press 3 for a layer of fiberglass')
		print('press 4 for a layer of carbon fiber')
		print('press 5 for a custom material layer')
		print('And then press the return key, duh')
		print('')
		continue

	interfacingEdges=interfacingEdges+1 #layers of material
	mylayer=mylayer+1 
	if float(layer)<mylayer:
		#print('here goes')
		inputLoop=False
		break

trans(Hn)
trans(E1perlay)

Htotal=sum(Hn)  #the conversion is from inches to mm
Htotalinches=Htotal/25.4
print('Assuming radial concave')
concavedepth=float(input('how deep is the concave in inches? '))*25.4
camber=float(input('what is the rocker in inches? Camber is negative. '))*25.4
boardwidth=float(input('How wide is the board in inches at the thinnest section? '))*25.4
wheelbase=float(input('What is the boards wheelbase in inches? '))*25.4

#for testing
print('TESTING ON')
concavedepth=0.1*25.4
camber=0.1*25.4
boardwidth=5*25.4
wheelbase=40*25.4

#*******************************INPUT DONE**************************

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

perboard = mylinspace(0,(interfacingEdges-2),(interfacingEdges-2))

thickness.append(Htotal)
for eachboard in perboard: #for each interfacing layer...
	subtracted+=Hn[int(eachboard)]
	thickness.append(Htotal-subtracted) #make a thickness 

layeredges=[]
for item in thickness:
	layeredges.append(item-Htotal/2)
layeredges=trans(layeredges)

#May the great looping begin! Making the ABD matrix
counter3=mylinspace(0,(interfacingEdges-2),(interfacingEdges-2)) #for each board
for loopvar in counter3:
	print(loopvar)
	loopvar=int(loopvar)
	E1=E1perlay[loopvar]
	E2=E2perlay[loopvar]
	n12=posrat[loopvar]
	G12=shearmod[loopvar]
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

#print(layeredges)

A=[[A11,A12,A16],[A12,A22,A26],[A16,A26,A66]]
A=numpy.matrix(A)
print('A')
print(A)
B=numpy.multiply((1/2),[[B11,B12,B16],[B12,B22,B26],[B16,B26,B66]])
B=numpy.matrix(B)
print('B')
print(B)
D=numpy.multiply((1/3),[[D11,D12,D16],[D12,D22,D26],[D16,D26,D66]])
D=numpy.matrix(D)
print('D')
print(D)
ABDcombined=numpy.vstack((numpy.hstack((A,B)),numpy.hstack((B,D)))) #figure out
print("\n")
print("ABDcombined")
print(ABDcombined)

print("\n")
print("det(ABD)")
print(numpy.linalg.det(ABDcombined))

print("\n")
#N (force per length) and M (Moment per area) **************************FIX?****************************
#figuring out the N and M matrix
NM=ABDcombined*numpy.matrix([[epsXnought],[epsYnought],[epsZnought],[KXnought],[KYnought],[KXYnought]])
print("NM")
print(NM)
print("\n")


#idk what this shit is?
E1perlay2 = E1perlay
E2perlay2 = E2perlay

#This is now an iterative process. No guess and check here.
weightloop=1
weightNewtons=1 #starting at 1 Newton (.225 lbs)
stressLfinal=0
strainLfinal=0
layeredges2=layeredges
GetOut = False
while weightloop==True:
		
	#newNM=NM+[0,0,0,weightNewtons*.5,0,0] #weight from the person
	newNM=NM
	newNM[3] = newNM[3]+ weightNewtons*.5
	ABDcombined=numpy.array(ABDcombined)
	ABDcombined=numpy.linalg.inv(ABDcombined)
	ABDcombined=numpy.matrix(ABDcombined)
	newNoughts=ABDcombined*newNM
	#With the assumptions made for this program to work, I can only add 
	#the person's weight as a moment in the X (front-back) direction.  
	
	
	newEPSXnought=newNoughts[0]
	newEPSYnought=newNoughts[1]
	newEPSXYnought=newNoughts[2]
	newKXnought=newNoughts[3]
	newKYnought=newNoughts[4]
	newKXYnought=newNoughts[5]
	
	#counter5=0  #making that Zalt business
	#for loopvar5 in layeredges:		
	#	if loopvar5==layeredges[1] or loopvar5==layeredges[interfacingEdges-1]:
	#		layeredges2[counter5]=loopvar5
	#	else:
	#		layeredges2[counter5]=loopvar5
	#		counter5=counter5+1
	#		layeredges2[counter5]=loopvar5
		
	#trans(layeredges2)
	
	for loopvar3 in mylinspace(0,(interfacingEdges-2),(interfacingEdges-2)):
		epsX=newEPSXnought+layeredges2[loopvar3]*newKXnought
		epsY=newEPSYnought+layeredges2[loopvar3]*newKYnought
		gamXY=newEPSXYnought+layeredges2[loopvar3]*newKXYnought
		#now to find the stresses
		#material properties by layer
		counter6=0
		counter7=0
		counter8=0
		counter9=0
#		for loopvar6 in E1perlay:
#			print(E1perlay2)
#			E1perlay2[counter6]=loopvar6
#			counter6 += 1
		
		E1=E1perlay2[loopvar3]
		trans(E2perlay)
#		for loopvar7 in mylinspace(1,(interfacingEdges-1),(interfacingEdges-1)):
#			counter7=counter7+interfacingEdges-1
#			E2perlay2[counter7]=E2perlay[loopvar7]
#			E2perlay2[counter7+1]=E2perlay[loopvar7]
		
		E2=E2perlay2[loopvar3]
		trans(posrat)
#		for loopvar8 in mylinspace(1,(interfacingEdges-1),(interfacingEdges-1)):
#			counter8=counter8+1
#			posrat2[counter8]=posrat[loopvar8]
#			counter8=counter8+1
#			posrat2[counter8]=posrat[loopvar8]
		
		n12=posrat[loopvar3]
		trans(shearmod)
#		for loopvar9 in mylinspace(1,(interfacingEdges-1),(interfacingEdges-1)):
#			counter9=counter9+1
#			shearmod2[counter9]=shearmod[loopvar9]
#			counter9=counter9+1
#			shearmod2[counter9]=shearmod[loopvar9]
		
		
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
		Rtheta=theta[loopvar3]*3.14159/180
		m=math.cos(Rtheta)
		n=math.sin(Rtheta)
		T=[[m**2,n**2,2*m*n],
		[n**2,m**2,-2*m*n],
		[-m*n,m*n,m**2-n**2]]
		T=numpy.matrix(T)
		Tinv=numpy.linalg.inv(T)
		Qbar=Tinv*Q*T
		Qbar=numpy.array(Qbar)
		Qbar[0][2]/=2
		Qbar[2][1]/=2
		Qbar[1][2]/=2
		Qbar[2][0]/=2
		Qbar=numpy.matrix(Qbar)#new
		# the 'human' element lol
		epsX=numpy.array(epsX)[0][0]
		epsY=numpy.array(epsY)[0][0]
		gamXY=numpy.array(gamXY)[0][0]
		strainGlobe=[[epsX],[epsY],[gamXY]] # in mm/mm
		# strains are all unitless
		#stresses should be GPa
		stressGlobe=Qbar*strainGlobe
		strainLocal=T*strainGlobe
		strainLfinal=strainLfinal+strainLocal
		stressLocal=Q*strainLocal
		stressLfinal=stressLfinal+stressLocal
		strainLocal2=strainLfinal /1000 #units were converted here
		stressLocal2=stressLfinal /1000
		
		
		#print(stressLocal2) #all time 10**9
		if E1perlay2[loopvar3]==11:  #birch
			if abs(stressLocal2[0])>39*10**6 or abs(stressLocal2[2])>8.3*10**6: #units?
				breakcause=1
				breakNewtons=(math.floor(weightNewtons))
				breakLBS=math.floor(weightNewtons*0.224808943)
				GetOut=True
			
		elif E1perlay2[loopvar3]==12.5: #maple
			if abs(stressLocal2[0])>41*10**6 or abs(stressLocal2[2])>16*10**6: #units?
				breakcause=2
				breakNewtons=(math.floor(weightNewtons))
				breakLBS=math.floor(weightNewtons*0.224808943)
				GetOut=True
			
		elif E1perlay2[loopvar3]==69: #fiberglass
			if abs(stressLocal2[0])>0.440*10**6 or abs(stressLocal2[2])>0.04*10**6: #units?
				breakcause=3
				breakNewtons=(math.floor(weightNewtons))
				breakLBS=math.floor(weightNewtons*0.224808943)
				GetOut=True
			
		elif E1perlay2[loopvar3]==150: #carbon
			if abs(stressLocal2[0])>1.5*10**6 or abs(stressLocal2[2])>0.07*10**6: #units?
				breakcause=4
				breakNewtons=(math.floor(weightNewtons))
				breakLBS=math.floor(weightNewtons*0.224808943)
				GetOut=True
			
		elif E1perlay2[loopvar3]==valueStore: #custom
			if abs(stressLocal2[0])>tensileStrength or abs(stressLocal2[2])>shearStrength:
				breakcause=5
				breakNewtons=(math.floor(weightNewtons))
				breakLBS=math.floor(weightNewtons*0.224808943)
				GetOut=True
		
		if GetOut == True:
			weightloop=False
		else:
			weightNewtons=weightNewtons+1 #increasing weight
			
		
	

#now to see if it deflects more than the height of the trucks and wheels
#if it does I assume it bottoms out

# to find the moment of inertia, first i'll need a center line
centerlinePRE=0
totalMass=0
for loopvar4 in mylinspace(0,(interfacingEdges-2),(interfacingEdges-2)):
	layercenter=(layeredges[loopvar4]+layeredges[loopvar4+1])/2
	footplatform=boardwidth*wheelbase
	layerMass=Hn[loopvar4]*footplatform*density[loopvar4]
	centerlinePRE=centerlinePRE+layerMass*layercenter
	totalMass=totalMass+layerMass #kg


centerline=centerlinePRE/(totalMass) # units of mm

NeutralAxisDist = []
PreE=0
#finding all the neutral axis distances
for loopvar10 in mylinspace(0,(interfacingEdges-2),(interfacingEdges-2)):
	NeutralAxisDist.append(0)
	NeutralAxisDist[loopvar10]=(layeredges[loopvar10]+layeredges[loopvar10+1])/2-centerline
	PreE=PreE+E1perlay[loopvar10]*abs(layeredges[loopvar10]-layeredges[loopvar10+1])*boardwidth  
	#I'll just take an average with respect to area. 


FinalE=PreE/((layeredges[0]-layeredges[interfacingEdges-1])*boardwidth)

# remember || axis theorm, I=Ii+Ad**2
IFinal=0
for loopvar11 in mylinspace(0,(interfacingEdges-2),(interfacingEdges-2)):
	IInitial=((layeredges[loopvar11]-layeredges[loopvar11+1])*boardwidth**3)/12
	layerarea=(layeredges[loopvar11]-layeredges[loopvar11+1])*boardwidth
	distancesquared=NeutralAxisDist[loopvar11]**2
	IFinal=IFinal+IInitial+layerarea*distancesquared


#ok, I'm trying to find the b in a simply supported beam
#delta=(Force*Length**3)/(48*E*I)
bottomOut=48*FinalE*IFinal*(50.8+camber)/(wheelbase**3) 
#conversion from GPa to LBS
bottomOutLBS=bottomOut*145037.73773*(wheelbase*boardwidth/(25.4**2)) 
bottomOutLBS=bottomOutLBS[0]

if round(bottomOutLBS,0)<breakLBS:
	print('Itll bottom out at')
	print(round(bottomOutLBS,0))
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


