
from file_manipulation import cleaning , recurse_static , generate_pages_recursive

source_dir = "Static"
dest_dir = "public"
def main():
    cleaning()
    recurse_static(source_dir,dest_dir)
    generate_pages_recursive("content" , "template.html", "public")
    
main()

