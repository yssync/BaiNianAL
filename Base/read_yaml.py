import os

import yaml


class ReadYAML():

    def __init__(self, filename):
        self.file_path = os.getcwd()+os.sep+"Data"+os.sep+filename

    def read_yaml(self):

        with open(self.file_path, "r", encoding="utf-8") as f:

            return yaml.load(f)


"""测试数据"""
# with open("../Data/login_data.yml", "r", encoding="utf-8") as f:
#
#     read = yaml.load(f)
#     print(read)