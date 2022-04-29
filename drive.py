from pathlib import Path
from urllib import request
import json
import requests
import shutil
import glob
import os
import datetime

auth = {"Authorization": "{{input_auth}}"}

Path = ("./user")
ct = datetime.datetime.now()
time = ct.strftime("%Y_%m_%d %S")
print('foldername : '+str (time))
folder_name = time + ' User'
os.mkdir(folder_name)
zi = shutil.make_archive(time + ' User','zip', Path)
shutil.move(zi,folder_name)

dir_list = os.listdir("./")
os.chdir(folder_name)

for file in glob.glob("*"):
    with open(file,"rb") as f:
        fn = os.path.basename(f.name)
        
        param = {
            "name": fn ,
            "parents":["{{input_parent_folder}}"]
        }
        files = {
            'data': ('metadata', json.dumps(param), 'application/json; charset=UTF-8'),
            'file': open(os.path.basename(f.name), "rb")
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=auth,
            files=files
        )
        print(r.text)