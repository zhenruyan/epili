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
    if os.path.exists("dist/epili.db"):
        os.remove("dist/epili.db")
    db = sqlite3.connect("dist/epili.db")
    db.execute("""
    create table epili
(
    id     char not null
        constraint epili_pk
            primary key,
    name   varchar,
    title  varchar,
    level  varchar,
    race   varchar,
    sects  varchar,
    poetry text,
    desc   text,
    img    text
);

    """)
    db.commit()
    for i in json_list:
        db.execute(
            """
            INSERT INTO "epili" 
            ("id", "name", "title", 
            "level", "race", "sects",
             "poetry", "desc", "img") 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
             ,(i["id"],i["name"],i["title"],i["level"],i["race"],i["sects"],json.dumps(i["poetry"],ensure_ascii=False),i["desc"],json.dumps(i["img"],ensure_ascii=False),))
    db.commit()
    db.close()
    print("sqlite build done")
if __name__ == "__main__":
    build_json()
    build_db()