import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


# Duration of the animation
t0=0 # [s]
t_end=4 # [s]
dt=0.02 # [s]
dt5=0.001 # For creating a thin circle

# Create array for time
t=np.arange(t0,t_end+dt,dt)
t5=np.arange(t0,t_end+dt5,dt5) # For creating a thin circle

# Create x & y for circular motion
r=125 # [mm]
f=0.5 # [Hz]
alpha=2*np.pi*f*t
x1=r*np.cos(alpha)
y1=r*np.sin(alpha)

x2=r*np.cos(alpha-np.pi/2)
y2=r*np.sin(alpha-np.pi/2)

x3=r*np.cos(alpha-np.pi)
y3=r*np.sin(alpha-np.pi)

x4=r*np.cos(alpha-3*np.pi/2)
y4=r*np.sin(alpha-3*np.pi/2)

alpha5=2*np.pi*f*t5 # For creating a thin circle
x5=r*np.cos(alpha5) # For creating a thin circle
y5=r*np.sin(alpha5) # For creating a thin circle

connector_length=467 # [mm]

frame_amount=len(t)

def update_plot(num):
    global pos,arrow_text
    pos.remove()
    arrow_text.remove()
    pos=ax.arrow(400,200,dx=x1[num],dy=y1[num],length_includes_head=True,head_width=10,head_length=20,color='g',linewidth=5)
    pos.set_zorder(5)
    arrow_text = ax.text(400+x1[num]+20,200+y1[num]+20,'arrow', fontsize=11)
    arrow_text.set_zorder(5)
    point_A_side_1.set_data([[x1[num]-5,x1[num]+5],[y1[num],y1[num]]])
    point_A_side_2.set_data([[x2[num]-5,x2[num]+5],[y2[num],y2[num]]])
    point_A_side_3.set_data([[x3[num]-5,x3[num]+5],[y3[num],y3[num]]])
    point_A_side_4.set_data([[x4[num]-5,x4[num]+5],[y4[num],y4[num]]])
    point_A_side_5.set_data([[x1[num]-600-5,x1[num]-600+5],[y1[num],y1[num]]])
    bridge_sides_13.set_data([[x1[num],x3[num]],[y1[num],y3[num]]])
    bridge_sides_24.set_data([[x2[num],x4[num]],[y2[num],y4[num]]])
    bridge_sides_5.set_data([[x1[num]-600,-600],[y1[num],0]])
    connector_2.set_data([[x1[num]-600,x1[num]],[y1[num],y1[num]]])
    connector.set_data([[x1[num],x1[num]+(connector_length**2-r**2)**0.5],[y1[num],0]])
    point_B.set_data([[x1[num]+(connector_length**2-r**2)**0.5-70,x1[num]+(connector_length**2-r**2)**0.5+70],[0,0]])

    return bridge_sides_13,bridge_sides_24,bridge_sides_5,connector_2,point_A_side_2,point_A_side_3,\
        point_A_side_4,point_A_side_5,connector,point_A_side_1,point_B,pos,arrow_text

# Define figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(4,4)
plt.subplots_adjust(left=0.03,bottom=0.035,right=0.99,top=0.97,wspace=0.15,hspace=0.2)
ax=fig.add_subplot(gs[:,0:4],facecolor=(0.9,0.9,0.9))

pos=ax.arrow(400,200,dx=x1[0],dy=y1[0],length_includes_head=True,head_width=10,head_length=10,color='g',linewidth=2)
arrow_text = ax.text(400+x1[0]+20,200+y1[0]+20,'arrow', fontsize=11)

point_A_side_1,=ax.plot([],[],'r',linewidth=10)
point_A_side_1.set_zorder(5)
point_A_side_2,=ax.plot([],[],'w',linewidth=10)
point_A_side_2.set_zorder(4)
point_A_side_3,=ax.plot([],[],'w',linewidth=10)
point_A_side_3.set_zorder(4)
point_A_side_4,=ax.plot([],[],'w',linewidth=10)
point_A_side_4.set_zorder(4)
point_A_side_5,=ax.plot([],[],'r',linewidth=10)
point_A_side_5.set_zorder(5)
point_A_side_6,=ax.plot([-595,-605],[0,0],'k',linewidth=10)
point_A_side_6.set_zorder(3)
bridge_sides_13,=ax.plot([],[],'k',linewidth=10,alpha=1)
bridge_sides_13.set_zorder(3)
bridge_sides_24,=ax.plot([],[],'k',linewidth=10,alpha=1)
bridge_sides_24.set_zorder(3)
bridge_sides_5,=ax.plot([],[],'k',linewidth=5)
bridge_sides_5.set_zorder(3)
connector_2,=ax.plot([],[],'k',linewidth=5)
connector_2.set_zorder(4)
connector,=ax.plot([],[],'k',linewidth=5)
connector.set_zorder(4)
point_B,=ax.plot([],[],'b',linewidth=50,alpha=0.5)
pipe_up=ax.plot([400,700],[40,40],'k',linewidth=8)
pipe_down=ax.plot([400,700],[-40,-40],'k',linewidth=8)
wall_middle=ax.plot([700,700],[-40,40],'k',linewidth=8)
plate_A,=ax.plot([0,0],[-10,10],'g',linewidth=250)
plate_A.set_zorder(2)
circle=ax.plot(x5[:],y5[:],'k',linewidth=10)

plt.xlim(-800,800)
plt.ylim(-400,400)
plt.xlabel('x-length [mm]',fontsize=12)
plt.ylabel('y-length [mm]',fontsize=12)
plt.grid()


engine_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=False,blit=True)
# plt.show()

# # Matplotlib 3.3.3 needed or newer - comment out plt.show()
Writer=animation.writers['ffmpeg']
writer=Writer(fps=30,metadata={'artist': 'Me'},bitrate=1800)
engine_ani.save('engine_ani.mp4',writer)










































#
