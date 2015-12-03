#!/usr/bin/env python

import unittest, numpy as np

class TestCase(unittest.TestCase):
    
    def test(self):
        "load image series configuration"
        from nimg.config.imageseries import load
        path = "imageseries.yml"
        imageseries = load(path)
        self.assertEqual(
            imageseries.filename_template, "2014*_CT*_%07.3f_*.fits")
        np.testing.assert_array_almost_equal(
            np.arange(0, 180, 1./3), 
            imageseries.angles
        )
        return


if __name__ == '__main__': unittest.main()
