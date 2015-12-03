#

from .AbstractOperator import AbstractOperator

class crop:
    
    def __init__(self, window):
        self.window = window
        return
    
    def __call__(self, data):
        left, right, top, bottom = self.window
        return data[top:bottom, left:right]
    
