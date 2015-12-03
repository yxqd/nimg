from astropy.io import fits
import os, sys, numpy as np, pylab, glob


class ImageSeries:
    
    
    def __init__(self, filename_template, angles):
        self.filename_template = filename_template
        self.angles = angles
        return
    
        
    def getFilename(self, angle):
        path_pattern = filename_template % (angle,)
        base, ext = os.path.splitext(path_pattern)
        # bad code
        path_pattern = base.replace(".", "_") + ext
        
        paths = glob.glob(path_pattern)
        if len(paths)!=1:
            raise RuntimeError, "template %r no good" % filename_template
    
        path = paths[0]
        return path
    
    
    def getData(self, angle):
        path = self.getFilename(angle)
        f = fits.open(path)
        return f[0].data
