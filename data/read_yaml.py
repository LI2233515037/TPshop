import sys
import os

sys.path.append(os.getcwd())
import yaml
import json


def read_yaml():
    with open('E:\\项目01\\TPshop\\data\\login.json', encoding="utf-8", )as f:
        read = json.load(f)
        login = []
        for data in read.values():
            login.append(tuple(data.values()))
        return login

print(read_yaml())
