import json
from pathlib import Path
import numpy as np
import pandas as pd
import tensorflow as tf

class Preprocessor(object):

    def __init__(
        self
    ):
        self.paths = self.resolve_data_paths()
        assert len(self.paths.keys()) >= 1, "Please supply paths to your Yelp json and/or image datasets in the data_env.json file"

    

    def resolve_data_paths(self):
        with open('../data_env.json') as file:
            data_env = json.load(file)
        return {k: v for k, v in data_env.items() if Path(v).exists() and v != ""}



preprocessor = Preprocessor()