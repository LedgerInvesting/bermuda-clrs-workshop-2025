#!/usr/bin/env python3
"""
Alternative landing page builder that works around JupyterLite's index.html override.
"""

import markdown
from pathlib import Path

def build_landing_page_alt():
    """Create landing page as home.html and modify JupyterLite to redirect there."""
    
    # Read README.md
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("⚠️  README.md not found, using default content")
        readme_content = "# Bermuda CLRS Workshop 2025\n\nWelcome to the JupyterLite environment!"
    else:
        with open(readme_path, 'r') as f:
            readme_content = f.read()
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'tables'])
    readme_html = md.convert(readme_content)
    
    # Same HTML template as before
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bermuda CLRS Workshop 2025 - JupyterLite</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
            line-height: 1.5;
            color: #1f2328;
            max-width: 1012px;
            margin: 0 auto;
            padding: 16px;
            background: #ffffff;
            font-size: 16px;
        }
        
        /* Launch Section - Clean Business Style */
        .launch-section {
            background: #f8f9fa;
            border: 1px solid #e1e4e8;
            margin: -20px -20px 30px -20px;
            padding: 25px 20px;
            border-radius: 6px;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .launch-title {
            color: #24292e;
            margin: 0 0 20px 0;
            font-size: 20px;
            font-weight: 600;
            text-align: center;
        }
        
        .launch-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .launch-button {
            display: inline-flex;
            align-items: center;
            padding: 10px 20px;
            background: #0969da;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            border: 1px solid transparent;
        }
        
        .launch-button:hover {
            background: #0860ca;
            text-decoration: none;
        }
        
        .launch-button.secondary {
            background: #f6f8fa;
            color: #24292e;
            border: 1px solid #d0d7de;
        }
        
        .launch-button.secondary:hover {
            background: #f3f4f6;
        }
        
        .launch-button .icon {
            margin-right: 6px;
            font-size: 16px;
        }
        
        /* README Content Styling - Authentic GitHub-like */
        .readme-content {
            padding: 0 24px;
            max-width: none;
        }
        
        .readme-content h1 {
            font-size: 2em;
            font-weight: 600;
            padding-bottom: 10px;
            border-bottom: 1px solid #d0d7de;
            margin-top: 0;
            margin-bottom: 16px;
            line-height: 1.25;
        }
        
        .readme-content h2 {
            font-size: 1.5em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            padding-bottom: 7px;
            border-bottom: 1px solid #d0d7de;
            line-height: 1.25;
        }
        
        .readme-content h3 {
            font-size: 1.25em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
        }
        
        .readme-content h4 {
            font-size: 1em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
        }
        
        .readme-content h5 {
            font-size: 0.875em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
        }
        
        .readme-content h6 {
            font-size: 0.85em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
            color: #656d76;
        }
        
        .readme-content p {
            margin-bottom: 16px;
        }
        
        .readme-content ul, .readme-content ol {
            padding-left: 2em;
            margin-bottom: 16px;
        }
        
        .readme-content li {
            margin-bottom: 8px;
        }
        
        .readme-content code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(175,184,193,0.2);
            border-radius: 6px;
            font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
        }
        
        .readme-content pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
            margin-bottom: 16px;
            border: 1px solid #d0d7de;
        }
        
        .readme-content pre code {
            display: inline;
            padding: 0;
            margin: 0;
            border: 0;
            background-color: transparent;
            border-radius: 0;
            font-size: 100%;
        }
        
        .readme-content blockquote {
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin-bottom: 16px;
        }
        
        .readme-content table {
            border-spacing: 0;
            border-collapse: collapse;
            margin-bottom: 16px;
            width: 100%;
        }
        
        .readme-content table th {
            font-weight: 600;
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
            background-color: #f6f8fa;
        }
        
        .readme-content table td {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }
        
        .readme-content table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }
        
        .readme-content a {
            color: #0366d6;
            text-decoration: none;
        }
        
        .readme-content a:hover {
            text-decoration: underline;
        }
        
        .readme-content img {
            max-width: 100%;
            box-sizing: content-box;
            background-color: #fff;
        }
        
        /* Footer */
        .footer {
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #e1e4e8;
            text-align: center;
            color: #586069;
            font-size: 14px;
        }
        
        /* Mobile responsive */
        @media (max-width: 768px) {
            .launch-section {
                position: relative;
            }
            
            .launch-buttons {
                flex-direction: column;
            }
            
            .launch-button {
                width: 100%;
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <!-- Launch Section with Buttons -->
    <div class="launch-section">
        <h1 class="launch-title">JupyterLite Environment</h1>
        <div class="launch-buttons">
            <a href="lab/index.html" class="launch-button">
                <span class="icon">🔬</span>
                JupyterLab
            </a>
            <a href="notebooks/index.html" class="launch-button secondary">
                <span class="icon">📓</span>
                Classic Notebooks
            </a>
            <a href="consoles/index.html" class="launch-button secondary">
                <span class="icon">💻</span>
                Python Console
            </a>
        </div>
    </div>
    
    <!-- README Content -->
    <div class="readme-content">
        {readme_content}
    </div>
    
    <!-- Footer -->
    <div class="footer">
        <p>🏝️ Bermuda CLRS Workshop 2025 | Powered by JupyterLite & Pyodide</p>
        <p>
            <a href="https://github.com/LedgerInvesting/bermuda-clrs-workshop-2025">GitHub Repository</a> |
            <a href="https://jupyterlite.readthedocs.io">JupyterLite Docs</a>
        </p>
    </div>
</body>
</html>"""
    
    # Replace placeholder with converted README content
    final_html = html_template.replace("{readme_content}", readme_html)
    
    # Create home.html instead of overwriting index.html
    with open("home.html", 'w') as f:
        f.write(final_html)
    print("✅ Generated home.html from README.md")
    
    if Path("dist").exists():
        with open("dist/home.html", 'w') as f:
            f.write(final_html)
        print("✅ Copied home.html to dist/")
    
    # Now create a simple index.html that redirects to home.html
    redirect_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting to Bermuda Workshop...</title>
    <script>
        // Redirect to home.html immediately
        window.location.href = './home.html';
    </script>
    <meta http-equiv="refresh" content="0;url=./home.html">
</head>
<body>
    <div style="text-align: center; margin-top: 100px; font-family: Arial, sans-serif;">
        <h1>🏝️ Bermuda CLRS Workshop 2025</h1>
        <p>Redirecting to workshop home...</p>
        <p><a href="./home.html">Click here if not redirected automatically</a></p>
    </div>
</body>
</html>"""
    
    # Only create the redirect if dist exists (we don't want to overwrite the root index.html manually)
    if Path("dist").exists():
        # Wait a moment and then overwrite JupyterLite's index.html with our redirect
        import time
        time.sleep(0.1)  # Give filesystem a moment
        
        with open("dist/index.html", 'w') as f:
            f.write(redirect_html)
        print("✅ Created redirect from index.html to home.html")
    
    return True

if __name__ == "__main__":
    # Check if markdown module is available
    try:
        import markdown
    except ImportError:
        print("⚠️  Installing markdown module...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
        import markdown
    
    build_landing_page_alt()
    print("\n📄 Alternative landing page built successfully!")
    print("🏠 Landing page: home.html")
    print("🔄 Redirect: index.html -> home.html")
    print("🌐 To preview: python -m http.server 8000 --directory dist")