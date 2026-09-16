import os
import shutil
from markdown_blocks import markdown_to_html_node

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
    full_page = content_temp.replace("{{ Title }}",title)
    full_page = full_page.replace("{{ Content }}",html_string)
    
    dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(dest_path,"w") as file:
            file.write(full_page)
            
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file_content in os.listdir(dir_path_content):
        file_in_path = os.path.join(dir_path_content, file_content)
        if os.path.isfile(file_in_path):
            if file_in_path.endswith(".md"):
                dest_file_name = file_content.replace(".md",".html")
                dest_file_path = os.path.join(dest_dir_path,dest_file_name)
                generate_page(file_in_path,template_path,dest_file_path)
        else:
            dest_subfolder = os.path.join(dest_dir_path,file_content)
            os.makedirs(dest_subfolder,exist_ok=True)
            generate_pages_recursive(file_in_path,template_path,dest_subfolder)

