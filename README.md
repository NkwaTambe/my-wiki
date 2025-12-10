# My Tech Wiki 📚

A lightweight, high-performance personal knowledge base built entirely with Markdown and hosted on GitHub Pages.

![GitHub Pages](https://img.shields.io/badge/Hosted_with-GitHub_Pages-blue?logo=github&logoColor=white)
![Built with Markdown](https://img.shields.io/badge/Built_with-Markdown-000000?logo=markdown&logoColor=white)

## 📖 Overview

This repository hosts a static documentation website designed to be simple, maintainable, and fast. Unlike complex CMS platforms or heavy static site generators, this wiki relies solely on GitHub's native **Jekyll** integration.

**Key Features:**
*   **Zero Maintenance**: No servers to patch, no databases to manage.
*   **Pure Markdown**: Content is written in standard `.md` files.
*   **Git Versioned**: Full history of all changes and updates.
*   **Automatic Hosting**: Pushing to the `main` branch automatically updates the live site.

## 📂 Project Structure

The project is organized into logical directories to keep content scalable.

```text
my-wiki/
├── _config.yml               # Site configuration (Theme, Title, SEO)
├── index.md                  # The homepage (Table of Contents)
├── README.md                 # This file (Repository documentation)
└── docs/                     # Content Directory
    ├── cloud/                # Cloud computing notes (AWS, Azure, etc.)
    │   └── aws.md
    ├── systems/              # System administration & Engineering
    │   ├── linux.md
    │   ├── networking.md
    │   ├── storage.md
    │   └── boot-process.md
    └── general/              # General project info
        └── about.md
```

## 🚀 How to Use

### 1. Adding New Content
To add a new topic (e.g., "Docker"):

1.  Create a new file: `docs/cloud/docker.md`.
2.  Add the standard header to the top of the file:
    ```markdown
    # Docker Notes

    [← Back to Home](../../index.md)

    ## Content starts here...
    ```
3.  Open `index.md` and add a link to your new file:
    ```markdown
    - [**Docker Notes**](./docs/cloud/docker.md) - Containerization basics.
    ```

### 2. Local Development (Optional)
You can edit files directly on GitHub or use VS Code locally. To preview the site locally (requires Ruby & Jekyll):

```bash
bundle install
bundle exec jekyll serve
# Access at http://localhost:4000
```
*Note: Local preview is optional. GitHub Pages renders the site automatically upon push.*

## ⚙️ Configuration

The `_config.yml` file controls the site settings:

*   **title**: The name displayed in the browser tab.
*   **description**: Used for SEO and social sharing.
*   **theme**: The visual style (default: `jekyll-theme-minimal`).

## 🌐 Deployment

This site is deployed via **GitHub Pages**.

1.  Go to **Settings** > **Pages**.
2.  Select Source: **Deploy from a branch**.
3.  Branch: **main** / Folder: **root**.
4.  Click **Save**.

The site will be available at: `https://[USERNAME].github.io/[REPO-NAME]/`

## 📄 License

This project is open-source and available for personal or educational use.