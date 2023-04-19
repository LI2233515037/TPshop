import sys
import os

sys.path.append(os.getcwd())
import yaml
import json


def read_yaml():
    with open('/TPshop_front_desk/data/login.json', encoding="utf-8")as f:
        read = json.load(f)
        login = []
        for data in read.values():
            login.append(tuple(data.values()))
        return login

# print(read_yaml())
