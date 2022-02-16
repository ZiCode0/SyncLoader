import os
import yaml

__root_folder__ = os.path.split(os.path.split(__file__)[0])[0]


class YamlConfig:
    data = None

    def __init__(self, path):
        with open(path, "r") as stream:
            try:
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def __getattr__(self, item):
        return self.data[item]


stations = YamlConfig(path=os.path.join(__root_folder__, 'config.yaml')).stations
main = YamlConfig(path=os.path.join(__root_folder__, 'config.yaml')).main
