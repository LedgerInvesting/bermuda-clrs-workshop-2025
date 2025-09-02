#!/usr/bin/env python3
"""
Simple landing page builder that doesn't interfere with JupyterLite's index.html
"""

import markdown
from pathlib import Path

def build_simple_landing():
    """Create home.html without touching JupyterLite's index.html."""
    
    # Read README.md
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("⚠️  README.md not found")
        return False
    
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'tables'])
    readme_html = md.convert(readme_content)
    
    # Same clean HTML template as before
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
        
        .launch-section {
            background: #f8f9fa;
            border: 1px solid #e1e4e8;
            margin: -16px -16px 30px -16px;
            padding: 25px 20px;
            border-radius: 6px;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .launch-title {
            color: #1f2328;
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
        
        .readme-content p {
            margin-bottom: 16px;
        }
        
        .readme-content ul, .readme-content ol {
            padding-left: 2em;
            margin-bottom: 16px;
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
        
        .footer {
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #e1e4e8;
            text-align: center;
            color: #586069;
            font-size: 14px;
        }
    </style>
</head>
<body>
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
    
    <div class="readme-content">
        {readme_content}
    </div>
    
    <div class="footer">
        <p>🏝️ Bermuda CLRS Workshop 2025 | Powered by JupyterLite & Pyodide</p>
        <p>
            <a href="https://github.com/LedgerInvesting/bermuda-clrs-workshop-2025">GitHub Repository</a> |
            <a href="https://jupyterlite.readthedocs.io">JupyterLite Docs</a>
        </p>
    </div>
</body>
</html>"""
    
    final_html = html_template.replace("{readme_content}", readme_html)
    
    # Only create home.html, don't touch index.html
    if Path("dist").exists():
        with open("dist/home.html", 'w') as f:
            f.write(final_html)
        print("✅ Created home.html landing page")
        print("🌐 Access at: /home.html")
        print("⚠️  JupyterLite default behavior preserved at: /")
        return True
    
    return False

if __name__ == "__main__":
    try:
        import markdown
    except ImportError:
        print("⚠️  Installing markdown module...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
        import markdown
    
    if build_simple_landing():
        print("\n✅ Simple landing page created!")
        print("📍 Landing page: http://localhost:8000/home.html")
        print("🔬 JupyterLab: http://localhost:8000/lab")
        print("📓 Notebooks: http://localhost:8000/notebooks") 
        print("💻 Console: http://localhost:8000/consoles")
    else:
        print("❌ Failed to create landing page")