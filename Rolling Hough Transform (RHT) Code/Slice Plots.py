from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import aplpy



#Velocity Values Array
velocity_step=(-0.82443237)*(10**3)
start_value=28211.5
velocity_array=np.zeros(88)
velocity_array[0]=start_value

i=1
while i<=len(velocity_array)-1:
    velocity_array[i]=velocity_array[i-1]+velocity_step
    i=i+1
    
velocity_array=velocity_array/1000



#Generating Plots
i=69
while i<=156:
    fig = plt.figure(figsize=(9,9))
    f1  = aplpy.FITSFigure(str(i)+'H_Slice.fits',figure=fig,subplot=(1,1,1),convention='calabretta')
    f1.show_colorscale(cmap="afmhot",vmin = -0.198815, vmax = 0.212316)
    # axis labels
    f1.axis_labels.set_font(size=15)
    # tick labels
    f1.tick_labels.show()
    f1.tick_labels.set_font(size=15)
    # colour bar
    f1.add_colorbar()
    f1.colorbar.set_axis_label_text(r"$HI\,\mathrm{(K)}$")
    f1.colorbar.set_axis_label_font(size=15)
    f1.set_title(str(round(velocity_array[i-69],4))+" km/s HI Velocity Channel")
    i=i+1
    # fig.canvas.draw()
    f1.close()
    f1.save(str(i)+"Slice.png")