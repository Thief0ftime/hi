exit=6*60+52
low=8+15/60
med=7+12/60
calc=exit+1*low+3*med+1*low
x=calc/60
x1=int(x)
x2=x-x1
ques=x2*0.6
sx=str(x1)
sq=int(ques*100)
sqr=str(sq)
print(sx+(':')+sqr)



 
