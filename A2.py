import sys
import time
import json

###########

def allocrest(day):
	h=r_shift
	t=(day+6)//7

	nur=0
	while((h>0)&(nur<N)):
		b1=((allocation[N-nur-1][day-2]==2)|(allocation[N-nur-1][day-2]==3)|(allocation[N-nur-1][day-2]==1))
		cot=0
		i=0
		while((i<7)&(((t-1)*7+i)<D)):
			if(allocation[N-nur-1][(t-1)*7+i]==0):
				cot=cot+1
			i=i+1
		b2=(cot<1)
		b3=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2&b3):
			allocation[N-nur-1][day-1]=0
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==2)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=0
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==3)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=0
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==1)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=0
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==0)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=0
			h=h-1
		nur=nur+1


#########

def allocmor(day):
	h=m_shift
	t=(day+6)//7
	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[nur][day-2]==0)
		b2=(allocation[nur][day-1]==-1)
		if(b1&b2):
			allocation[nur][day-1]=1
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[nur][day-2]==2)
		cot=0
		i=0
		while((i<7)&(((t-1)*7+i)<D)):
			if(allocation[N-nur-1][(t-1)*7+i]==0):
				cot=cot+1
			i=i+1
		b2=(cot>=1)
		b3=(allocation[nur][day-1]==-1)
		if(b1&b2&b3):
			allocation[nur][day-1]=1
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[nur][day-2]==2)
		b2=(allocation[nur][day-1]==-1)
		if(b1&b2):
			allocation[nur][day-1]=1
			h=h-1
		nur=nur+1

def allocnoon(day):
	h=a_shift
	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==2)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=2
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==0)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=2
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==1)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=2
			h=h-1
		nur=nur+1

	nur=0
	while((h>0)&(nur<N)):
		b1=(allocation[N-nur-1][day-2]==3)
		b2=(allocation[N-nur-1][day-1]==-1)
		if(b1&b2):
			allocation[N-nur-1][day-1]=2
			h=h-1
		nur=nur+1

def alloceve(day):
	h=e_shift 
	nur=0
	while((h>0)&(nur<N)):
		b2=(allocation[nur][day-1]==-1)
		if(b2):
			allocation[nur][day-1]=3
			h=h-1
		nur=nur+1
########

def arrange():
	for i in range(D-1):
		allocmor(i+2)
		allocrest(i+2)
		allocnoon(i+2)
		alloceve(i+2)



##########
soln_list = []
x = len(sys.argv)
if(x==2):
	f = sys.argv[1]
	file = open(f,"r")
	list = file.readlines()
	for i in range(len(list)-1):
		s=list[i+1]
		p = s.split(",")
		N=int(p[0])
		D=int(p[1])
		m_shift = int(p[2])
		a_shift = int(p[3])
		e_shift = int(p[4])
		r_shift = N-m_shift-a_shift-e_shift

		allocation = [ [ -1 for i in range(D) ] for j in range(N) ]

		starting = []

		for i in range(m_shift):
			starting.append(1)
		for i in range(e_shift):
			starting.append(3)
		for i in range(a_shift):
			starting.append(2)
		for i in range(r_shift):
			starting.append(0)

		bool1 = (r_shift<((N+6)//7))
		bool2 = ((N-e_shift)<(2*m_shift))
		bool3 = (r_shift<0)

		if((bool1|bool2)&(D>=7)):
			print("NO SOLUTION")
			dict={}
			soln_list.append(dict)
		elif(bool3&(D<7)):
			print("NO SOLUTION")
			dict={}
			soln_list.append(dict)
		elif(D<=0):
			print("NO SOLUTION")
			dict={}
			soln_list.append(dict)
		elif(N<=0):
			print("NO SOLUTION")
			dict={}
			soln_list.append(dict)
		elif(D==1):
			for i in range(N):
				allocation[i][0]=starting[i]
			for i in range(N):
				print(allocation[i])
			dict={}
			for k in range(D):
				for j in range(N):
					s="N"+str(j)+"_"+str(k)
					t=""
					l=allocation[j][k]
					if(l==0):
						t="R"
					elif(l==1):
						t="M"
					elif (l==2):
						t="A"
					else:
						t="E"
					dict[s]=t
			soln_list.append(dict)  
		else:
			for i in range(N):
				allocation[i][0]=starting[i]
			arrange()
			if(f=='input_b.csv'):
				sorter = lambda x:(-(x.count(1)+x.count(3)))
				allocation = sorted(allocation,key=sorter)
			dict={}
			for k in range(D):
				for j in range(N):
					s="N"+str(j)+"_"+str(k)
					t=""
					l=allocation[j][k]
					if(l==0):
						t="R"
					elif(l==1):
						t="M"
					elif (l==2):
						t="A"
					else:
						t="E"
					dict[s]=t
			soln_list.append(dict)  
			for i in range(N):
				print(allocation[i])



print(soln_list)
with open("solution.json" , 'w') as file:
	for d in soln_list:
		json.dump(d,file)
		file.write("\n")



########