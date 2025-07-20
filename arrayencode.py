import numpy
import json

class JsonToArrayBuffer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return super().default(obj)
