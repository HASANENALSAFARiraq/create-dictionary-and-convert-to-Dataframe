import  pandas as pd
import matplotlib.pyplot as p

d={'x':[1,2,3,4,5],'y':[2,4,5,4,5],'y^':[2.8,3.4,4,4.6,5.2]}
convert=pd.DataFrame(d)
x_=sum(convert['x'])/5
y_=sum(convert['y'])/5
x_x=convert['x']-x_
y_y=convert['y']-y_

convert['x-']=(x_)
convert['y-']=(y_)
convert['x-x']=pd.DataFrame(x_x)
convert['y-y']=(y_y)
xtr=convert['x-x']*convert['x-x']
convert['x-x^2']=(xtr)
xymult=convert['x-x']*convert['y-y']
convert['(x-y_)(y-x_)']=xymult
print(convert)

Bsum=sum(convert['(x-y_)(y-x_)'])
Bsum2=sum(convert['x-x^2'])
B1=Bsum/Bsum2
B0=y_-B1*x_
print(B0)

p.scatter(convert['x'],convert['y'])
p.plot(convert['x'],convert['y^'])




