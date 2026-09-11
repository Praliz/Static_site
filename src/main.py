
from file_manipulation import cleaning , recurse_static , generate_page

source_dir = "Static"
dest_dir = "public"
def main():
    cleaning()
    recurse_static(source_dir,dest_dir)
    generate_page("content/index.md" , "src/template.html", "/public")

main()

