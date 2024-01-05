
from dorothy_datasets import download
import os

token = os.environ['DOROTHY_TOKEN']
basepath = os.getcwd()


download(token , 'china', basepath=basepath)


