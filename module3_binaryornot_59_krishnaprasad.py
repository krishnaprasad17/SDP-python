#STRING IS BINARY OR NOT...??
k=input("enter your string :")

i=0
j=1
while(i<len(k)):
    if(k[i]=="0" or k[i]=="1"):
        print("ITS A BINARY STRING")
        break
        
    else:
        j=0
        i=i+1
        
if(j==0):
    print("NOPE NOT A BINARY STRING")
