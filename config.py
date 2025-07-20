import os
import copy
import json

class Config:
    def __init__(self, file_name_):
        self._config = {}
        with open(file_name_, 'r') as config_file:
            self._config=json.load(config_file)
    def all(self)->dict[str, str | int]:
        return copy.deepcopy(self._config)
    def get(self, name:str)->str | int:
        return copy.deepcopy(self._config[name])
