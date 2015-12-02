#!/usr/bin/env python
# usage: display_fits_image.py filename_template angle_min,angle_max,delta_angle cmin,cmax
# 

from astropy.io import fits
import os, sys, numpy as np, pylab, glob

filename_template = sys.argv[1]
angle_min, angle_max, delta_angle = eval(sys.argv[2])
cmin, cmax = eval(sys.argv[3])

for angle in np.arange(angle_min, angle_max, delta_angle):
    
    path_pattern = filename_template % (angle,)
    base, ext = os.path.splitext(path_pattern)
    # bad code
    path_pattern = base.replace(".", "_") + ext
    
    paths = glob.glob(path_pattern)
    if len(paths)!=1:
        raise RuntimeError, "template %r no good" % filename_template
    
    path = paths[0]
    print path
    f = fits.open(path)
    img = f[0].data
    
    pylab.imshow(img)
    pylab.colorbar()
    pylab.clim(cmin, cmax)
    pylab.show()
    del f
