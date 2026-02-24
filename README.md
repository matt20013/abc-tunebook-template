# ABC Tunebook Template

This is a starter template for musicians to host and share their ABC sheet music on GitHub Pages. It automates the process of converting ABC files into PDFs and MP3s, and generates a simple web interface to browse and listen to the tunes.

## Features

- **Automated Compilation:** Uses GitHub Actions to automatically compile `.abc` files into PDF sheet music and MP3 audio files.
- **Web Interface:** Generates index pages for easy browsing of your PDF and MP3 collections.
- **GitHub Pages Hosting:** Deploys the result directly to GitHub Pages for free hosting.
- **ABCJS Integration:** Includes a web-based player and viewer (via `public/index.html`) to render and play tunes directly in the browser.

## How It Works

1.  **Source:** You place your ABC files in the `abcs/` directory. By default, it looks for `repertoire.abc`.
2.  **Build:** When you push changes to the `main` branch, a GitHub Action workflow (`.github/workflows/deploy-site.yml`) is triggered.
3.  **Process:**
    *   It uses `matt20013/abc_docker` to compile the ABC code.
    *   PDFs are generated in `public/pdfs`.
    *   MP3s are generated in `public/mp3s`.
    *   Directory indexes are generated using `scripts/generate_indexes.py`.
4.  **Deploy:** The contents of the `public/` directory are deployed to GitHub Pages.

## Usage

1.  **Clone or Use Template:** Use this repository as a template or clone it to your local machine.
2.  **Add Music:** Edit `abcs/repertoire.abc` or add your own `.abc` files to the `abcs/` directory.
3.  **Commit and Push:** Commit your changes and push them to the `main` branch.
4.  **View Site:** Go to your repository's "Settings" > "Pages" to see your deployed site URL (it might take a minute or two after the Action completes).

## Directory Structure

*   `abcs/`: Source directory for your ABC music files.
*   `public/`: The web root. Contains the static HTML files, and is where the build artifacts (PDFs, MP3s) are placed.
*   `scripts/`: Helper scripts for the build process (e.g., `generate_indexes.py`).
*   `.github/workflows/`: Contains the CI/CD pipeline configuration.

## Customization

You can modify `.github/workflows/deploy-site.yml` to change the input file name or output directories if needed.

## Credits

*   ABC processing provided by [matt20013/abc_docker](https://github.com/matt20013/abc_docker).
*   Frontend rendering powered by [abcjs](https://www.abcjs.net/).
