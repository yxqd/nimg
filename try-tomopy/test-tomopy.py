#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct the Anka topo-tomo tomography data as original tiff.
"""

from __future__ import print_function
import tomopy

if __name__ == '__main__':

    obj = tomopy.baboon()
    theta = tomopy.angles(180)
    proj = tomopy.project(obj, theta)
    import pdb; pdb.set_trace()

    # Find rotation center.
    rot_center = tomopy.find_center(proj, theta, emission=False, init=1024, ind=0, tol=0.5)
    print("Center of rotation: ", rot_center)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(proj, theta, center=rot_center, algorithm='gridrec', emission=False)

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    tomopy.write_tiff_stack(rec, fname='recon_dir/recon')
