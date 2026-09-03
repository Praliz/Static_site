import os, stat
import shutil

def main():
    if os.path.exists("/mnt/c/Users/SimonThinggaard/workspace/bootdotdev/static_web/public"):
        shutil.rmtree("/mnt/c/Users/SimonThinggaard/workspace/bootdotdev/static_web/public")
        os.mkdir("/mnt/c/Users/SimonThinggaard/workspace/bootdotdev/static_web/public",)

def recurse_static():
    dir_list = os.listdir("/mnt/c/Users/SimonThinggaard/workspace/bootdotdev/static_web/Static")
    print(dir_list)
main()
recurse_static()