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
        return ImageFile(path).getData()


class ImageFile:

    def __init__(self, path):
        self.path = path
        return


    def getData(self):
        fn, ext = os.path.splitext(self.path)
        handler = 'handle_' + ext[1:]
        return getattr(self, handler)()

        
    def handle_fits(self):
        from astropy.io import fits
        f = fits.open(self.path)
        d = f[0].data
        f.close()
        return d
