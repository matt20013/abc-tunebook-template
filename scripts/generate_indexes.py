import os
import sys
import html
import urllib.parse

def generate_index(start_dir):
    for root, dirs, files in os.walk(start_dir):
        # Determine relative path from start_dir to current root
        rel_path = os.path.relpath(root, start_dir)
        if rel_path == ".":
            rel_path = ""

        title_path = rel_path if rel_path else os.path.basename(start_dir)
        display_path = html.escape(title_path)

        content = "<html><head><title>Index of /" + display_path + "</title></head><body>"
        content += "<h1>Index of /" + display_path + "</h1><hr><pre>"

        # Add link to parent directory if not at start_dir
        if root != start_dir:
             content += '<a href="../">../</a>\n'

        for d in sorted(dirs):
            link = urllib.parse.quote(d)
            name = html.escape(d)
            content += f'<a href="{link}/">{name}/</a>\n'
        for f in sorted(files):
            if f == "index.html": continue
            link = urllib.parse.quote(f)
            name = html.escape(f)
            content += f'<a href="{link}">{name}</a>\n'

        content += "</pre><hr></body></html>"

        with open(os.path.join(root, "index.html"), "w") as f:
            f.write(content)
        print(f"Generated index for {root}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_indexes.py <directory> [directory ...]")
        sys.exit(1)

    for directory in sys.argv[1:]:
        if os.path.isdir(directory):
            generate_index(directory)
        else:
            print(f"Directory not found: {directory}")
