import sys
import build

def main(name):
    print(name)


if __name__ == "__main__":
    build.build_json()
    build.build_db()
    main(sys.argv[1])