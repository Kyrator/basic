# TODO здесь писать код

class MyDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)
