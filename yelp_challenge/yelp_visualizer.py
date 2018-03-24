import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Visualizer(object):

    def __init__(
        self,
        data_loader=None
    ):
        self.data_loader = data_loader

    def browse_photos(self):
        photos = self.data_loader.iter_photos()
        for i, photo in enumerate(photos):
            plt.figure()
            plt.imshow(photo)
            plt.show()