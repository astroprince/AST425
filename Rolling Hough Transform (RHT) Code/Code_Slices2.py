from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

FileName="g182_hi_crop"
AllData=fits.getdata(FileName+'.fits')

for i in range (0,256):
    Slice=AllData[i]
    hdu = fits.PrimaryHDU(Slice)
    hdul = fits.HDUList([hdu])
    hdul.writeto(str(i+1)+'Slice.fits')