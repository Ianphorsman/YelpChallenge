import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from yelp_challenge.yelp_data_loader import DataLoader

class Visualizer(object):

    def __init__(
        self
    ):
        self.data_loader = DataLoader()

    def browse_photos(self):
        photos = self.data_loader.iter_photos()
        for i, photo in enumerate(photos):
            plt.figure()
            plt.imshow(photo)
            plt.show()

v = Visualizer()
v.browse_photos()