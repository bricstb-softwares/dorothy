
from dorothy_datasets import download_china_from_server
import os

token = os.environ['DOROTHY_TOKEN']
basepath = os.getcwd()


download_china_from_server(token , basepath=basepath)


