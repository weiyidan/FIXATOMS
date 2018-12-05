#!/usr/bin/python3

###### Written by Yidan Wei ######
###### Address: 272918553@qq.com ######
###### If any bug exists, contact me ######

fo = open("POSCAR",'w')
fC = open("CONTCAR")
for i in range (1,9):
	linefc = fC.readline()
	fo.write( linefc )

f = open("OUTCAR")               # 返回一个文件对象 
line = f.readline()               # 调用文件的 readline()方法 
str_force = "TOTAL-FORCE"
str_drift = "total drift:"
receive = []
count_force = 0
count_drift = 0
line_force = []
line_drift = []
line_total  = 0
count = 0
criterion = float(input("input:"))

# 读取行数
while line: 
	line_total+=1
	line = f.readline()
#print (line_total)

# 读取最后的力
f.seek(0) #返回文件头
line2 = f.readline()

while line2: 
	exit_force = line2.find(str_force)   
	count_force+=1
	if exit_force!=-1:
		line_force.append(count_force)
	line2 = f.readline()
#print (line_force[-1])
Begin = line_force[-1]

f.seek(0) #返回文件头
line3 = f.readline()

while line3: 
	exit_drift = line3.find(str_drift)   
	count_drift+=1
	if exit_drift!=-1:
		line_drift.append(count_drift)
	line3 = f.readline()
#cleaprint (line_drift[-1])
Final = line_drift[-1]

# 写入另一个文件
f.seek(0) #返回文件头
line4 = f.readline()
fix  = " F F F \n"
move = " T T T \n"

while line4: 
	count+=1	
	if count in range (Begin+2, Final-1):
		if float(line4.split()[3])<criterion and float(line4.split()[4])<criterion and float(line4.split()[5])<criterion:
			line4=line4.strip('\n')		
			line4+=fix
			fo.write( line4 )
			print (line4)
		else:
			line4=line4.strip('\n')
			line4+=move
			fo.write( line4 )
			print (line4)
	line4 = f.readline()


f.close()
