#decode logic of rot 13 alog 
apfa=[" ",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
plantext=[]
cipertext=[]
msg=input("enter the string to enter : ")
a=msg.upper()
for i in a:
	if(i in apfa):
		if(i !=" "):
			inx=apfa.index(i)
			jnx=inx+13
			if(jnx>26):
				jnx=jnx-26
				dex=apfa[jnx]
				cipertext.append(dex)
			else:
				dex=apfa[jnx]
				cipertext.append(dex)
		else:
			cipertext.append("#")
	else:
		cipertext.append(" ")

print("the plan text you entered: ",end="")
for i in a:
	print(i,end="")
print()
print("the ciper text :",end="")
for i in cipertext:
	print(i.lower(),end="")				
				
	
