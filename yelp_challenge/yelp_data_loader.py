import json, os, random
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


class DataLoader(object):

    def __init__(
        self
    ):
        self.paths = self.resolve_data_paths()
        assert len(self.paths.keys()) >= 1, "Please supply paths to your Yelp json and/or image datasets in the data_env.json file."

        # if chunksize is not None then self.data will be a generator yielding chunks of the file
        self.photos = self.load_json('photos', chunksize=None)
        print(self.random_photo(show=True))

    def load_json(self, name, chunksize=None):
        can_open = self.file_exists_for(name=name)
        if not can_open[0]:
            return can_open[1]
        return pd.read_json(can_open[1], lines=True, chunksize=chunksize)

    def load_photos(self):
        pass

    def iter_photos(self):
        can_open = self.file_exists_for(photos=True)
        if not can_open[0]:
            return can_open[1]
        for filename in os.listdir(can_open[1]):
            yield plt.imread(os.path.join(can_open[1], filename))

    def random_photo(self, show=False):
        can_open = self.file_exists_for(photos=True)
        if not can_open[0]:
            return can_open[1]
        filename = random.choice(os.listdir(can_open[1]))
        return plt.imread(os.path.join(can_open[1], filename))


    def queue(self):
        pass

    def resolve_data_paths(self):
        with open('../data_env.json') as file:
            data_env = json.load(file)
        return {k: v for k, v in data_env.items() if Path(v).exists() and v != ""}

    def file_exists_for(self, name=None, photos=False):
        if not photos:
            if 'json_dataset_absolute_path' in self.paths:
                path = Path(os.path.join(self.paths['json_dataset_absolute_path'], "{}.json".format(name)))
            elif 'json_dataset_relative_path' in self.paths:
                path = Path(os.path.join(self.paths['json_dataset_relative_path'], "{}.json".format(name)))
            else:
                return False, "You need to supply the path to the {}.json file in data_env.json".format(name)
            if not path.is_file():
                return False, "The file {} does not exist.".format(str(path))
            return True, str(path)
        else:
            if 'image_dataset_absolute_path' in self.paths:
                path = Path(self.paths['image_dataset_absolute_path'])
            elif 'image_dataset_relative_path' in self.paths:
                path = Path(self.paths['image_dataset_relative_path'])
            else:
                return False, "You need to supply the path to the photos directory in data_env.json"
            if not path.exists():
                return False, "The path {} does not exists.".format(str(path))
            return True, str(path)