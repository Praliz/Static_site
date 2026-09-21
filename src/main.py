import sys
from file_manipulation import cleaning , recurse_static , generate_pages_recursive

source_dir = "Static"
dest_dir = "docs"
def main():
    
    if len(sys.argv) >1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    cleaning()
    recurse_static(source_dir,dest_dir)
    generate_pages_recursive("content" , "template.html", dest_dir,basepath)
    
main()

