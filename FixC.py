#!/usr/bin/python3

######################################################
###### Written by Yidan Wei ##########################
###### Address: 272918553@qq.com #####################
###### If any bug exists, contact me #################
######################################################
fo = open("POSCAR_NEW",'w')
fC = open("POSCAR")
line_total = 0
j=0
k=0
for i in range (1,10):
	linefc = fC.readline()
	fo.write( linefc )

minimum = float(input("minimum input:"))
maximum = float(input("maximum input:"))

line = fC.readline()
fC.seek(0)
while line: 
	line_total+=1
	line = fC.readline()

fC.seek(0) 
line2 = fC.readline()
fix  = " F F F \n"
move = " T T T \n"

while line2:
	if j>8: 	
		if float(line2.split()[2])<minimum or float(line2.split()[2])>maximum: #line2.split()[2]代表Z方向，line2.split()[0]代表x方向，line2.split()[1]代表y方向，自己手动改一下就行了
			line2=line2.replace("T","")
			line2=line2.strip('\n')		
			line2+=fix
			fo.write( line2 )
			print (line2)
		else:
			line2=line2.replace("T","")
			line2=line2.strip('\n')		
			line2+=move
			fo.write( line2 )
			print (line2)
	j+=1
	line2 = fC.readline()

fC.close()
