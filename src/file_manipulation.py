import os
import shutil
from markdown_to_html_node import markdown_to_html_node

source_dir = "Static"
dest_dir = "public"

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
            
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ").strip()
    raise Exception("No H1 was found")

def generate_page(from_path , template_path, dest_path):
    print(f"Generating Page from:{from_path} to:{dest_path} using:{template_path}")
    with open(from_path) as file:
        content_from = file.read()
        title = extract_title(content_from)
    with open(template_path) as file:
        content_temp = file.read()
    html_node = markdown_to_html_node(content_from)
    html_string = html_node.to_html()
    content_temp.replace("{{ Title }}",title)
    content_temp.replace("{{Content}}",html_string)
    