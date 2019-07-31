import sys
import os
import sqlite3
def main(args):
    if not os.path.exists("dist/epili.db"):
        print("先执行 python tools/build.py")
        return
    if len(args) < 2:
        print("请在命令后面输入要搜索的人物")
        return
    name = args[1]
    with sqlite3.connect("dist/epili.db") as db:
        cur = db.cursor()

        cur.execute(f"select * from epili where name like '%{name}%'",())
        res = cur.fetchall()
        cur.close()
    for i in res:
        print("======霹雳诗号==========")
        print("名字:",i[2]+"·"+i[1])
        print("诗号:",i[6]) 
        print("=======================")


if __name__ == "__main__":
    main(sys.argv)