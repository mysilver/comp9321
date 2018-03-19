import codecs
import pickle


def serialize(object):
    return codecs.encode(pickle.dumps(object, pickle.HIGHEST_PROTOCOL), "base64").decode()


def deserialize(object_string):
    return pickle.loads(codecs.decode(object_string.encode(), "base64"))
