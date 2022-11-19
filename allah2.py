# made by rubidium, edit 9th line as your resources, it will ensure them.

import os

def main():
    resources = os.listdir(os.path.expanduser("~/Desktop/resources"))
    with open(os.path.expanduser("~/Desktop/resources/server.cfg"), "w") as f:
        for resource in resources:            
            if resource.startswith("hyx") or resource.startswith("hy-lib") or resource.startswith("hy-base"):
                f.write("ensure " + resource + "\n")
            else:
                f.write("start " + resource + "\n")


if __name__ == "__main__":
    main()
