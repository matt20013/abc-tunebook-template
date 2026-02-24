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

        content = "<html><head><title>Index of /" + display_path + "</title>"
        content += """
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; padding: 10px; background: #f9f9f9; border-radius: 5px; display: flex; align-items: center; flex-wrap: wrap; }
            .file-link { flex-grow: 1; text-decoration: none; color: #333; font-weight: bold; min-width: 200px; }
            audio { margin: 10px 15px; flex-grow: 1; max-width: 400px; }
            .download-btn { text-decoration: none; color: #007bff; font-size: 0.9em; white-space: nowrap; margin-left: 10px; }
            .dir-link { font-weight: bold; color: #0056b3; }
        </style>
        </head><body>"""
        content += "<h1>Index of /" + display_path + "</h1><hr><ul>"

        # Add link to parent directory if not at start_dir
        if root != start_dir:
             content += '<li><a href="../" class="dir-link">../</a></li>\n'

        for d in sorted(dirs):
            link = urllib.parse.quote(d)
            name = html.escape(d)
            content += f'<li><a href="{link}/" class="dir-link">{name}/</a></li>\n'

        for f in sorted(files):
            if f == "index.html": continue
            link = urllib.parse.quote(f)
            name = html.escape(f)

            if f.lower().endswith('.mp3'):
                content += f'''
                <li>
                    <span class="file-link">{name}</span>
                    <audio controls src="{link}"></audio>
                    <a href="{link}" download class="download-btn">Download</a>
                </li>
                '''
            else:
                content += f'<li><a href="{link}" class="file-link">{name}</a></li>\n'

        content += "</ul><hr></body></html>"

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
