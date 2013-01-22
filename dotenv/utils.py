from dotenv import Dotenv


def set_variable(file_path, key, value):
    dotenv = Dotenv(file_path)
    dotenv[key] = value


def get_variable(file_path, key):
    dotenv = Dotenv(file_path)
    return dotenv[key]