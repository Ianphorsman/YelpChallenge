import numpy as np
import pandas as pd
import tensorflow as tf
from yelp_challenge.yelp_data_loader import DataLoader

class Preprocessor(object):

    def __init__(
        self
    ):
        self.data_loader = DataLoader()