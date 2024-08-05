import json


class JsonUtils:

    @classmethod
    def json_file_to_dict(cls, _file_path):
        config = None
        with open(_file_path) as config_file:
            config = json.load(config_file)
        return config
