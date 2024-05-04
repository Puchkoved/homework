a=int(input('введите число'))
cod=[]
st=''
for i in range (2,a+1):
        if a%i==0:
            for j in range (0,(i//2)+1):
                 if j!=i-j:
                     cod.append((j,i-j))
cod.sort()
for i in range (0,len(cod)):
    for j in range (0,2):
            s=str (cod[i][j])
            st=st+s
print(a,'-',st)













