#

class ImageSeriesMappingOperator:
    
    """map an operator onto an image series,
    to produce an output image series of same length
    """
    
    def __init__(self, input_imageseries, operator, output_template):
        self.input_imageseries = input_imageseries
        self.operator = operator
        self.output_template = output_template
        return

    
    def run(self):
        for angle in self.input_imageseries.angles:
            self.applyOperatorOnOneImage(angle)
            continue
        return
        
        
    def applyOperatorOnOneImage(self, angle):
        input_imagefile = self.input_imageseries.getImageFile(angle)
        data = input_imagefile.getData()
        data1 = self.operator(data)
        # output
        from .io import ImageFile
        output_imagefile = ImageFile(self.output_template % angle)
        output_imagefile.data = data1
        output_imagefile.save()
        return
        
