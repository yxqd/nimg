#!/usr/bin/env python
# usage: display_fits_images.py filename_template angle_min,angle_max,delta_angle cmin,cmax
# display_fits_images.py data/February_25/2014*_CT*_%07.3f_*.fits 0,180,30 0,3000

maxN = 11

from astropy.io import fits
import os, sys, numpy as np, pylab, glob

filename_template = sys.argv[1]
angle_min, angle_max, delta_angle = eval(sys.argv[2])
cmin, cmax = eval(sys.argv[3])

def getPaths():
    return [p for p in iterPaths()]

def iterPaths():
    for angle in np.arange(angle_min, angle_max, delta_angle):
    
        path_pattern = filename_template % (angle,)
        base, ext = os.path.splitext(path_pattern)
        # bad code
        path_pattern = base.replace(".", "_") + ext
        
        paths = glob.glob(path_pattern)
        if len(paths)!=1:
            raise RuntimeError, "template %r no good" % filename_template
    
        path = paths[0]
        yield path
        continue
    return
    
paths = getPaths()
N = len(paths)
if N > maxN:
    raise RuntimeError("too many images")

cols = int(np.sqrt(N)) + 1
rows = int(np.ceil(1.*N/cols))

import matplotlib.pyplot as plt
plt.figure(1)
for index, path in enumerate(paths):
    plt.subplot(rows, cols, index)
    print path
    f = fits.open(path)
    img = f[0].data
    
    pylab.imshow(img)
    # pylab.colorbar()
    pylab.clim(cmin, cmax)
    del f
    
    continue
pylab.show()
