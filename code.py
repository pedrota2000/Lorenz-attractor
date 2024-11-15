# INTENTARLO EN 3D A VER QUÉ COJONES SALE #
from pylab import *
# Definimos las constantes #
N = 10000  # Número de pasos deseado
sigma = 10
r  = 28
b = 8/3
t0 = 0     # Tiempo inicial #
tf = 50    # Tiempo final #
h = (tf-t0)/N
def f(v,t): # Definimos la función del lado derecho de las ecuaciones diferenciales y decimos que nos devuelva un array
    v0 = sigma*(v[1]-v[0])
    v1 = r*v[0]-v[1]-v[0]*v[2]
    v2 = v[0]*v[1]-b*v[2]
    return array([v0,v1,v2],float)
tpoints = linspace(t0,tf,N)
v = array([0.0,1.0,0.0],float) # Condiciones iniciales
xpoints = []
ypoints = []
zpoints = []
for t in tpoints: # Método de Runge Kutta de cuarto orden
    xpoints.append(v[0])
    ypoints.append(v[1])
    zpoints.append(v[2])
    k1 = h*f(v,t)
    k2 = h*(f((v+0.5*k1),(t+0.5*h)))
    k3 = h*f((v+0.5*k2),(t+0.5*h))
    k4 = h*f((v+k3),(t+h))
    v += (1/6)*(k1+2*k2+2*k3+k4)

###########################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(figsize=(20,20))
ax1 = plt.subplot(3,3,1)
ax2 = plt.subplot(3,3,2)
ax3 = plt.subplot(3,3,3)
axf = plt.subplot(3,3,(4,9),projection = '3d')

# Gráfica 1 #
ax1.set_xlim(-1,53)
ax1.set_ylim(-17,22)
ax1.grid()
ax1.set_xlabel('Time')
ax1.set_ylabel('x(t)')
ax1.set_title('Graphical representation of x(t)')


# Gráfica 2 #
ax2.set_xlim(-1,53)
ax2.set_ylim(-22,30)
ax2.grid()
ax2.set_xlabel('Time')
ax2.set_ylabel('y(t)')
ax2.set_title('Graphical representation of y(t)')


# Gráfica 3 #
ax3.set_xlim(-1,53)
ax3.set_ylim(-2,51)
ax3.grid()
ax3.set_xlabel('Time')
ax3.set_ylabel('z(t)')
ax3.set_title('Graphical representation of z(t)')

# Gráfica final #
axf.set_xlim(-20,23)
axf.set_ylim(-22,30)
axf.set_zlim(-1,51)
axf.grid()
axf.set_xlabel('x(t)')
axf.set_ylabel('y(t)')
axf.set_zlabel('z(t)')

txt_title = axf.set_title('')
line1, = ax1.plot([],[],'-r', lw = 2)
pt1, = ax1.plot([],[],'.k',ms = 20)
line2, = ax2.plot([],[],'-g', lw = 2)
pt2, = ax2.plot([],[],'.k', ms = 20)
pt3, = ax3.plot([],[],'.k', ms = 20)
line3, = ax3.plot([],[],'-m',lw = 2)
linef, = axf.plot3D([],[],[],'-b',lw = 2)
ptf, = axf.plot3D([],[],[],'.k', ms = 20)
tpoints = np.linspace(0,50,10000)

# LA ANIMACIÓN #
def drawframe(n):
    x = xpoints[n]
    y = ypoints[n]
    z = zpoints[n]
    t = tpoints[n]
    txt_title.set_text('Frame = {:4d}'.format(n))
    linef.set_data_3d(xpoints[0:n],ypoints[0:n],zpoints[0:n])
    ptf.set_data_3d(x,y,z)
    line1.set_data(tpoints[0:n],xpoints[0:n])
    pt1.set_data(t,x)
    line2.set_data(tpoints[0:n],ypoints[0:n])
    pt2.set_data(t,y)
    line3.set_data(tpoints[0:n],zpoints[0:n])
    pt3.set_data(t,z)
    angle = (360/10000)*n+45 
    axf.view_init(30, angle)
    return (linef,ptf)

from matplotlib import animation
anim = animation.FuncAnimation(fig, drawframe, frames = 10000, interval = 1, blit = True)

matplotlib.rcParams['animation.embed_limit'] = 2**128

from matplotlib import rc
rc('animation',html = 'html5')

anim
