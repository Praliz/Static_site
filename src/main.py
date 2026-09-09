import os
import shutil

source_dir = "Static"
dest_dir = "public"
def main():
    cleaning()
    recurse_static(source_dir,dest_dir)

def cleaning():
    if os.path.exists("public"):
        shutil.rmtree("public")
        os.mkdir("public")
    else:
        os.mkdir("public")

def recurse_static(source_dir , dest_dir):
    if not os.path.exists(dest_dir):    
        os.mkdir(dest_dir)
    for file_name in os.listdir(source_dir):
        source_path = os.path.join(source_dir,file_name)
        destination_path = os.path.join(dest_dir,file_name)
        if os.path.isfile(source_path):
            print(f"this is a file and its transferred {source_path} -> {destination_path}")
            shutil.copy(source_path,destination_path)
        else:
            print(f"this is not a file{source_path}")
            recurse_static(source_path,destination_path)
main()

