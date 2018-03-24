import json
from pathlib import Path
import numpy as np
import pandas as pd
import tensorflow as tf


class DataLoader(object):

    def __init__(
        self
    ):
        self.paths = self.resolve_data_paths()
        assert len(self.paths.keys()) >= 1, "Please supply paths to your Yelp json and/or image datasets in the data_env.json file."

    # Data Loading

    def load_json(self, name, random=False):
        pass

    def load_photos(self):
        pass

    def queue(self):
        pass

    def resolve_data_paths(self):
        with open('../data_env.json') as file:
            data_env = json.load(file)
        return {k: v for k, v in data_env.items() if Path(v).exists() and v != ""}





dl = DataLoader()