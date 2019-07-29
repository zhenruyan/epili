import os
import json
import sqlite3
print("build start ...")

file_list=os.listdir("data")
json_list = []

def build_json():
    for item  in file_list:
        with open(f"data/{item}") as json_file:
            print(f"load {item} ing")
            json_list.append(json.load(json_file)) 
    dist_file = open("dist/epili.json","w")
    dist_file.write(json.dumps(json_list,ensure_ascii=False))
    dist_file.close()
    print("build json success")

def build_db():
    pass

if __name__ == "__main__":
    build_json()
    build_db()