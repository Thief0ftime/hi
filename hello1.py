exit=6*60**2+52*60
low=8*60+15
med=7*60+12
calc=exit+1*low+3*med+1*low #Here we got 27006
h=calc/60**2  #here we start calculate hour 
h1=int(h)    
qh=str(h1)     #here we end
m=(h-h1)*60
m1=int(m)
qm=str(m1)
s=(m-m1)*60
s1=int(s)
qs=str(s1)
#ques=x2*0.6
#sh=str(h1)
#sq=int(ques*100)
#sqr=str(sq)
#print(sh+(':')+sqr)
print(qh+':'+qm+':'+qs)



 
