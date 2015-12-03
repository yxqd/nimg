
example1 = """
filenamepattern: data/February_25/2014*_CT*_%07.3f_*.fits
angles:
  min: 0
  max: 180
  step: 1./3
"""

import numpy as np

def load(path):
    from . import loadYmlConfig
    c = loadYmlConfig(path)
    pattern = c.filenamepattern
    def _eval(token):
        try:
            return eval(token)
        except:
            return token
    angles = np.arange(*map(_eval, (c.angles.min, c.angles.max, c.angles.step)))
    from ..io import ImageSeries
    return ImageSeries(pattern, angles)
