#coding=utf-8
from skimage import feature
class HOG:
    def __init__(self, orientations = 12, pixelsPerCell = (4, 4), cellsPerBlock = (2, 2), normalize = True):
        self.orientations = orientations
        self.pixelsPerCell = pixelsPerCell
        self.cellsPerBlock = cellsPerBlock
        self.normalize = normalize

    def describe(self, image):
        hist = feature.hog(image, orientations = self.orientations, pixels_per_cell = self.pixelsPerCell, cells_per_block = self.cellsPerBlock, transform_sqrt = self.normalize)
        hist[hist < 0] = 0
        return hist
