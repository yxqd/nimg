#!/usr/bin/env python
# usage: display_fits_image.py filename cmin,cmax
# 

from astropy.io import fits
import os, sys

# path = os.path.join("data", "February_25", "20140226_CT_GEsample_0090_134_100_0447.fits")
# cmin, cmax = 0, 3000

path = sys.argv[1]
cmin, cmax = eval(sys.argv[2])
f = fits.open(path)
img = f[0].data

import pylab
pylab.imshow(img)
pylab.colorbar()
pylab.clim(cmin, cmax)
pylab.show()
