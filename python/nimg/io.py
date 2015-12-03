from astropy.io import fits
import os, sys, numpy as np, pylab, glob


class ImageSeries:
    
    
    def __init__(self, filename_template, angles):
        self.filename_template = filename_template
        self.angles = angles
        return
    
        
    def getFilename(self, angle):
        path_pattern = self.filename_template % (angle,)
        dir = os.path.dirname(path_pattern)
        basename = os.path.basename(path_pattern)
        base, ext = os.path.splitext(basename)
        # bad code
        path_pattern = os.path.join(dir, base.replace(".", "_") + ext)
        
        paths = glob.glob(path_pattern)
        if len(paths)!=1:
            raise RuntimeError, "template %r no good: \npath_pattern=%r" % (
                self.filename_template, path_pattern)
    
        path = paths[0]
        return path
    
    
    def getData(self, angle):
        path = self.getFilename(angle)
        f = fits.open(path)
        return f[0].data
