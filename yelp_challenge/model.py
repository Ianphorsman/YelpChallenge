from yelp_challenge.yelp_data_loader import DataLoader
from yelp_challenge.yelp_preprocessor import Preprocessor
from yelp_challenge.yelp_visualizer import Visualizer

class Model(object):

    def __init__(
        self
    ):
        self.preprocess = Preprocessor()
        self.visualize = Visualizer()