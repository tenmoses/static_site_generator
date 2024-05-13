import os
import shutil
from markdown_to_html import markdown_to_html
from pathlib import Path

def print_files(files, path, depth = 1):
    for file in files:
        filepath = os.path.join(path, file)
        print(f"{filepath}".rjust(len(filepath) + depth, "-"))
        if os.path.isdir(filepath):     
            print_files(os.listdir(filepath), filepath, depth + 1)

def copy_files(copy_from, copy_to):
    for file in os.listdir(copy_from):
        filepath = os.path.join(copy_from, file)
        if os.path.isfile(filepath):
            shutil.copy(filepath, copy_to)
        else:
            new_copy_to_path = os.path.join(copy_to, file)
            os.mkdir(new_copy_to_path)
            copy_files(filepath, new_copy_to_path)
            

def publish_static():
    if os.path.exists("public"):
        print("\nThese files from public will be removed:\n")
        print_files(os.listdir("public"), "public")
        shutil.rmtree("public")
        os.mkdir("public")
    else:
        print("\nCreating public directory...\n")
        os.mkdir("public")

    if os.path.exists("static"):
        print("\nThese files form static directory will be copied to public:\n")
        print_files(os.listdir("static"), "static")

        copy_files("static", "public")

        print("\nDone. Public directory content:\n")
        print_files(os.listdir("public"), "public")

def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.split("\n")[0].lstrip("# ")
    
    raise Exception("All pages need a single h1 header.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}\n")
    file = open(from_path)
    markdown = file.read()
    file.close()

    print("Extracting title\n")
    title = extract_title(markdown)

    print("Transforming markdown to html\n")
    html = markdown_to_html(markdown)

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    dest_file = open(dest_path, "x")
    dest_file.write(page)
    dest_file.close()
    
    print(f"{dest_path} - Done")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        filepath = os.path.join(dir_path_content, file)
        file_name = Path(file).stem
        if os.path.isfile(filepath):
            generate_page(filepath, template_path, os.path.join(dest_dir_path, f"{file_name}.html"))
        else:
            generate_pages_recursive(filepath, template_path, os.path.join(dest_dir_path, file))

def main():
    publish_static()
    generate_pages_recursive("content", "template.html", "public")


main()