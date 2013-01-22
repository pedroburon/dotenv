__version__ = '0.0.1'


class Dotenv(dict):
    def __init__(self, file_path):
        self.file_path = file_path
        super(Dotenv, self).__init__(**self.__create_dict())

    def __create_dict(self):
        with open(self.file_path, 'r') as dotenv:
            variables = {}
            for line in dotenv.readlines():
                variables.update(self.__parse_line(line))
            return variables

    def __parse_line(self, line):
        key, value = map(lambda x: x.strip().strip('\'').strip('"'), line.split('='))
        return {key: value}

    def __persist(self):
        with open(self.file_path, 'w') as dotenv:
            for key, value in self.items():
                dotenv.write("%s=%s\n" % (key, value))

    def __setitem__(self, key, value):
        super(Dotenv, self).__setitem__(key, value)
        self.__persist()

    def __delitem__(self, key):
        super(Dotenv, self).__delitem__(key)
        self.__persist()

def set_variable(file_path, key, value):
    dotenv = Dotenv(file_path)
    dotenv[key] = value


def get_variable(file_path, key):
    dotenv = Dotenv(file_path)
    return dotenv[key]


def get_variables(file_path):
    return Dotenv(file_path)