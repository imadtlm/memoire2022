import pandas as pd
from pylab import * 
from scipy.optimize import leastsq
from matplotlib.ticker import StrMethodFormatter


df = pd.read_csv('GaN.outputeos',delim_whitespace=True,lineterminator='\n',on_bad_lines='skip' ,skiprows=10, nrows=11)
print(df.columns)
print(df['vol'])
e=df['energy'].to_numpy()
v = df['vol'].to_numpy()


#make a vector to evaluate fits on with a lot of points so it looks smooth
vfit = np.linspace(min(v),max(v),100)

### fit a parabola to the data
# y = ax^2 + bx + c
a,b,c = polyfit(v,e,2) #this is from pylab



#now here are our initial guesses.
v0 = -b/(2*a)
e0 = a*v0**2 + b*v0 + c
b0 = 58
bP = 4

#now we have to create the equation of state function
def Murnaghan(parameters,vol):
    '''
    given a vector of parameters and volumes, return a vector of energies.
    equation From PRB 28,5480 (1983)
    '''
    E0 = parameters[0]
    B0 = parameters[1]
    BP = parameters[2]
    V0 = parameters[3]
    
    E=E0+(B0*vol/BP*(1/(BP-1)*(V0/vol)**BP +1)-B0*V0/(BP-1))/14703.6
   

    return E

# and we define an objective function that will be minimized
def objective(pars,y,x):
    #we will minimize this function
    err =  y - Murnaghan(pars,x)
    return err

x0 = [e0, b0, bP, v0] #initial guesses in the same order used in the Murnaghan function

murnpars, ier = leastsq(objective, x0, args=(e,v)) #this is from scipy
#gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
figure(figsize=(8, 6))
gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
#now we make a figure summarizing the results
plot(v,e,'ro')

plot(vfit, Murnaghan(murnpars,vfit), label='Murnaghan ')
xlabel('Volume ($\AA^3$)')
ylabel('Énergie (eV)')
legend(loc='best')

#add some text to the figure in figure coordinates
ax = gca()
text(0.4,0.9,"$GaN$",transform = ax.transAxes)
text(0.4,0.8,'$V_0$= %1.8f $\AA^3$' % murnpars[3],transform = ax.transAxes)
text(0.4,0.7,'B=  %1.5f GPa' % (murnpars[1]) , transform = ax.transAxes)
text(0.4,0.6,'BP=  %1.5f ' % (murnpars[2]) , transform = ax.transAxes)
text(0.4,0.5,'$E_0$=  %1.5f eV' % (murnpars[0]) , transform = ax.transAxes)
savefig('GaNMurnaghan.png')
show()
