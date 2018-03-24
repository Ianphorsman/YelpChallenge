import json, os
import numpy as np
import pandas as pd


class Preprocessor(object):

    def __init__(
        self,
        data_loader=None
    ):
        self.data_loader = data_loader

    def data_completeness(self, df):
        return sum(df.count()) / df.size * 100