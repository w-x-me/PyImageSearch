#coding=utf-8
from json_minify import json_minify
import commentjson as json
class Conf:
    def __init__(self, confPath):
        print ("调用conf出事话函数")
        conf = json.loads(open(confPath).read())
        print (conf)
        self.__dict__.update(conf)

    def __getitem__(self, k):
      
        return self.__dict__.get(k, None)
