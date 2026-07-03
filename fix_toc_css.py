import os
import re

base_dir = '/Users/karolbohdanowicz/my-ai-agents/naukaAI'
files = ['CLOUDeindex.html', 'ANTIGRAVITYindex.html']

for fname in files:
    filepath = os.path.join(base_dir, fname)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the color-mix back to rgba for default
    html = html.replace('background: color-mix(in srgb, var(--bg) 85%, transparent);', 'background: rgba(7, 8, 16, 0.85);')
    
    # Add light-mode specific toc-bar background
    light_mode_css = """  body.light-mode .toc-bar {
    background: rgba(248, 250, 252, 0.85);
  }
</style>"""
    if 'body.light-mode .toc-bar' not in html:
        html = html.replace('</style>', light_mode_css, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed toc-bar css")
